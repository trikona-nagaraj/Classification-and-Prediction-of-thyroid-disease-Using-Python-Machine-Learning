
from flask import Flask, request, render_template, jsonify, url_for
from flask import Response
import os
from flask_cors import CORS, cross_origin
from Training_data_validation_Insertion import train_validation
from training_model import trainModel
from prediction_validation_insertion import pred_validation
from predictionFromModel import prediction

 # Setting LANG and LC_ALL environment variables for the
 # current Python Script to 'en_US.UTF-8' means that the language will be English

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)                    # Creating a flask web application object

CORS(app)

@app.route('/', methods=['GET', 'POST'])
                # TO render web Homepage
@cross_origin()
                # Allows cross-origin resource sharing (CORS)
                # for routes in the Flask application.

def home_page():
    return render_template('index.html')


                    # TO Get into the training function

@app.route("/train", methods=['POST'])
@cross_origin()


                    # Creating a function to operate the methods
                    # and functions we want to execute

def trainRouteClient():

    try:
        if request.json['folderPath'] is not None:
            path = request.json['folderPath']

            # object initialization
            train_valObj = train_validation(path)

            # Calling the training_validation function
            train_valObj.train_validation()

            # Object initialization
            trainModelObj = trainModel()

            # Training the model for the files in the table
            trainModelObj.trainingModel()

    except ValueError:
        return Response("Error Occurred! %s" % ValueError)
    except KeyError:
        return Response("Error Occurred! %s" % KeyError)
    except Exception as e:
        return Response("Error Occurred! %s" % e)
    return Response("Training successfull!!")


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRouteClient():

    try:
        if request.json['folderPath'] is not None:

            path = request.json['folderPath']

            # object initialization
            pred_val = pred_validation(path)

            # calling the prediction_validation function
            pred_val.prediction_validation()

            # object initialization
            pred = prediction(path)

            # predicting for dataset present in database
            path = pred.predictionFromModel()

            return Response("Prediction File created at %s!!!" % path)


    except ValueError:
        return Response("Error Occurred! %s" % ValueError)
    except KeyError:
        return Response("Error Occurred! %s" % KeyError)
    except Exception as e:
        return Response("Error Occurred! %s" % e)



if __name__ == "__main__":
    app.run()

