# tw-quant-pipeline

台股量化研究流程：資料 -> 驗證 -> 清洗 -> 回測。
目前進度為 W1：用 20 檔大型股跑通「含交易成本的等權重 baseline」。

## 目前的範圍與限制

- 標的：20 檔台股大型股，2015-2024，日資料，來源為 Yahoo Finance (yfinance)。
- 這 20 檔是以今天的眼光挑選，含前視偏誤。baseline 績效不能當研究結論，
  只用來證明引擎能端到端運作。正式版將改用點時股票池。
- NaN 報酬暫時視為 0（簡化），正式引擎要另外處理。

## 環境安裝

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

## 一鍵執行

    python run_pipeline.py                   # 下載 -> 驗證 -> 清洗 -> 回測
    python run_pipeline.py --skip-download   # 已有 data/raw 時略過下載

預期結果（同樣輸入必得同樣輸出）：淨 Sharpe 約 0.99、調倉 243 次、年化換手約 0.368。
圖會存到 results/baseline_nav.png。

## 測試

    python -m pytest -v

test_baseline.py 以手算案例驗證回測引擎（建倉成本、權重漂移、再平衡成本、換手）。

## 專案結構

    src/data.py        下載日價量，存 data/raw/prices.parquet
    src/validate.py    原始資料驗證報表
    src/clean.py       清洗：刪休市日、凍結價設為 NaN，存 data/processed/
    src/baseline.py    等權重、每 10 個交易日調倉、買賣不對稱成本
    tests/             單元測試
    docs/              資料來源實測紀錄 (data_sources.md)
    run_pipeline.py    一鍵執行

## 時序與成本假設

- 報酬為開盤到開盤。決策日 t 收盤後定權重，t+1 開盤成交，t+2 起賺報酬。
- 買進成本 0.1925%（手續費 0.1425% + 滑價 0.05%）。
- 賣出成本 0.4925%（手續費 0.1425% + 證交稅 0.3% + 滑價 0.05%）。

## 資料

原始資料不進 repo（見 .gitignore）。執行 run_pipeline.py 會自行下載。
已知資料問題與處理規則見 docs/data_sources.md。
