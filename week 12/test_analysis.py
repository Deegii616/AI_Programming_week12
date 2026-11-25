from pathlib import Path

import pandas as pd

from analysis import 정제, 반별평균


data_dir = Path(__file__).resolve().parent
df = 정제(pd.read_csv(data_dir / "scores_2026.csv"))
mini = 정제(
    pd.read_csv(
        data_dir / "mini.csv",
        sep="\t",
        skiprows=1,
        header=None,
        names=["학번", "이름", "반", "과목", "점수"],
    )
)


def test_정제하면_100행이_남는다():
    assert len(df) == 100


def test_반은_두_종류만_남는다():
    assert sorted(df["반"].unique()) == ["1반", "2반"]


def test_그룹합이_전체합과_같다():
    assert df.groupby("반")["점수"].sum().sum() == df["점수"].sum()


def test_손계산과_일치한다():
    assert 반별평균(mini)["1반"] == 80.0