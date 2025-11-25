import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, KFold
from sklearn.svm import OneClassSVM
#isolation forest
from sklearn.ensemble import IsolationForest
from sklearn.cluster import DBSCAN
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from data_clean import url_to_df

from sklearn.model_selection import cross_val_score
vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(3,5))

def train_test_split_data(df, test_size=0.2, random_state=42):
    X_train, X_test = train_test_split(df, test_size=test_size, random_state=random_state)
    return X_train, X_test


def train_model(df):
    svm=OneClassSVM(nu=0.1, kernel='rbf', gamma='scale')
    X_train, X_test = train_test_split_data(df)

    preprocessor = ColumnTransformer(
        transformers=[('url', vectorizer, 'url')],
    )
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', svm)
    ])

    pipeline.fit(X_train)

    url='https://gvedshtyhn-3.pages.dev/gp/customer-reviews/R117SU381UABSD?ASIN=1433688670'
    url_df = url_to_df(url)
    prediction = pipeline.predict(url_df)
    print(f'Prediction for {url}: {prediction[0]}')  # Output: 1 for normal, -1 for anomaly

if __name__ == "__main__":
    # Example usage
    df = pd.read_csv('../Data/safe_links.csv')
    train_model(df)





