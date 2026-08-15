from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def hello():
    return {'message':'helloooo'}

@app.get('/about')
def about():
    return {'message':'Great to see you'}