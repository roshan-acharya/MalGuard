from preprocessing import train_model, clean_safe_data, save_data
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def main():
    # df=clean_safe_data(BASE_DIR / 'Data/safe_link.csv')
    # save_data(df,BASE_DIR / 'Data/clean_safe_links.csv')

    df = pd.read_csv(BASE_DIR / 'Data/clean_safe_links.csv')
    print("Training Model")
    train_model(df, BASE_DIR / 'models/one_class_svm_model.pkl')
    print("Training Completed")


