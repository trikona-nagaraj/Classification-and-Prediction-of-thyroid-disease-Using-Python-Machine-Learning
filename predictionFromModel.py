import pandas
import pickle
from Logging_file.Logger import App_Logger
from PredictionRawData_Validation.predictionDataValidation import Prediction_Data_validation
from data_ingestion import data_loader_prediction
from data_preprocessing import preprocessing
from File_operations import file_methods


class prediction:

    def __init__(self,path):
        self.file_object = open("Prediction_Logs/Prediction_Log.txt", 'a+')
        self.log_writer = App_Logger()
        self.pred_data_val = Prediction_Data_validation(path)


    def predictionFromModel(self):

        self.log_writer.log(self.file_object, 'Start of Prediction')

        try:
            self.pred_data_val.deletePredictionFile() #deletes the existing prediction file from last run!

            data_getter = data_loader_prediction.Data_Getter_Pred(self.file_object,self.log_writer)
            data = data_getter.get_data()

            """Performing data preprocessing"""

            preprocessor = preprocessing.Preprocessor(self.file_object, self.log_writer)
            data = preprocessor.dropUnnecessaryColumns(data,
                                                   ['TSH_measured', 'T3_measured', 'TT4_measured', 'T4U_measured',
                                                    'FTI_measured', 'TBG_measured', 'TBG', 'TSH'])

            # replacing '?' values with np.nan as discussed in the EDA part

            data = preprocessor.replaceInvalidValuesWithNull(data)

            # get encoded values for categorical data

            data = preprocessor.encodeCategoricalValuesPrediction(data)

            # check if missing values are present in the dataset

            is_null_present = preprocessor.is_null_present(data)

            if (is_null_present):
                data = preprocessor.impute_missing_values(data)

            """ Applying the clustering approach"""

            file_loader = file_methods.File_Operation(self.file_object, self.log_writer)

            kmeans = file_loader.load_model('KMeans')

            clusters = kmeans.predict(data)  # drops the first column for cluster prediction

            data['clusters'] = clusters

            clusters = data['clusters'].unique()

            """parsing all the clusters and looking for the best ML algorithm to fit on individual cluster"""


            result = []  # initialize balnk list for storing predicitons
            with open('EncoderPickle/enc.pickle', 'rb') as file:  # let's load the encoder pickle file to decode the values
                encoder = pickle.load(file)

            for i in clusters:
                 cluster_data = data[data['clusters'] == i]
                 cluster_data = cluster_data.drop(['clusters'], axis=1)
                 model_name = file_loader.find_correct_model_file(i)
                 model = file_loader.load_model(model_name)
                 for val in (encoder.inverse_transform(model.predict(cluster_data))):
                    result.append(val)

  #               predictions = encoder.inverse_transform(model.predict(cluster_data))
   #              result = pandas.concat([cluster_data, pandas.DataFrame(predictions, columns=['Predictions'])],axis=1)
            result = pandas.DataFrame(result, columns=['Predictions'])
            result = result.reset_index(drop=True)
            path = "Prediction_Output_File/Predictions.csv"
            result.to_csv(path,header=False,index=True)
            self.log_writer.log(self.file_object, 'End of Prediction')

        except Exception as ex:
            self.log_writer.log(self.file_object, 'Error occured while running the prediction!! Error:: %s' % ex)
            raise ex

        return path
