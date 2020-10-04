"""
File: model.py

Trains and evaluates a logistic regression model to predict whether an article is patent
cited on the basis of a tf-idf featurization of abstract.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from tqdm import tqdm
import csv

def get_data():
    """
    Extracts data from raw files. pos_data_raw.csv and
    neg_data_raw.csv consist of three columns, an index column,
    a column indicating the publication year, and a column containing abstracts
    """
    data = []
    with open("pos_data_raw.csv", "r") as pos:
        csv_reader = csv.reader(pos)
        for row in tqdm(csv_reader):
            if 2015 >= int(row[1]) >= 1970:
                data.append((1, row[-1]))
    with open("neg_data_raw.csv", "r") as pos:
        csv_reader = csv.reader(pos)
        for row in tqdm(csv_reader):
            if 2015 >= int(row[1]) >= 1970:
                data.append((0, row[-1]))
    return data


def main():
    data = get_data()
    train, test = train_test_split(data, random_state=42)
    tfidf_text = [x[1] for x in train]
    vectorizer = TfidfVectorizer()
    x = vectorizer.fit_transform(tfidf_text)
    y_test = [x[0] for x in test]
    test_text = [x[1] for x in test]
    x_test = vectorizer.transform(test_text)
    y_test_hat = fitted.predict_proba(x_test)
    with open("tfidf_vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)
    with open("y_test.pkl", "wb") as f:
        pickle.dump(y_test, f)
    with open("y_test_hat.pkl", "wb") as f:
        pickle.dump(y_test_hat, f)

if __name__=="__main__":
    main()
