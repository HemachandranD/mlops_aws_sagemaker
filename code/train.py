from prophet import Prophet
import pandas as pd


def train():
    # Initialize and fit Prophet model
    model = Prophet()
    model.fit(df)


if __name__ == "__main__":
    # Load preprocessed data
    df = pd.read_csv('/opt/ml/processing/train/preprocessed_data.csv')
    train()
