import config
import pickle
import json
import numpy as np
import pandas as pd

class Diabetes:

    def __init__(self, user_data):

        self.Model_File_Path = "model_diabetes.pkl"
        self.user_data = user_data
        


    def load_saved_data(self):

        with open (self.Model_File_Path, "rb") as f:
            self.model = pickle.load(f)

        # with open ("project_data.json", 'r') as f:
        #     self.project_data = json.load(f)

        #print(self.log_clf_model) 


    
    def get_predicted_outcome(self):

        self.load_saved_data()

        Glucose = eval(self.user_data['Glucose'])
        BloodPressure = eval(self.user_data['BloodPressure'])
        print("BP",BloodPressure)
        SkinThickness = eval(self.user_data['SkinThickness'])
        Insulin = eval(self.user_data['Insulin'])
        BMI = eval(self.user_data['BMI'])
        DiabetesPedigreeFunction = eval(self.user_data['DiabetesPedigreeFunction'])
        Age = eval(self.user_data['Age'])

        test_array = np.array([Glucose, BloodPressure, SkinThickness, Insulin, BMI,
                            DiabetesPedigreeFunction, Age], ndmin = 2)
        print(test_array)

        predicted_class = self.model.predict(test_array)[0]
        
        print("Predicted Class : ", predicted_class)

        return predicted_class



if __name__ == "__main__":



    dbs = Diabetes()


