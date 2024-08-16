import pandas as pd


def preprocess(df):
    processed_df = df.dropna(axis=0)
    return processed_df


if __name__ == "__main__":
    base_dir = "/opt/ml/processing"

    df = pd.read_csv(f"{base_dir}/input/syntehetic_data.csv", header=None)
    processed_df = preprocess(df)
    processed_df.to_csv(f"{base_dir}/output/preprocessed_data.csv", index=False)