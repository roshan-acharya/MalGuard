import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from pipeline.predict import predict_url
from pathlib import Path
import matplotlib.pyplot as plt
BASE_DIR = Path(__file__).resolve().parent.parent


def evaluatemodel():
    test=pd.read_csv(BASE_DIR / 'Data/test.csv')
    model_path = BASE_DIR / 'models/model.pkl'
    
    #I have benigh and phishing labels in test data
    X_test = test['url'].values
    #labels are benign and phishing
    y_true = test['type'].apply(lambda x: 1 if x == 'safe' else -1).values
    y_pred = []
    for url in X_test:
        prediction = predict_url(url, model_path)
        y_pred.append(prediction)
    print("Confusion Matrix:")
    print(confusion_matrix(y_true, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_true, y_pred))
    # Plot confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(6, 4))
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title('Confusion Matrix')
    plt.colorbar()
    #save
    plt.savefig(BASE_DIR / 'reports/confusion_matrix.png')
    plt.close()

if __name__ == "__main__":
    evaluatemodel()