import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal

from src.features import build_features, cs_rank, forward_return

CUT = 300


def _prices(T=400, N=5, seed=0):
    rng = np.random.default_rng(seed)
    r = rng.normal(0.0005, 0.02, size=(T, N))
    idx = pd.date_range("2020-01-01", periods=T, freq="B")
    return pd.DataFrame(100 * np.cumprod(1 + r, axis=0), index=idx, columns=list("ABCDE"))


def _tamper(close, cut=CUT):
    """把第 cut 列之後的價格全換成雜訊。"""
    out = close.copy()
    rng = np.random.default_rng(1)
    out.iloc[cut + 1:] = rng.uniform(50, 150, size=out.iloc[cut + 1:].shape)
    return out


def test_features_no_lookahead():
    close = _prices()
    a, b = build_features(close), build_features(_tamper(close))
    for name in a:
        assert_frame_equal(a[name].iloc[:CUT + 1], b[name].iloc[:CUT + 1], obj=name)


def test_check_detects_centered_rolling():
    """測試要會失敗：故意寫一個偷看未來的特徵，上面那種檢查必須抓得到。"""
    def leaky(c):
        ret = c / c.shift(1) - 1
        return ret.rolling(60, center=True, min_periods=48).std()

    close = _prices()
    assert not leaky(close).iloc[:CUT + 1].equals(leaky(_tamper(close)).iloc[:CUT + 1])


def test_forward_return_handcalc():
    # h=2，決策日 t=1：bars 3,4 的報酬為 +10%、+10%，複利 1.1*1.1-1 = 0.21
    o = pd.DataFrame({"A": [100.0, 100.0, 100.0, 110.0, 121.0, 121.0]})
    y = forward_return(o, h=2)["A"]
    assert np.isclose(y.iloc[1], 1.1 * 1.1 - 1)
    assert np.isclose(y.iloc[0], 0.10)
    assert np.isclose(y.iloc[2], 0.10)
    assert y.iloc[3:].isna().all()          # 最後 h+1 天沒有完整標籤


def test_cs_rank_range_and_nan():
    df = pd.DataFrame([[3.0, 1.0, 2.0, np.nan]])
    assert np.allclose(cs_rank(df).iloc[0], [1 / 3, -1 / 3, 0.0, 0.0])
    assert np.isnan(cs_rank(df, fill=None).iloc[0, 3])


def test_cs_rank_each_day_independent():
    a = pd.DataFrame([[1.0, 2.0, 3.0], [10.0, 5.0, 7.0]])
    b = a.copy()
    b.iloc[1] = [100.0, 1.0, 50.0]
    assert_frame_equal(cs_rank(a).iloc[[0]], cs_rank(b).iloc[[0]])
