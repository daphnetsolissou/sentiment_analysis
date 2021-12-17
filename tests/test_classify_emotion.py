import pytest
from classify_emotion import Classifier
import pandas as pd
import os

ROOT_DIR = os.path.dirname(os.getcwd())
old_dir = os.getcwd()
os.chdir(ROOT_DIR)
TEST_DATASET = pd.read_csv(os.path.join(ROOT_DIR, 'Articles.csv'), encoding='utf8')


@pytest.fixture()
def classifier():
    return Classifier(TEST_DATASET, model_name='dnn')


def test_prepare_dataset(classifier):
    X = classifier.prepare_dataset()
    assert X.shape[0] == len(TEST_DATASET)


def test_perform_predictions(classifier):
    predictions = classifier.perform_predictions()
    assert predictions.shape[0] == len(TEST_DATASET)


def test_load_model(classifier):
    model = classifier.load_model()
    assert model is not None


def test_create_corpus_from_text_columns(classifier):
    corpus = classifier.create_corpus_from_text_columns()
    assert len(corpus) == len(TEST_DATASET)
