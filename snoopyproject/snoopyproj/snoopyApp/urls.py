from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:id>', views.post, name='post'),
    #path('post/<int:id>/createComment', views.createComment, name='createComment'),
    path('createComment/', views.createComment, name='createComment'),
    path('post/createComment/', views.createComment, name='createComment'),

]