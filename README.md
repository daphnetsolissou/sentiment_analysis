# How does the world feel?

In this project the goal is to perform Emotion Detection on news articles that are downloaded in real time. 
To do that I used the https://newsapi.org which provides a free licence for trial. 

The project consists of a http client for the data downloading part, a text preprocessor and a classifier class
for the emotion detection part. Two different classifiers were trained, a Multinomial Naive Bayes as a baseline 
and a plain Deep Neural Network.


# Install Requirements
To run this project you need a virtual environment of Python 3.9.0.

After setting up your environment you can install the required packages using the requirements.txt:
```bash
pip install -r requirements.txt
```

# Available commands
To see the project in action you can try the available commands:

```bash
python main.py topic 'christmas' # returns a report of the original sources of the articles for the specific topic
python main.py topic 'christmas' --sentiment # performs emotion detection on the articles using the DNN model
python main.py topic 'christmas' --sentiment --mnb # performs emotion detection on the articles using the Multinomial NB model
python main.py topic 'christmas' --year=2021 # a temporal restriction is also available
```

# Restrictions

1) The free licence doesn't allow pagination and returns max 100 results per request. This is why the pagination option is available but by default deactivated.

2) The free plan limits historical data search to one month before today.
   
# Emotion Dataset 

The models were trained using an emotion dataset of 20000 English Twitter messages which can be found on 
https://www.kaggle.com/parulpandey/emotion-dataset. 

The training dataset comprises six different classes: sadness, joy, love, anger, fear and surprise.
   
# Trained models

I trained two models using the above mentioned emotion dataset, a Multinomial Naive Bayes model and a Deep Neural Network. The 
Bag-of-Words features extraction technique was used for the training of both models.

The Multinomial NB model achieved train accuracy = 0.87 and test accuracy = 0.7668 on the training/test sets. The 
DNN model achieved train accuracy = 0.94 and test accuracy = 0.84, using also a validation split of 0.3 and a 
batch size of 1024.
