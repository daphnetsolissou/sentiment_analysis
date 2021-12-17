# Sentiment Task

This is a project that performs Emotion Detection on news articles downloaded from the https://newsapi.org API using two
different methods. 

The available methods are a Multinomial Naive Bayes model and a Deep Neural Network model trained on an emotion dataset.


# Install Requirements
The project is built using a clean venv of Python 3.9.0.

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

1) The news API restricted me from downloading more than one pages containing 100 results for a request. This is why
the pagination option is available but by default deactivated.

2) Also because of the free plan I was not able to download articles past a month before my subscription. This is why the 
year restriction for 2021 is limited to December 2021. For paid plan thought past year can be accessed.

3) Since the downloaded data are limited to 100 each time they can fit in memory. This is why they are kept in memory as a
dataframe and not stored in a database.
   
# Emotion Dataset 

The models were trained using an emotion dataset of 20000 English Twitter messages which can be found on 
https://www.kaggle.com/parulpandey/emotion-dataset. 

The training dataset comprises six different classes: sadness, joy, love, anger, fear and surprise.
   
# Trained models

I trained two models using the emotions dataset, a Multinomial Naive Bayes model and a Deep Neural Network. The 
Bag-of-Words features extraction technique was used for the training of both models.

The Multinomial NB model achieved train accuracy = 0.87 and test accuracy = 0.7668 on the training/test sets. The 
DNN model achieved train accuracy = 0.94 and test accuracy = 0.84, using also a validation split and batch size of 1024.

More complex models using BERT, BiDirectional LSTMs could perform better on this task but they require a lot of time to 
train. If I wasn't time restricted I would attempt to try those models.