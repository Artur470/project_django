from django.urls import path
from .views import blog, createBlog, updateBlog, deleteBlog, areaView, commentView
urlpatterns = [
    path('', blog),
    path('create/', createBlog),
    path('update/<int:id>/', updateBlog),
    path('delete/<int:id>/', deleteBlog),
    path('area/', areaView),
    path('comment/<int:id>/', commentView)

]
