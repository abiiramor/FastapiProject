from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title : str
    content: str
    #optional field for our schema
    published: bool= True
    #default nan 
    rating: Optional[int] = None

#create variable to save postsme into array
my_posts = [{"title":"title of post 1", "content":"content of post 1", "id":1},
{"title":"favorite drink", "content":"coffee", "id":3}]
def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


            
#requset Get method url :"/ " 

@app.get("/")
def root(): # path operation function 
    return {"Hello abir ": "fast api project"}

@app.get("/posts")
def get_posts():
    return {"data":my_posts }

@app.post("/posts")
def create_post(post:Post):
    post_dict =post.dict()
    post_dict['id']= randrange(0 , 100000)
    my_posts.append(post_dict)
    return{"data" : post_dict}

#retrive one 
@app.get("/posts/{id}")
 # id : int is validation to put int id 
def get_post(id: int):
    #any time we have path parameter  always is return in str type
    post= find_post(int(id))
    print(post)
    return{"post details": post}
