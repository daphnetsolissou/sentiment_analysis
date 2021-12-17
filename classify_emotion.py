from sklearn.feature_extraction.text import CountVectorizer
from preprocessing import Preprocessor
import pickle as pkl
import os
import tensorflow as tf
import numpy as np


class Classifier:
    def __init__(self, data, model_name='bayes'):
        self.data = data.copy()
        self.model_name = model_name
        self.models_path = os.path.join(os.getcwd(), 'models')

    def perform_predictions(self):
        input_data = self.prepare_dataset()
        model = self.load_model()
        predictions = model.predict(input_data)
        if self.model_name == 'dnn':
            predictions = np.argmax(predictions, axis=1)
            return predictions
        return predictions

    def prepare_dataset(self):
        corpus = []
        for i, row in self.data.iterrows():
            try:
                text_to_classify = ' '.join([row['title'], row['description'], row['content']])
            except (KeyError, TypeError):
                print('Error while trying to get texts from dataframe. Check your columns.\n')
                return

            preprocessor = Preprocessor(text_to_classify)
            words_list = preprocessor.get_preprocessed_list_words()
            text = ' '.join(words_list)
            corpus.append(text)

        try:
            vocab_path = os.path.join(self.models_path, 'multinomial_nb_vocabulary.pkl')
            learnt_vocabulary = pkl.load(open(vocab_path, 'rb'))
        except (FileNotFoundError, ImportError, IOError):
            print('Vectorization vocabulary could not be loaded.\n')
            return
        vectorizer = CountVectorizer(vocabulary=learnt_vocabulary)
        x = vectorizer.fit_transform(corpus)
        return x

    def load_model(self):
        try:
            if self.model_name == 'bayes':
                filename = os.path.join(self.models_path, 'multinomial_nb_model.pkl')
                loaded_model = pkl.load(open(filename, 'rb'))
            else:
                loaded_model = tf.keras.models.load_model(os.path.join(self.models_path, 'best_model_dnn_bow.h5'))
            return loaded_model
        except (FileNotFoundError, ImportError, IOError):
            print('Requested model could not be loaded.\n')
            return

