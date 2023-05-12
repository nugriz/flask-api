from flask import Flask, jsonify, request
import datetime
import joblib #pip install joblib
from flask_cors import CORS, cross_origin #pip install flask_cors
#pip install sklearn
# Load the trained model


# Create a Flask app
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
model = joblib.load(open('pred_model.joblib', 'rb'))

# Create a route for the input page
# @app.route('/')
# def input_page():
#     return render_template('input.html')

# Create a route to handle the form submission
@app.route('/predict', methods=['POST','GET'])
@cross_origin()
def predict():
    param = request.get_json()
    open_price = param['open'] #4870.5923 #request.form['Open']
    high_price = param['high'] #5192.2323 #request.form['High']
    low_price = param['low'] #4304.131 #request.form['Low']
    year = datetime.date.today().year #request.form['Year']
    month = datetime.date.today().month #request.form['Month']
    day = datetime.date.today().day #request.form['Day']
    
    # Create a dataframe from the input values
    # input_df = pd.DataFrame({'Open': [open_price], 'High': [high_price], 'Low': [low_price], 'Year':[year], 'Month': [month], 'Day': [day] })
    input_df = [[open_price, high_price, low_price, year, month, day]]
    
    # Use the trained model to predict the price
    predicted_price = model.predict(input_df) #[0]
    return jsonify(predicted_price=str(predicted_price[0]))
    # response.headers.add('Access-Control-Allow-Origin', '*')
    # return response
    # return jsonify(str(predicted_price[0]))
    # Render the template with the predicted price
    # return predicted_price
    # return render_template('output.html', predicted_price=predicted_price)

if __name__ == '__main__':
    #os.environ.setdefault('FLASK_ENV', 'development')
    app.run(debug=True)