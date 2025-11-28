import pickle 
import pandas as pd

with open('/home/manav-bassi/Desktop/insurance premium project/model/model.pkl','rb') as f:
    model = pickle.load(f)

#this can be done using mlflow ,i am taking this as example 
MODEL_VERSION = '1.0.0'

class_labels = model.classes_.tolist()

def predict_output(user_input : dict):

    df = pd.DataFrame([user_input])

    predicted_class = model.predict(df)[0]

    probabilities = model.predict_proba(df)[0]

    confidence = max(probabilities)
    #mapping
    class_probs = dict(zip(class_labels,map(lambda x: round(x,4), probabilities)))

    return {
        'predicted_category' : predicted_class,
        'confidence': confidence,
        'class_probabilites': class_probs
    }

