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
    BlogPost("I love onion", "Humble yet bold, the onion is flavor’s quiet architect. Raw slices add bite; slow sweats melt into sweetness; roasting coaxes caramel depths. Reds brighten salads, yellows anchor soups and sauces, sweets sing on the grill. Cheap, storable, and rich in prebiotic fiber and quercetin, onions deserve a permanent pantry spot. Pro tip: leave the root intact until the end to tame tears. With time and heat, this layered bulb turns simple food into comfort. Peel back a layer, and dinner possibilities multiply.", 1),
    BlogPost("My Second Blog Post", "This is my second blog post", 2),
    BlogPost("My Third Blog Post", "This is my third blog post", 3),
    BlogPost("My Fourth Blog Post", "This is my fourth blog post", 4),
]

# Create your views here.
def post_listing(request):
    return render(request, "blog/blog_listing.html", {"posts": posts})

def post_details(request, id:int,  slug: str):
    displayed_post = None
    for post in posts:
        if post.id == id and post.slug == slug:
            displayed_post = post
            break
    return render(request, "blog/blog_details.html", {"post": displayed_post})