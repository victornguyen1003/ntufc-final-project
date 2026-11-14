"""資料驗證：回傳每一類異常的筆數，全為 0 才表示資料可以放心使用。"""
import pandas as pd


def validate(prices: pd.DataFrame) -> dict:
    close = prices["close"]
    ret = close.groupby(level="ticker").pct_change()

    checks = {
        "價格 <= 0": int((prices[["open", "high", "low", "close"]] <= 0).any(axis=1).sum()),
        "high < low": int((prices["high"] < prices["low"]).sum()),
        "成交量為 0": int((prices["volume"] == 0).sum()),
        "缺值": int(prices.isna().any(axis=1).sum()),
        "(股票, 日期) 重複": int(prices.index.duplicated().sum()),
        "日報酬超出 ±10.5%": int((ret.abs() > 0.105).sum()),
    }
    return checks


def main():
    prices = pd.read_parquet("data/raw/prices.parquet")
    print(f"資料形狀: {prices.shape}")
    for name, n in validate(prices).items():
        flag = "OK " if n == 0 else "請檢查"
        print(f"[{flag}] {name}: {n}")


if __name__ == "__main__":
    main()
