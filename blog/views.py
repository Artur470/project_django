from django.shortcuts import render, redirect, HttpResponse
from .models import Blog, Area
from .forms import Formblog, UpdateBlogForm
# Create your views here.
def blog(request):
    blogs = Blog.objects.all()
    context = {
        "blogs": blogs
    }

    return render(request, 'blog.html', context)

def createBlog(request):

    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        Blog.objects.create(

            title=title,
            body=body

        )
        return redirect('http://127.0.0.1:8000/blog/')



    form = Formblog()
    context = {
        'form': form


    }


    return render(request, 'form_blog.html', context)


def updateBlog(request,id):
    blog = Blog.objects.get(pk=id)

    if request.method == 'POST':
        form = UpdateBlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/blog/')

        return HttpResponse('error',)

    form = UpdateBlogForm(instance=blog)
    context = {'form': form}
    return render(request, 'update_blog.html', context)

def deleteBlog(request, id):
    blog = Blog.objects.get(pk=id)
    blog.delete()
    return redirect('http://127.0.0.1:8000/blog/')


def areaView(request):
    areas = Area.objects.all()

    context = {

        'areas': areas


    }
    return render(request, 'area.html', context)