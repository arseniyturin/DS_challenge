# DS Challenge for Monitaur

## Notes
- Model was trained on a basic Random Forest classifier, no evaluation and no features selection  has been done
- Pipeline transformed categorical features with one-hot encoding, numerical features are used as is (i.e. no scaling, since it doesn't affect classifier performance)

## Installation and Use

### 1. Create Environment
- `$ python -m venv flask_app`
- `$ source flask_app/bin/activate`
- `$ python -m pip install -r requirements.txt`

### 2. Train Random Forest Classifier
- `$ python train_model.py`

### 3. Run REST API with Flask
Few optios to play around. Due to the class imbalance the model predicts class **0** very well, but a bit worse on the less frequent classes (**1**, .., **4**). First example will correctly predict class **0**, second will correctly predict class **2**

- `$ python app.py # starts on http://localhost:1200`
- `$ curl -H 'Content-Type: application/json' -d '{"SexInsured": "U", "VehicleType": "T", "PC": 0,  "Exp_weights": 0.668035592, "NCD": 30, "AgeCat": 0, "AutoAge0": 0, "AutoAge1": 0, "AutoAge2": 0, "AutoAge": 0, "VAgeCat": 0, "VAgecat1": 2}' http://localhost:1200`
- `$ curl -H 'Content-Type: application/json' -d '{"SexInsured": "U", "VehicleType": "G", "PC": 0,  "Exp_weights": 0.394250513, "NCD": 20, "AgeCat": 0, "AutoAge0": 0, "AutoAge1": 0, "AutoAge2": 0, "AutoAge": 0, "VAgeCat": 0, "VAgecat1": 2}' http://localhost:1200`