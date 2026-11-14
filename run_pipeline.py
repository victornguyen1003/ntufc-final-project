"""一鍵執行：下載 -> 驗證 -> 清洗 -> 回測。

用法：
    python run_pipeline.py                  # 完整流程
    python run_pipeline.py --skip-download  # 已有 data/raw 時略過下載
"""
import argparse

from src import baseline, clean, data, validate


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-download", action="store_true")
    args = ap.parse_args()

    if not args.skip_download:
        print("== 1/4 下載 ==");  data.main()
    print("== 2/4 驗證原始資料 =="); validate.main()
    print("== 3/4 清洗 ==");        clean.main()
    print("== 4/4 回測 ==");        baseline.main()


if __name__ == "__main__":
    main()
