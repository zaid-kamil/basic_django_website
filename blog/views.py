from django.shortcuts import render

def blog_list(request):
    # load all blog articles from database
    return render(request, 'blog/list.html', {})