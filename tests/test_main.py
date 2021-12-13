from main import parse_arguments


def test_parse_arguments():
    parser = parse_arguments(['topic', 'brexit'])
    assert parser.topic == 'topic'
    assert parser.query == 'brexit'
