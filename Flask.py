from flask import Flask, request, jsonify, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re
import csv
import os

app = Flask(__name__, template_folder="templates_folder")


class TextSentimentAnalyzer:
    def __init__(self, classifier):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words("english"))
        self.vectorizer = TfidfVectorizer(
            sublinear_tf=True,
            encoding="utf-8",
            decode_error="ignore",
            stop_words="english",
        )
        self.classifier = classifier

    def preprocess_text(self, text):
        text = re.sub(r"\W", " ", text.lower())
        tokens = word_tokenize(text)
        tokens = [
            self.lemmatizer.lemmatize(word)
            for word in tokens
            if word not in self.stop_words
        ]
        return " ".join(tokens)

    def train(self, X_train, y_train):
        X_train_preprocessed = [self.preprocess_text(text) for text in X_train]
        X_train_vectorized = self.vectorizer.fit_transform(X_train_preprocessed)
        self.classifier.fit(X_train_vectorized, y_train)

    def predict(self, X):
        X_preprocessed = [self.preprocess_text(text) for text in X]
        X_vectorized = self.vectorizer.transform(X_preprocessed)
        return self.classifier.predict(X_vectorized)


class LinearSVCAnalyzer(TextSentimentAnalyzer):
    def __init__(self):
        classifier = LinearSVC()
        super().__init__(classifier)


class RandomForestAnalyzer(TextSentimentAnalyzer):
    def __init__(self):
        classifier = RandomForestClassifier()
        super().__init__(classifier)


class NaiveBayesAnalyzer(TextSentimentAnalyzer):
    def __init__(self):
        classifier = MultinomialNB()
        super().__init__(classifier)


analyzer_svc = LinearSVCAnalyzer()
analyzer_rf = RandomForestAnalyzer()
analyzer_nb = NaiveBayesAnalyzer()


@app.route("/")
def index():
    return render_template("Test.html")


@app.route("/analyze_svc", methods=["POST"])
def analyze_text_sentiment_svc():
    data = request.json
    text = data["text"]

    prediction = analyzer_svc.predict([text])

    return jsonify({"sentiment": prediction[0]})


@app.route("/analyze_rf", methods=["POST"])
def analyze_text_sentiment_rf():
    data = request.json
    text = data["text"]

    prediction = analyzer_rf.predict([text])

    return jsonify({"sentiment": prediction[0]})


@app.route("/analyze_nb", methods=["POST"])
def analyze_text_sentiment_nb():
    data = request.json
    text = data["text"]

    prediction = analyzer_nb.predict([text])

    return jsonify({"sentiment": prediction[0]})


if __name__ == "__main__":

    directory_path = r"C:\Users\gamer\OneDrive\Рабочий стол\VSCODE\Python\lab1\classtask\projects\Flask - Text Analyzer"

    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    file_path = os.path.join(directory_path, "sentiment_data_extended.csv")

    texts = []
    sentiments = []

    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            texts.append(row["text"])
            sentiments.append(row["sentiment"])

    analyzers = [analyzer_svc, analyzer_rf, analyzer_nb]
    for analyzer, label in zip(analyzers, sentiments):
        analyzer.train(texts, sentiments)

    app.run(debug=True)
