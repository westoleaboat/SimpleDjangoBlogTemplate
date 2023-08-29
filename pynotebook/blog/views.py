from django.shortcuts import render, get_object_or_404
from .models import Post

from django.views.generic import ListView

# pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# tags
from taggit.models import Tag
from django.db.models import Count

from plotly.offline import plot
# from utils import get_visual
from .utils import get_visual, generate_visual
import json
from .hn_submissions import hn_articles

# Create your views here.
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 6
    template_name = 'blog/post/list.html'

def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    tag = None # optional param that has a None def val.

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    # all_tags = Post.objects.values_list('slug', flat=True)
    all_tags = Tag.objects.all()

    paginator = Paginator(object_list, 6) # 6 posts in each page
    page = request.GET.get('page')

    # Generate the Plotly figure using the loaded data
    fig2 = generate_visual()

    # plot_html = plot(get_visual(), output_type='div')
    plot_html = plot(fig2, output_type='div')
    
    submission_dicts = hn_articles()
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
        # posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'page':page, 'posts': posts, 'tag': tag, 'plot_html': plot_html, 'submission_dicts': submission_dicts, 'tags': all_tags })

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                    status='published',
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day)
    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]
    return render(request, 'blog/post/detail.html', {'post': post, 'similar_posts':similar_posts})