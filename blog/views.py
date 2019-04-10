# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Post, Tag, Category

# Create your views here.
def post_list(request, category_id=None, tag_id=None):
    tag = None
    category = None

    if tag_id:
        post_list, tag = Post.get_by_tag(tag_id)
    elif category_id:
        post_list, category = Post.get_by_category(category_id)
    else:
        post_list = Post.objects.filter(status=Post.STATUS_NORMAL).select_related('owner', 'category')

    context = {
        'category': category,
        'tag': tag,
        'post_list': post_list,
    }
    context.update(Category.get_navs())

    return render(request, 'blog/list.html', context=context)


def post_detail(request, post_id=None):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None

    context = {
        'post': post
    }
    context.update(Category.get_navs())

    return render(request, 'blog/detail.html', context={'post': 'post'})