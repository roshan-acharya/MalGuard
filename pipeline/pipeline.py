from preprocessing import train_model,clean_safe_data,save_data
import pandas as pd

if __name__ == "__main__":
    df=pd.read_csv('./Data/safe_links.csv')
    print("Training Model")
    train_model(df,'./models/one_class_svm_model.pkl')