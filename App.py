import pickle
from flask import Flask, request, render_template

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    exp = float(request.form['exp'])
    test_score = float(request.form['test'])
    interview_score = float(request.form['interview'])

    prediction = model.predict([[exp, test_score, interview_score]])
    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text=f"Predicted Salary: ${output}")

if __name__ == '__main__':
    app.run(debug=True)
