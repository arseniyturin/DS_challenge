from sklearn.base import BaseEstimator

class NoTransformation(BaseEstimator):
    '''Not transformation'''
    def fit(self, X, y=0):
        return self
    def transform(self, X):
        return X
