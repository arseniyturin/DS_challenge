import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from custom_pipe import NoTransformation

# Load dataset
df = pd.read_csv('data/SingaporeAuto.csv')
X = df.drop('Clm_Count', axis=1)
y = df['Clm_Count']

def save_model(obj, filename):
    with open(filename, 'wb') as file:
        pickle.dump(obj, file)

def build_pipeline(Classifier):

    # Features to be included in the pipeline
    categorical_features = ("SexInsured", "VehicleType", "PC", "AgeCat", "VAgeCat")
    numerical_features = ('Exp_weights', 'NCD', 'AgeCat', 'AutoAge0',
                          'AutoAge1', 'AutoAge2', 'AutoAge', 'VAgeCat', 'VAgecat1')

    # Features transformation
    preprocessor = ColumnTransformer(transformers = [
        # Custom transformer just to pass features
        (
            "no_transformation",
            NoTransformation(),
            numerical_features
        ),
        # One-hot encoder for categorical features
        (
            "one-hot",
            OneHotEncoder(handle_unknown="ignore", drop='if_binary'),
            categorical_features
        ),
    ])

    # Building final pipeline
    pipe = Pipeline([
        ("preprocessor", preprocessor),
        ("classifier", Classifier())
    ])

    return pipe

# Using pipeline to transform/train classifier
pipe = build_pipeline(RandomForestClassifier)
pipe.fit(X, y)

# Saving
save_model(pipe, 'models/RandomForest.bin')
