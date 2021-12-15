import regex as re
import unidecode
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


class Preprocessor:
    def __init__(self, input_text):
        self.input_text = input_text
        self.text_cleaned = self.clean_text()
        self.tokens = self.remove_stopwords()
        self.result_words = self.lemmatize_words()

    def get_preprocessed_list_words(self):
        return self.result_words

    def clean_text(self):
        temp_text = self.input_text.lower()
        # remove numbers
        temp_text = re.sub(r'\d+', ' ', temp_text)
        # replace accentuated characters
        temp_text = unidecode.unidecode(temp_text)
        temp_text = self.strip_urls(temp_text)
        temp_text = self.strip_html_tags(temp_text)
        # remove special symbols (commas, dashes etc)
        temp_text = re.sub("[^a-zA-Z0-9\s]+", ' ', temp_text)
        # remove double or more spacing
        result_text = re.sub("\s{2,}|\t", ' ', temp_text)

        return result_text

    @staticmethod
    def strip_html_tags(text):
        pattern = re.compile(r'<.*?>')
        return pattern.sub('', text)

    @staticmethod
    def strip_urls(text):
        url_regex = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
        pattern = re.compile(url_regex)
        return pattern.sub('', text)

    def remove_stopwords(self):
        nltk_stopwords = set(stopwords.words('english'))
        nltk_stopwords.add('href')
        word_tokens = word_tokenize(self.text_cleaned)
        filtered_text = [word for word in word_tokens if not word in nltk_stopwords]
        return filtered_text

    def lemmatize_words(self):
        lemmatizer = WordNetLemmatizer()
        words = [lemmatizer.lemmatize(w) for w in self.tokens]
        return words