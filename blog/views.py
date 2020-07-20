from django.shortcuts import render, get_object_or_404
from .models import Project2

# Create your views here.


def all_blogs(request):
    projects = Project2.objects.order_by('-date')#timely order hbe r 2ta show krabe
    #projects = Project2.objects.all()#shob blog 1 page e show krbe
    return render(request, 'blog/all_blogs.html', {'projects': projects })

def detail(request, blog_id):
    blog = get_object_or_404(Project2, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})
