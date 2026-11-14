import numpy as np
import pandas as pd

from src.baseline import run_equal_weight


def test_engine_hand_calc():
    R = np.zeros((12, 2))
    R[5] = [0.10, -0.10]          # 只有第 5 天有報酬：A +10%，B -10%
    ret = pd.DataFrame(R, index=pd.date_range("2020-01-01", periods=12),
                       columns=["A", "B"])
    net, gross, turn = run_equal_weight(ret, h=10, c_buy=0.002, c_sell=0.005)

    assert np.isclose(net.iloc[1], -0.002)        # 第一次建倉只扣買進成本
    assert np.isclose(gross.iloc[5], 0.0)         # 漲跌抵銷，組合毛報酬為 0
    assert np.isclose(net.iloc[11], -0.00035)     # 漂移後再平衡的成本
    assert np.allclose(turn, [1.0, 0.05])         # 換手紀錄
