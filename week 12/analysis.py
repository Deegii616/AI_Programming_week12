from pathlib import Path
import pandas as pd


def 정제(df):
    # 작업용 복사본 만들기
    df = df.copy()
    print("시작", len(df))

    # 1) 점수가 비어 있는 행 삭제
    df = df.dropna(subset=["점수"])
    print("빈 칸 제거", len(df))

    # 2) 모든 열이 완전히 같은 중복 행 제거
    df = df.drop_duplicates()
    print("중복 제거", len(df))

    # 3) 반과 과목의 앞뒤 공백 제거
    df["반"] = df["반"].str.strip()
    df["과목"] = df["과목"].str.strip()

    # 4) 점수가 0~100 범위 밖인 행 삭제
    df = df[(df["점수"] >= 0) & (df["점수"] <= 100)]
    print("범위 밖 제거", len(df))

    return df


def 반별평균(df):
    통계표 = df.groupby("반")["점수"].agg(
        ["count", "mean", "median", "max"]
    ).round(2)
    print(통계표)
    return 통계표["mean"]


if __name__ == "__main__":
    csv_path = Path(__file__).resolve().parent / "scores_2026.csv"
    정제된_df = 정제(pd.read_csv(csv_path))
    print(sorted(정제된_df["반"].unique()))
    print(sorted(정제된_df["과목"].unique()))

    수학_df = 정제된_df[정제된_df["과목"] == "수학"]
    print(len(수학_df))

    반1_90점이상_df = 정제된_df[(정제된_df["반"] == "1반") & (정제된_df["점수"] >= 90)]
    print(len(반1_90점이상_df))

    반별_평균 = 정제된_df.groupby("반")["점수"].mean()
    print(반별_평균)

    과목_반별_평균 = 정제된_df.groupby(["과목", "반"])["점수"].mean()
    print(과목_반별_평균)

    반별평균(정제된_df)

    print(정제된_df.groupby("반")["점수"].sum().sum())
    print(정제된_df["점수"].sum())

    print(정제된_df.groupby("반")["점수"].count().sum())
    print(len(정제된_df))

    print(정제된_df[(정제된_df["반"] == "1반") & (정제된_df["과목"] == "수학")]["점수"])

