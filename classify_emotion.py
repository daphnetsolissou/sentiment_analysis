from sklearn.feature_extraction.text import CountVectorizer
from preprocessing import Preprocessor
import pickle as pkl
import os
import tensorflow as tf
import numpy as np


class Classifier:
    def __init__(self, data, model='bayes'):
        self.data = data.copy()
        self.model_name = model
        self.models_path = os.path.join(os.getcwd(), 'models')

    def perform_predictions(self):
        input_data = self.prepare_dataset()
        model = self.load_model()
        predictions = model.predict(input_data)
        if self.model_name == 'dnn':
            classes = np.argmax(predictions, axis=1)
            return classes
        return predictions

    def prepare_dataset(self):
        corpus = []
        for i, row in self.data.iterrows():
            text_to_classify = ' '.join([row['title'], row['description'], row['content']])
            preprocessor = Preprocessor(text_to_classify)
            words_list = preprocessor.get_preprocessed_list_words()
            text = ' '.join(words_list)
            corpus.append(text)

        vocab_path = os.path.join(self.models_path, 'multinomial_nb_vocabulary.pkl')
        learnt_vocabulary = pkl.load(open(vocab_path, 'rb'))
        vectorizer = CountVectorizer(vocabulary=learnt_vocabulary)
        x = vectorizer.fit_transform(corpus)
        return x

    def load_model(self):
        if self.model_name == 'bayes':
            filename = os.path.join(self.models_path, 'multinomial_nb_model.pkl')
            loaded_model = pkl.load(open(filename, 'rb'))
        else:
            loaded_model = tf.keras.models.load_model(os.path.join(self.models_path, 'best_model_dnn_bow.h5'))
        return loaded_model

