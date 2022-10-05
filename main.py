from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from model import predict#, convert

app = FastAPI()

# pydantic models
class StockIn(BaseModel):
    comment: str

class StockOut(StockIn):
    forecast: dict

@app.post("/predict", response_model=StockOut, status_code=200)
def get_prediction(payload: StockIn):
    comment = payload.comment
    prediction_list = predict(comment)
    

    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {
        "comment": comment,
        "forecast": prediction_list[0]
        } 


    return response_object
