from transformers import pipeline

def get_sentiment(text):
    """
    Uses a pre-trained NLP model to get the sentiment of a text.
    """
    sentiment_pipeline = pipeline("sentiment-analysis")
    result = sentiment_pipeline(text)
    return result[0]

def get_model_bias(text):
    """
    Uses a pre-trained NLP model to get the model bias from a text.
    """
    # This is a simplified example. A real implementation would be more complex.
    sentiment = get_sentiment(text)
    if sentiment['label'] == 'POSITIVE':
        return "Long-Conservative", sentiment['score']
    elif sentiment['label'] == 'NEGATIVE':
        return "Short-Volatility", sentiment['score']
    else:
        return "Neutral", sentiment['score']
