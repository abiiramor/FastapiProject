from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title : str
    content: str
    #optional field for our schema
    published: bool= True
    #default nan 
    rating: Optional[int] = None




#requset Get method url :"/ " 

@app.get("/")
def root(): # path operation function 
    return {"Hello": "fast api project"}

@app.get("/posts")
def get_posts():
    return {"data":"this is a post for testing"}

@app.post("/createposts")
def create_post(post:Post):
    print(post)
    print(post.dict())
    return{"data" : post}

