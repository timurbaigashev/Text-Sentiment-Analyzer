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
  
3. Launch Flask server and go on through provided ip URL : then ---> HTML page:
```HTML
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text Sentiment Analyzer</title>
</head>

<body>
    <h1>Text Sentiment Analyzer</h1>
    <form id="analyzeForm">
        <textarea id="textInput" rows="4" cols="50" placeholder="Enter your text here..."></textarea><br>
        <input type="checkbox" id="linearSVC" name="algorithm" value="svc">
        <label for="linearSVC">LinearSVC</label><br>
        <input type="checkbox" id="randomForest" name="algorithm" value="rf">
        <label for="randomForest">RandomForest</label><br>
        <input type="checkbox" id="naiveBayes" name="algorithm" value="nb">
        <label for="naiveBayes">NaiveBayes</label><br>
        <input type="submit" value="Analyze">
    </form>
    <div id="result"></div>

    <script>
        document.getElementById('analyzeForm').addEventListener('submit', function (e) {
            e.preventDefault();

            var text = document.getElementById('textInput').value;
            var selectedAlgorithm = document.querySelector('input[name="algorithm"]:checked').value;

            var url = '/analyze_' + selectedAlgorithm;

            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: text })
            })
                .then(response => response.json())
                .then(data => {
                    document.getElementById('result').innerText = 'Sentiment: ' + data.sentiment;
                })
                .catch(error => console.error('Error:', error));
        });
    </script>
</body>

</html>
```
4.  Enter text into the provided input box and click the "Analyze" button to see the sentiment analysis result.

## Notes:

- This application is a basic implementation for educational purposes. For more accurate sentiment analysis, consider using larger datasets and more advanced machine learning models.
- Make sure to handle exceptions and edge cases appropriately for a robust application.
Feel free to customize and enhance the application as needed for your specific requirements.

Author: Timur Baigashev

## License: 
[MIT](https://choosealicense.com/licenses/mit/)
