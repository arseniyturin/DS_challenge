from flask import Flask, request
import predict_model

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def predict():

    if request.method == 'POST':
        y = predict_model.predict(request.json)[0]
        return str(y)

    if request.method == 'GET':
        return 'Hello\n'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1200)
