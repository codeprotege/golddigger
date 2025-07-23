from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

def train_model(data):
    """
    Trains a sentiment analysis model.

    Args:
        data (pandas.DataFrame): The preprocessed data with 'processed_text' and 'sentiment' columns.

    Returns:
        tuple: A tuple containing the trained model and the vectorizer.
    """
    # Create a bag-of-words model
    cv = CountVectorizer(max_features=1500)
    X = cv.fit_transform(data['processed_text']).toarray()
    y = data['sentiment']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Naive Bayes classifier
    model = MultinomialNB()
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    print(classification_report(y_test, y_pred))

    return model, cv

def predict_sentiment(text, model, vectorizer):
    """
    Predicts the sentiment of a given text.

    Args:
        text (str): The text to analyze.
        model: The trained sentiment analysis model.
        vectorizer: The fitted CountVectorizer.

    Returns:
        str: The predicted sentiment ('positive' or 'negative').
    """
    from src.data_preprocessing import preprocess_text
    processed_text = preprocess_text(text)
    vectorized_text = vectorizer.transform([processed_text]).toarray()
    prediction = model.predict(vectorized_text)
    return prediction[0]

if __name__ == '__main__':
    # This is an example of how to use the sentiment analysis module.
    # In the main script, we will import the necessary modules and run them.
    from data_collection import collect_data
    from data_preprocessing import preprocess_data
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')


    market_data = collect_data()
    preprocessed_data = preprocess_data(market_data)
    model, cv = train_model(preprocessed_data)

    # Example prediction
    new_text = "Gold is a good investment."
    sentiment = predict_sentiment(new_text, model, cv)
    print(f"The sentiment of '{new_text}' is: {sentiment}")
