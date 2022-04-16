from ninja import NinjaAPI
from django.http import HttpRequest
from django.shortcuts import get_object_or_404

from posts.models import Post 
from posts.schemas import PostInputSchema, PostOutputSchema

from typing import List



api = NinjaAPI()

@api.get('post/', response=List[PostOutputSchema])
def get_all_posts(request):
    queryset = Post.objects.all()
    return queryset

@api.post('post/', response={201:PostOutputSchema})
def create_a_post(request, context:PostInputSchema):
    new_post = Post.objects.create(**context.dict())       # ** means your passing a dictionary
    return 201, new_post

@api.get('post/{post_id}/', response={200:PostOutputSchema})
def get_post(request, post_id:int):
    post = get_object_or_404(Post, pk=post_id)
    return post
    # return 200, Post.objects.get(id=post_id)


@api.put('post/update/{post_id}/', response={201:PostOutputSchema})
def update_post(request, post_id:int, payload:PostInputSchema):
    post_to_update = get_object_or_404(Post, pk=post_id)
    print(post_to_update)
    post_to_update.title = payload.title
    post_to_update.content = payload.content
    post_to_update.save()
    return 201, post_to_update


@api.delete('post/delete/{post_id}/', response={204:None})
def delete_post(request, post_id:int):
    post_to_delete = get_object_or_404(Post, pk=post_id)
    post_to_delete.delete()
    return 204



##########################################
# Getting an Item using its ID


# posts = [
#     {
#         "id": 1,
#         "title": 'Title1',
#         "content": 'Content1'
#     },
#     {
#         "id": 2,
#         "title": 'Title2',
#         "content": 'Content2'
#     },
#     {
#         "id": 3,
#         "title": 'Title3',
#         "content": 'Content3'
#     }
# ]
# @api.get('posts/{post_id}')
# def getPostID(request, post_id:int):
#     for item in posts:
#         if item["id"] == post_id:
#             return {'data': item}
#     return "item not found"
###########################################

# Practice ROUTES
# create routes
# @api.get('/')
# def index(request):
#     return {"message":"Hello Django Ninja"}

# @api.get('/add')
# def add(request, x:int, y:int):
#     return {"SUM": (x+y)}

# @api.post('/post')
# def create(request, payload:PostInputSchema):
#     return payload

