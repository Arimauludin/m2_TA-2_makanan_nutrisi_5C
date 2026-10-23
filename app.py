from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Memuat model nutrisi
model = joblib.load('model/model_nutrisi.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_result = None
    input_value = None
    nama_makanan = None
    
    if request.method == 'POST':
        try:
            nama_makanan = request.form.get('nama_makanan', 'Makanan')
            input_value = float(request.form['carbs'])
            
            # Prediksi Kalori
            pred_calories = model.predict(np.array([[input_value]]))[0]
            pred_calories = max(0, pred_calories)
            
            prediction_result = round(pred_calories, 2)
        except ValueError:
            prediction_result = "Error"

    return render_template('index.html', 
                           prediction=prediction_result, 
                           input_val=input_value,
                           nama=nama_makanan)

if __name__ == '__main__':
    app.run(debug=True)