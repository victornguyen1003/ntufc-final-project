"""特徵、標籤與橫斷面 rank（W2）。

所有資料都是寬表：index = date（交易日），columns = ticker。
寬表上每一欄是一檔股票，所以 shift / rolling 只在單檔內運算，不會跨股票。

時序慣例（與 baseline.py 一致）：
    決策日 t 收盤後算特徵（只用 t 以前的資料）
    -> t+1 開盤成交
    -> 標籤 = open[t+1] 到 open[t+h+1] 的報酬
"""
from pathlib import Path

import pandas as pd

H = 10
PROCESSED = Path("data/processed/prices_clean.parquet")
OUT = Path("data/processed/features.parquet")


def load_wide(path=PROCESSED):
    """讀清洗後的長表，轉成 (日期 x 股票) 的開盤價與收盤價寬表。"""
    p = pd.read_parquet(path)
    return p["open"].unstack("ticker"), p["close"].unstack("ticker")


def build_features(close):
    """回傳 {特徵名: 寬表}。第 t 列只使用第 t 列以前的資料。"""
    ret = close / close.shift(1) - 1
    return {
        "mom_12_1": close.shift(21) / close.shift(252) - 1,   # 跳過最近一個月
        "rev_5": close / close.shift(5) - 1,
        "rev_21": close / close.shift(21) - 1,
        "vol_60": ret.rolling(60, min_periods=48).std(),
    }


def forward_return(open_, h=H, exec_lag=1):
    """標籤：決策日 t 的 open[t+exec_lag] 到 open[t+exec_lag+h] 的報酬。

    注意：這個函式刻意使用未來資料，只能用來當標籤，絕不能當特徵。
    最後 exec_lag+h 列沒有完整標籤，自動為 NaN。
    """
    return open_.shift(-(exec_lag + h)) / open_.shift(-exec_lag) - 1


def cs_rank(df, fill=0.0):
    """橫斷面 rank：每個日期（每一列）獨立，映射到 (-0.5, 0.5)。

    fill=0.0：缺值補 0（= 中位數），用於特徵。
    fill=None：缺值保留 NaN，用於標籤（沒有標籤的日子不能當成 0）。
    """
    n = df.notna().sum(axis=1)                       # 每個日期有幾檔有值
    out = df.rank(axis=1).sub(0.5).div(n, axis=0).sub(0.5)
    return out if fill is None else out.fillna(fill)


def build_dataset(open_, close, h=H):
    feats = build_features(close)
    X = {k: cs_rank(v) for k, v in feats.items()}
    y_raw = forward_return(open_, h)
    y_rank = cs_rank(y_raw, fill=None)
    return feats, X, y_raw, y_rank


def to_long(X, y_raw, y_rank):
    """寬表轉回與前面階段一致的長表 (ticker, date)。"""
    cols = {**X, "y_raw": y_raw, "y_rank": y_rank}
    return pd.DataFrame({k: v.unstack() for k, v in cols.items()})


def main():
    open_, close = load_wide()
    feats, X, y_raw, y_rank = build_dataset(open_, close)

    print("== 各特徵缺失率（rank 前）==")
    for k, v in feats.items():
        print(f"{k:10s} {v.isna().mean().mean():.3%}")
    print(f"{'label':10s} {y_raw.isna().mean().mean():.3%}")

    out = to_long(X, y_raw, y_rank)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    out.to_parquet(OUT)
    print(f"已存入 {OUT}，形狀 {out.shape}")


if __name__ == "__main__":
    main()
