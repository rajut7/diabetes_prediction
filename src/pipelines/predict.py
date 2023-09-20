import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class Predict:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','proprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)


class CustomData:
    def __init__(self,
            Pregnancies: int,
            Glucose: int,
            BloodPressure: int,
            SkinThickness: int,
            Insulin: int,
            BMI: float,
            DiabetesPedigreeFunction: float,
            Age: int):
    
        self.Pregnancies = Pregnancies
        self.glucose = Glucose
        self.BloodPressure = BloodPressure
        self.skinthickness = SkinThickness
        self.insulin = Insulin
        self.bmi = BMI
        self.diabetespedigreefunction = DiabetesPedigreeFunction
        self.age = Age
    
    def get_data_as_frame(self):
        try:
            customdata_input_dict= {
                "Pregnancies":[self.Pregnancies],
                "Glucose":[self.glucose],
                "BloodPressure":[self.BloodPressure],
                "SkinThickness":[self.skinthickness],
                "Insulin":[self.insulin],
                "BMI":[self.bmi],
                "DiabetesPedigreeFunction":[self.diabetespedigreefunction],
                "Age":[self.age]
            }

            return pd.DataFrame(customdata_input_dict)

        except Exception as e:
            raise CustomException(e,sys)
    
