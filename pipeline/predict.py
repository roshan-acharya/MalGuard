import pickle
from preprocessing.data_clean import url_to_df
import pandas as pd
from pathlib import Path
from urllib.parse import * 


BASE_DIR = Path(__file__).resolve().parent.parent

safe=pd.read_csv(BASE_DIR / 'Data/safe_links.csv')

def predict_url(url,model_path='../models/one_class_svm_model.pkl'):
    parse_url = urlparse(url)
    domain = parse_url.hostname
    scheme= parse_url.scheme
    domain_norm = domain.lower().replace("www.", "")
    combine= scheme + "://" + domain_norm

    if combine in safe['url'].values:
            return 1
    else:


        # Load the trained model
        with open(model_path, 'rb') as f:
            model = pickle.load(f)

        # Preprocess the URL
        url_df = url_to_df(url)

        # Make prediction
        prediction = model.predict(url_df)
        return prediction[0]