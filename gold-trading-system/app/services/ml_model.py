from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class MLModel:
    def __init__(self, data):
        self.data = data
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)

    def prepare_data(self):
        self.data['price_change'] = self.data['Close'].diff()
        self.data['target'] = (self.data['price_change'] > 0).astype(int)
        self.data = self.data.dropna()

        features = ['Open', 'High', 'Low', 'Close', 'Volume']
        target = 'target'

        X = self.data[features]
        y = self.data[target]

        return train_test_split(X, y, test_size=0.2, random_state=42)

    def train_model(self):
        X_train, X_test, y_train, y_test = self.prepare_data()
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        return accuracy_score(y_test, y_pred)

    def predict(self, data):
        return self.model.predict(data)
