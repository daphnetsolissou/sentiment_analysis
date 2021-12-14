import pytest
from preprocessing import Preprocessor


@pytest.fixture()
def preprocessor():
    my_text = 'Patrick Drahi is playing the long game at BT <a href="https://www.reuters.com/companies/BT.L" ' \
              'target="_blank">(BT.L)</a>. The Franco-Israeli billionaire <a href="https://investegate.co.uk/' \
              'altice-uk-s.a-r.l./rns/statement-regarding-bt-group-plc/202112140700065… LONDON, Dec 14 (Reuters ' \
              'Breakingviews) - Patrick Drahi is playing the long game at BT (BT.L). The Franco-Israeli billionaire says' \
              ' he doesnt want to buy the 17 billion pound UK telecoms group; increas… [+3710 chars]'
    return Preprocessor(my_text)


def test_clean_text(preprocessor):
    clean_text = preprocessor.clean_text()
    print(clean_text)
    assert len(clean_text) > 2


def test_remove_stopwords(preprocessor):
    words_list = preprocessor.remove_stopwords()
    print(words_list)
    assert len(words_list) > 2


def test_lemmatize_words(preprocessor):
    words_list = preprocessor.lemmatize_words()
    print(words_list)
    assert len(words_list) > 2
