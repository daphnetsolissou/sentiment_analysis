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

    def get_report_string(self):
        df_with_predictions = self.add_predictions()
        if df_with_predictions is None:
            return ''

        emotions_dict = self.calculate_percentage_per_emotion(df_with_predictions)
        if emotions_dict is None:
            return ''

        report_string = '\n'
        for key, value in emotions_dict.items():
            report_string = report_string + f'{key} {value}\n'
        return report_string

    def add_predictions(self):
        classifier = Classifier(self.df.copy(), model_name=self.model_name)
        predictions = classifier.perform_predictions()
        if predictions is None:
            print("Could not predict emotions on the input dataset.\n")
            return
        new_df = self.df.copy()
        new_df['predictions'] = predictions
        new_df['predictions'] = new_df['predictions'].apply(lambda x: int_to_label[x])
        return new_df

    @staticmethod
    def calculate_percentage_per_emotion(df):
        try:
            count_emotions = df['predictions'].value_counts()
        except KeyError:
            print('No predictions column found\n')
            return
        emotions_dict = {}
        for index, value in count_emotions.items():
            emotion_percentage = (value * 100) / len(df)
            emotions_dict[f'{emotion_percentage} %'] = index
        return emotions_dict

