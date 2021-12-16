from classify_emotion import Classifier

int_to_label = {0: "sadness",
                1: "joy",
                2: "love",
                3: "anger",
                4: "fear",
                5: "surprise"
                }


class SentimentReporter:
    def __init__(self, articles_df, model_name='bayes'):
        self.df = articles_df
        self.model_name = model_name

    def add_predictions(self):
        classifier = Classifier(self.df.copy(), model=self.model_name)
        predictions = classifier.perform_predictions()
        self.df['predictions'] = predictions
        self.df['predictions'] = self.df['predictions'].apply(lambda x: int_to_label[x])

    def percentage_per_emotion(self):
        count_emotions = self.df['predictions'].value_counts()
        emotions_dict = {}
        for index, value in count_emotions.items():
            emotion_percentage = (value * 100) / len(self.df)
            emotions_dict[f'{emotion_percentage} %'] = index
        return emotions_dict

    def get_report_string(self):
        self.add_predictions()
        emotions_dict = self.percentage_per_emotion()
        report_string = '\n'
        for key, value in emotions_dict.items():
            report_string = report_string + f'{key} {value}\n'
        return report_string