from fastapi import FastAPI

app = FastAPI()

@app.get("/welcome")
def welcome():
    return{
        "Message":"How are you Yousef"
    }
