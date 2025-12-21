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
from preprocessing.data_clean import url_to_df

from sklearn.model_selection import cross_val_score
vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(3,5))

def train_test_split_data(df, test_size=0.2, random_state=42):
    X_train, X_test = train_test_split(df, test_size=test_size, random_state=random_state)
    return X_train, X_test


def train_model(df,path):
    svm=OneClassSVM(nu=0.1, kernel='rbf', gamma='scale')
    X_train, X_test = train_test_split_data(df, test_size=0.2, random_state=42)


    pipeline = Pipeline(steps=[
       
        ('classifier', svm)
    ])

    pipeline.fit(X_train)

    #save model
    import pickle
    with open(path, 'wb') as f:
        pickle.dump(pipeline, f)
    print("Model saved to ../Models/one_class_svm_model.pkl")





