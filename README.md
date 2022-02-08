# How does the world feel?

This is a project that performs Emotion Detection on news articles. The https://newsapi.org API is used as a data source and the emotion detection is performed using two models. A Multinomial Naive Bayes model and a Deep Neural Network model were trained on an emotion training dataset.


# Install Requirements
A clean venv of Python 3.9.0 is recommended.

Begin by installing the required packages with the command:
```bash
pip install -r requirements.txt
```

# Available commands

```bash
python main.py topic 'christmas' # it returns a report of the sources containing article of the selected topic
python main.py topic 'christmas' --sentiment # performs emotion detection on the articles using the DNN model
python main.py topic 'christmas' --sentiment --methodA # performs emotion detection on the articles using the DNN model
python main.py topic 'christmas' --sentiment --methodB # performs emotion detection on the articles using the Multinomial NB model
python main.py topic 'christmas' --year=2021 # a temporal restriction is also available
```

# Restrictions

1) The news API free api key allowd requests of the first page only with 100 results. This is why the pagination option is available but by default deactivated.

2) The free plan limits historical data search to one month before today.
   
# Emotion Dataset 

The models were trained using an emotion dataset of 20000 English Twitter messages which can be found on 
https://www.kaggle.com/parulpandey/emotion-dataset. 

The training dataset comprises six different classes: sadness, joy, love, anger, fear and surprise.
   
# Trained models

I trained two models using the emotions dataset, a Multinomial Naive Bayes model and a Deep Neural Network. The 
Bag-of-Words features extraction technique was used for the training of both models.

The Multinomial NB model achieved train accuracy = 0.87 and test accuracy = 0.7668 on the training/test sets. The 
DNN model achieved train accuracy = 0.94 and test accuracy = 0.84, using also a validation split of 0.3 and a 
batch size of 1024.
