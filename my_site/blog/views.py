from django.shortcuts import render
from dataclasses import dataclass

@dataclass
class BlogPost:
    title: str
    content: str
    id: int
    slug: str
    def __init__(self, title, content, id):
        self.title = title
        self.content = content
        self.id = id
        self.slug = title.lower().replace(" ", "-")


posts: list[BlogPost] = [
    BlogPost("Hello World", "This is my first blog post", 1),
    BlogPost("My Second Blog Post", "This is my second blog post", 2),
    BlogPost("My Third Blog Post", "This is my third blog post", 3),
    BlogPost("My Fourth Blog Post", "This is my fourth blog post", 4),
]

# Create your views here.
def index(request):
    return render(request, "blog/index.html", {"posts": posts})

def post(request, id:int,  slug: str):
    displayed_post = None
    for post in posts:
        if post.id == id and post.slug == slug:
            displayed_post = post
            break
    return render(request, "blog/article.html", {"post": displayed_post})