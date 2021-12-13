import pytest
import pandas as pd

from main import parse_arguments


@pytest.fixture()
def argsparser():
    return parse_arguments(['topic', 'brexit'])


def test_parse_arguments(argsparser):
    # parser = parse_arguments(['topic', 'brexit'])
    assert argsparser.topic == 'topic'
    assert argsparser.query == 'brexit'


