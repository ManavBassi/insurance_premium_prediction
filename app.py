from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from schema.Prediction_response import Predicition
from model.predict import predict_output ,model, MODEL_VERSION

app = FastAPI()

@app.get('/')
def home():
    return{'message':'Insurance Premium Prediction API'}

@app.get('/health')
def health_check():
    return {
        'status': 'ok',
        'version':MODEL_VERSION,
        'model_loaded': model is not None

    }
@app.post('/predict',response_model = Predicition)
def predict_premium(data: UserInput):

    user_input = {
        'income_lpa': data.income_lpa,
        'bmi': data.bmi,
        'age_group': data.age_group,
        'occupation': data.occupation,
        'city_tier': data.city_tier,
        'lifestyle_risk': data.lifestyle_risk
    
        
    }
    try:
        prediction = predict_output(user_input)

        return JSONResponse(status_code=200,content={'response': prediction})

    except Exception as e:
        return JSONResponse(status_code=500,content= str(e))