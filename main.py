from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

#requset Get method url :"/ " 

@app.get("/")
def root(): # path operation function 
    return {"Hello": "to fast api "}

@app.get("/posts")
def get_posts():
    return {"data":"this is the first post"}

@app.post("/createposts")
def create_post(payload: dict = Body(...)):
    print(payload)
    return{"new post":f"title:{payload['title']} content{payload['content']}"}
