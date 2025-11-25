import pickle
from preprocessing.data_clean import url_to_df

def predict_url(url,model_path='../models/one_class_svm_model.pkl'):
    # Load the trained model
    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    # Preprocess the URL
    url_df = url_to_df(url)

    # Make prediction
    prediction = model.predict(url_df)
    return prediction[0]