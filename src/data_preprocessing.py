import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

def preprocess_text(text):
    """
    Preprocesses a single text document.

    Args:
        text (str): The text to preprocess.

    Returns:
        str: The preprocessed text.
    """
    # Remove non-alphabetic characters and convert to lowercase
    text = re.sub('[^a-zA-Z]', ' ', text).lower()

    # Tokenize the text
    words = word_tokenize(text)

    # Remove stopwords and perform stemming
    ps = PorterStemmer()
    words = [ps.stem(word) for word in words if not word in set(stopwords.words('english'))]

    return ' '.join(words)

def preprocess_data(data):
    """
    Preprocesses the entire dataset.

    Args:
        data (pandas.DataFrame): The input data with a 'text' column.

    Returns:
        pandas.DataFrame: The preprocessed data with a 'processed_text' column.
    """
    data['processed_text'] = data['text'].apply(preprocess_text)
    return data

if __name__ == '__main__':
    # This is an example of how to use the preprocessing module.
    # In the main script, we will import the necessary modules and run them.
    from data_collection import collect_data

    # Download NLTK data (if not already downloaded)
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')

    market_data = collect_data()
    preprocessed_data = preprocess_data(market_data)
    print(preprocessed_data)
