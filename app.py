from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract input values from form
        tv = float(request.form['tv'])
        radio = float(request.form['radio'])
        newspaper = float(request.form['newspaper'])

        # Apply the regression formula
        prediction = 2.7452 + 0.0476 * tv + 0.1847 * radio + 0.0038 * newspaper

        return render_template('index.html', prediction_text=f'Predicted Sales: {prediction:.2f}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)
