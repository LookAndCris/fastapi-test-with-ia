from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Blog Test with Pydantic Models")

class BlogPost(BaseModel):
    id: int
    title: str
    content: str

class BlogPostCreate(BaseModel):
    title: str
    content: str

class BlogPostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

blog_posts: List[BlogPost] = []
@app.post("/posts/", response_model=BlogPost)
def create_post(post: BlogPostCreate):
    new_post = BlogPost(id=len(blog_posts) + 1, **post.dict())
    blog_posts.append(new_post)
    return new_post

@app.get("/posts/", response_model=List[BlogPost])
def read_posts(skip: int = 0, limit: int = Query(default=10, le=100)):
    return blog_posts[skip : skip + limit]

@app.get("/posts/{post_id}", response_model=BlogPost)
def read_post(post_id: int):
    for post in blog_posts:
        if post.id == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")

@app.put("/posts/{post_id}", response_model=BlogPost)
def update_post(post_id: int, post: BlogPostUpdate):
    for index, existing_post in enumerate(blog_posts):
        if existing_post.id == post_id:
            updated_data = post.dict(exclude_unset=True)
            updated_post = existing_post.copy(update=updated_data)
            blog_posts[index] = updated_post
            return updated_post
    raise HTTPException(status_code=404, detail="Post not found")


@app.delete("/posts/{post_id}", response_model=BlogPost)
def delete_post(post_id: int):
    for index, post in enumerate(blog_posts):
        if post.id == post_id:
            deleted_post = blog_posts.pop(index)
            return deleted_post
    raise HTTPException(status_code=404, detail="Post not found")


