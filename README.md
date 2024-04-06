# Text-Sentiment-Analyzer
Clone the repository from git clone: https://github.com/timurbaigashev/Text-Sentiment-Analyzer.

Go to project directory: cd projects\Flask-Text$Analyzer

Install the required dependencies using the following command:

```bash
pip install Flask 
pip install scikit-learn 
pip install nltk
```

Download NLTK data by running the following Python code:
```python
import nltk
nltk.download("punkt")
nltk.download("wordnet")
nltk.download("stopwords")
```

## Usage:

1. Run the Flask application by executing the flask.py file:
```python
python Flask.py
```

2. Access the application through a web browser at http://localhost:5000.
  
3. Enter text into the provided input box and click the "Analyze" button to see the sentiment analysis result.

## Notes:

- This application is a basic implementation for educational purposes. For more accurate sentiment analysis, consider using larger datasets and more advanced machine learning models.
- Make sure to handle exceptions and edge cases appropriately for a robust application.
Feel free to customize and enhance the application as needed for your specific requirements.

Author: Timur Baigashev

## License: 
[MIT](https://choosealicense.com/licenses/mit/)
