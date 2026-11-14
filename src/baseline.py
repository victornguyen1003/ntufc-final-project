"""W1 baseline：等權重、每 H 個交易日調倉、含買賣不對稱成本。

時序：決策日 t 收盤後定目標權重，t+1 開盤成交（= 第 t+1 根 bar 結束），
新權重從第 t+2 根 bar 起賺報酬。（對應計畫書第 17 章）
"""
import numpy as np
import pandas as pd

C_BUY, C_SELL = 0.001925, 0.004925   # 手續費 0.1425% (+證交稅 0.3% 僅賣出) + 滑價 0.05%
H = 10                               # 調倉間隔（交易日）


def load_returns(path="data/processed/prices_clean.parquet"):
    """回傳 (日期 x 股票) 的開盤到開盤報酬；NaN 先視為 0（簡化，需在報告註明）。"""
    p = pd.read_parquet(path)
    op = p["open"].unstack("ticker")          # 長表 -> 寬表
    ret = op / op.shift(1) - 1                # 寬表上 shift(1) 已是每檔各自往前一天
    return ret.iloc[1:].fillna(0.0)


def run_equal_weight(ret, h=H, c_buy=C_BUY, c_sell=C_SELL):
    R = ret.to_numpy()
    T, N = R.shape
    target = np.full(N, 1.0 / N)
    w = np.zeros(N)
    invested = False
    net = np.zeros(T)
    gross = np.zeros(T)
    turnover = []
    pending = None
    for s in range(T):
        if s % h == 0:
            pending = target                   # 決策日 s 收盤後決定；下一根 bar 結束時成交
        rp = 0.0
        if invested:
            rp = float(w @ R[s])
            w = w * (1 + R[s]) / (1 + rp)      # 漂移
        gross[s] = rp
        cost = 0.0
        if pending is not None and s % h == 1 or (pending is not None and s == 1):
            buys = np.clip(pending - w, 0, None).sum()
            sells = np.clip(w - pending, 0, None).sum()
            cost = c_buy * buys + c_sell * sells
            turnover.append(buys)
            w, invested, pending = pending.copy(), True, None
        net[s] = (1 + rp) * (1 - cost) - 1
    idx = ret.index
    return (pd.Series(net, idx, name="net"), pd.Series(gross, idx, name="gross"),
            np.array(turnover))


def perf(r, ppy=252):
    r = np.asarray(r, float)
    nav = np.cumprod(1 + r)
    return {
        "年化報酬": nav[-1] ** (ppy / len(r)) - 1,
        "年化波動": r.std(ddof=1) * np.sqrt(ppy),
        "Sharpe": r.mean() / r.std(ddof=1) * np.sqrt(ppy),
        "最大回撤": (nav / np.maximum.accumulate(nav) - 1).min(),
    }


def main():
    ret = load_returns()
    net, gross, turn = run_equal_weight(ret)
    for name, r in [("毛報酬", gross), ("淨報酬", net)]:
        print(name, {k: round(v, 4) for k, v in perf(r.iloc[1:]).items()})
    print("調倉次數:", len(turn), " 年化換手(單邊買入):", round(turn[1:].mean() * 252 / H, 3))

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from pathlib import Path
    Path("results").mkdir(exist_ok=True)
    ((1 + net).cumprod()).plot(label="net")
    ((1 + gross).cumprod()).plot(label="gross")
    plt.legend(); plt.title("Equal-weight baseline (20 large caps)")
    plt.savefig("results/baseline_nav.png", dpi=120)
    print("已存 results/baseline_nav.png")


if __name__ == "__main__":
    main()
