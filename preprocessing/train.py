import pandas as pd
import numpy as np
#isolation forest
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split


columns=[ 'domain_length', 'count_dots', 'count_dashes', 'count_at_symbol',
       'count_digits', 'subdomain_count', 'query_length', 'num_params', 'num_slashes',
       'entropy']

process=ColumnTransformer(
    transformers=[
        ('scaler', StandardScaler(), columns)
    ], remainder='passthrough'
)

def train_test_split_data(df, test_size=0.2, random_state=42):
    X_train, X_test = train_test_split(df, test_size=test_size, random_state=random_state)
    return X_train, X_test


def train_model(df,path):
    forest=IsolationForest(
    n_estimators=200,       
    max_samples=256,         
    contamination=0.03,      
    max_features=0.9,       
    bootstrap=False,         
    random_state=42,
    n_jobs=-1
)
    X_train, X_test = train_test_split_data(df, test_size=0.2, random_state=42)




    pipeline = Pipeline(steps=[
       
        ('preprocessing', process),
        ('classifier', forest)
    ])

    pipeline.fit(X_train)

    #save model
    import pickle
    with open(path, 'wb') as f:
        pickle.dump(pipeline, f)
    print("Model saved to ../Models/model.pkl")





