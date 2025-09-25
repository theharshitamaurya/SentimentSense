# SentimentSense

SentimentSense is a simple sentiment analysis project that classifies text as positive or negative. It uses a logistic regression model trained on movie review data and features a Streamlit frontend for easy user interaction. Ideal for beginners in natural language processing (NLP).

## Folder Structure

SentimentSense/
│
├── model_training/
│   ├── train_model.ipynb
│   └── sentiment_model.pkl
│
├── app/
│   ├── app.py
│   ├── sentiment_model.pkl
│   └── requirements.txt
│
└── README.md



## Features

- Train a sentiment analysis model using movie reviews dataset from NLTK.
- Simple logistic regression pipeline with CountVectorizer.
- Streamlit web app for real-time sentiment prediction on user input.
- Easy to extend and customize with different models or datasets.

## Getting Started

### 1. Train the Model (Optional)

- Open `model_training/train_model.ipynb` in Google Colab.
- Run all cells to train the logistic regression model.
- Download the generated `sentiment_model.pkl`.

### 2. Setup the Streamlit App

- Place the downloaded `sentiment_model.pkl` into the `app/` folder.
- Navigate to the `app/` directory in your terminal.
- Install dependencies:

pip install -r requirements.txt


- Run the app:

streamlit run app.py


### 3. Use the App

- Open the local URL displayed in your terminal (usually http://localhost:8501).
- Type a sentence or phrase in the input box.
- Click "Analyze Sentiment" to see if the sentiment is positive or negative.

## Possible Improvements

- Replace the model with a more advanced transformer-based sentiment model for better accuracy on short sentences.
- Enhance UI with detailed sentiment scores or confidence values.
- Add support for multilingual text.


---

Enjoy using SentimentSense! Feel free to contribute or customize for your needs.
