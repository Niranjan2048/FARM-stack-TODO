from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# app object
app=FastAPI()

origin=['https//:localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,   
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get("/")
def read_root():
    return {"Hello": "Niranjan"}
    


