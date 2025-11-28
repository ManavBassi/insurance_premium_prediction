from pydantic import BaseModel, Field
from typing import Dict 

class Predicition(BaseModel):
    predicted_category : str  = Field(...,description = 'the insurance premium category',example = "High")

    confidence: float = Field(...,
                              description = " model's confidence score for the prediction,example = 0.8432")
    
    class_probabilties : Dict[str,float] = Field(...,description = 'Probability distribution across all possible classes'
 ,example = {"Low": 0.01, "Medium": 0.15, "High": 0.84}   )