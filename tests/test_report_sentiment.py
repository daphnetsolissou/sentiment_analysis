import pytest
from report_sentiment import SentimentReporter
import pandas as pd
import os

ROOT_DIR = os.path.dirname(os.getcwd())
old_dir = os.getcwd()
os.chdir(ROOT_DIR)
TEST_DATASET = pd.read_csv(os.path.join(ROOT_DIR, 'Articles.csv'), encoding='utf8')


@pytest.fixture()
def reporter():
    return SentimentReporter(TEST_DATASET, model_name='dnn')


def test_add_predictions(reporter):
    new_df = reporter.add_predictions()
    new_columns = new_df.columns
    assert 'predictions' in new_columns


def test_calculate_percentage_per_emotion(reporter):
    new_df = reporter.add_predictions()
    report_dict = reporter.calculate_percentage_per_emotion(new_df)
    assert isinstance(report_dict, dict) is True


def test_get_report_string(reporter):
    report_string = reporter.get_report_string()
    assert len(report_string) > 0
