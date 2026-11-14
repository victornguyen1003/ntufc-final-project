"""資料層：下載台股日價量並存成 parquet。

輸出格式（之後換資料來源時必須維持不變）：
    index   = MultiIndex (ticker, date)
    columns = open, high, low, close, volume
    價格為還原權息後的價格
"""
from pathlib import Path

import pandas as pd
import yfinance as yf

# 20 檔大型股（Yahoo 代碼：台股上市加 .TW）
TICKERS = [
    "2330.TW", "2317.TW", "2454.TW", "2303.TW", "2308.TW",  # 台積電 鴻海 聯發科 聯電 台達電
    "2382.TW", "2357.TW", "2412.TW", "2882.TW", "2881.TW",  # 廣達 華碩 中華電 國泰金 富邦金
    "2891.TW", "2886.TW", "2884.TW", "1301.TW", "1303.TW",  # 中信金 兆豐金 玉山金 台塑 南亞
    "2002.TW", "2603.TW", "1216.TW", "2912.TW", "2207.TW",  # 中鋼 長榮 統一 統一超 和泰車
]
RAW_DIR = Path("data/raw")


def download_prices(tickers, start, end):
    """下載日資料，回傳長表 (ticker, date) x (open, high, low, close, volume)。"""
    raw = yf.download(
        tickers, start=start, end=end,
        auto_adjust=True,   # 開高低收全部做還原權息
        group_by="ticker",  # 欄位先分股票、再分價量欄
        progress=False,
    )
    long = pd.concat({t: raw[t] for t in tickers}, names=["ticker", "date"])
    long.columns = [c.lower() for c in long.columns]
    long = long.dropna(how="all").sort_index()
    return long[["open", "high", "low", "close", "volume"]]


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    prices = download_prices(TICKERS, start="2015-01-01", end="2025-01-01")
    out = RAW_DIR / "prices.parquet"
    prices.to_parquet(out)
    print(f"已存入 {out}，共 {len(prices)} 列")
    print(prices.groupby("ticker").size().to_string())  # 每檔有幾個交易日


if __name__ == "__main__":
    main()
