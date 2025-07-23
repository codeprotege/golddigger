from src.data_collection import collect_data
from src.data_preprocessing import preprocess_data
from src.sentiment_analysis import train_model, predict_sentiment
import nltk

def main():
    """
    Main function to run the market sentiment analysis system.
    """
    # Download NLTK data (if not already downloaded)
    # Download NLTK data (if not already downloaded)
    import nltk
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords')
    try:
        nltk.data.find('tokenizers/punkt_tab')
    except LookupError:
        nltk.download('punkt_tab')


    # 1. Collect data
    print("Collecting data...")
    market_data = collect_data()
    print("Data collection complete.")

    # 2. Preprocess data
    print("Preprocessing data...")
    preprocessed_data = preprocess_data(market_data)
    print("Data preprocessing complete.")

    # 3. Train the sentiment analysis model
    print("Training the model...")
    model, cv = train_model(preprocessed_data)
    print("Model training complete.")

    # 4. Predict sentiment of a new text
    new_text = "The future of gold is bright."
    sentiment = predict_sentiment(new_text, model, cv)
    print(f"The predicted sentiment of '{new_text}' is: {sentiment}")

if __name__ == '__main__':
    main()
