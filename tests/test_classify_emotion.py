import pytest
from classify_emotion import Classifier
import pandas as pd
import os

ROOT_DIR = os.path.dirname(os.getcwd())
old_dir = os.getcwd()
os.chdir(ROOT_DIR)


@pytest.fixture()
def classifier():
    dataset = pd.read_csv(os.path.join(ROOT_DIR, 'Articles.csv'), encoding='utf8')
    return Classifier(dataset, model_name='dnn')


def test_prepare_dataset(classifier):
    X = classifier.prepare_dataset()
    assert X.shape[0] == len(classifier.data)


def test_perform_predictions(classifier):
    predictions = classifier.perform_predictions()
    assert predictions.shape[0] == len(classifier.data)


def test_load_model(classifier):
    model = classifier.load_model()
    assert model is not None
