from fastapi import FastAPI
from fedexrates.rates import Rate
from pydantic import BaseModel

import json


CREDENTIALS = "TEST_DR6z1zWA0vFKnL+Znjk3FpRlLBEKGpKDg7N/yF7AShY"

app = FastAPI()

class AddressFrom(BaseModel):
    zip: str
    country: str

class AddressTo(BaseModel):
    zip: str
    country: str

class Parcel(BaseModel):
    length: float
    width: float
    height: float
    distance_unit: str
    weight: float
    mass_unit: str


class Item(BaseModel):
    address_from: AddressFrom
    address_to: AddressTo
    parcel: Parcel

    
@app.get("/")
def read_root():
    return {"Owner": "Luis Andres Garcia Contreras"}


@app.post("/rates/")
def get_rates(item: Item):
    request = item.json()
    request_json = json.loads(request)

    rate = Rate(quote_params=request_json, credentials=CREDENTIALS)
    return {"rates": rate.get_rate()}