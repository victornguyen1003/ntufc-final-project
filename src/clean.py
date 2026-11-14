"""清洗層：data/raw -> data/processed。每條規則的理由見 docs/data_sources.md。"""
from pathlib import Path

import pandas as pd

RAW = Path("data/raw/prices.parquet")
OUT = Path("data/processed/prices_clean.parquet")
PRICE_COLS = ["open", "high", "low", "close"]


def clean(prices: pd.DataFrame):
    dates = prices.index.get_level_values("date")

    # 規則 1：當天所有股票成交量都是 0 -> 市場沒開，整天刪除
    all_zero = (prices["volume"] == 0).groupby(level="date").all()
    closed = all_zero[all_zero].index
    out = prices[~dates.isin(closed)].copy()

    # 規則 2：市場有開、個股成交量為 0 -> 價格是舊資料，設為 NaN（不刪列、不編造）
    stale = out["volume"] == 0
    out.loc[stale, PRICE_COLS] = float("nan")
    return out, closed, int(stale.sum())


def main():
    prices = pd.read_parquet(RAW)
    out, closed, n_stale = clean(prices)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    out.to_parquet(OUT)
    print(f"刪除休市日 {len(closed)} 天，共 {len(prices) - len(out)} 列")
    print(f"個股價格設為 NaN：{n_stale} 列")
    print(f"清洗後：{len(out)} 列 -> {OUT}")


if __name__ == "__main__":
    main()
