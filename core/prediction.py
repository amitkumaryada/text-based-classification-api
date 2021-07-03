import yaml
from sklearn.external import joblib
import os
import pandas as pd
import numpy as np
from scipy.stats import randint
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
from sklearn.feature_extraction.text import  CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import chi2
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn import metrics
from sklearn.ensemble import GradientBoostingClassifier

with open(r"./configuration/config.yml") as file:
    config =yaml.load(file,Loader=yaml.FullLoader)

def get_prediction(path):
    """

    :param path: str, path of the local file in staorage
    :return:
    """

    classifier = joblib.load(config['model'])
    tfidfvectorizer = joblib.load(config['tfidf'])
    response = {}

    id_to_category = {0:'kbis',
                      1:'wolfsberg',
                      2:'coi',
                      3:'rib'}
    with open(path,'r') as f:
        test_data = f.read()
        x_tfidf = tfidfvectorizer.transform([test_data]).toarray()
        answer = classifier.predict(x_tfidf)
        response['text'] = test_data
        response['class'] = id_to_category[int(answer)]
        return response



