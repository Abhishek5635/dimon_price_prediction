from flask import Flask, render_template, request, jsonify
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline
application = Flask(__name__)
app = application



@app.route('/')
def hompage():
    return render_template('index.html')

@app.route('/predict', methods = ["GET", "POST"])

def predict_datapoint():
    if request.method == "GET":
        return render_template('form.html')
    ## and if the it not a get request then it will be post request means user is giving some input
    else:
        data = CustomData(
            carat= float(request.form.get('carat')), ## the request method is giving the data in the form of string that why we are converting it into fload
            depth = float(request.form.get('depth')),
            table = float(request.form.get('table')),
            x = float(request.form.get('x')),
            y = float(request.form.get('y')),
            z = float(request.form.get('z')),
            cut = request.form.get('cut'),
            color= request.form.get('color'),
            clarity = request.form.get('clarity')
            )

        final_new_data = data.get_data_as_dataframe()
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_new_data)
       
        result =  round(pred[0],2) # this is returning the first value of a array upto 2 decimal

        return render_template('results.html', final_result = result)
    
if __name__ == "__main__":
    app.run(host= "0.0.0.0")