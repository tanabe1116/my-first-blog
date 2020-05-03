from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    d = {
        'objects': range(10),
    }
    posts = Post.order_by('published_date')
    # https://qiita.com/shonansurvivors/items/12b087cf5ab591273c8c
    return render(request, 'blog/post_list.html', d)
