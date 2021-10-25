"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.urls import path
from users.views import *
from posts.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', LoginView.as_view(),name='login'),
    path("logout/", LogoutView.as_view(),{'next_page': settings.LOGOUT_REDIRECT_URL}, name="logout"),
    path('register', RegisterView.as_view(),name="register"),
    path('post/',login_required(HomeView.as_view()),name='posts'),
    path('post/detail/<int:pk>', login_required(PostDetailView.as_view()),name='postDetail'),
    path('post/create', login_required(PostCreateView.as_view()),name='postCreate'),
    path('post/update/<int:pk>', login_required(PostUpdateView.as_view()),name='postUpdate'),
    path('detail/comment',login_required(post_comment),name='post_comment'),
    path('detail/comment/update_delete',login_required(post_comment_update_delete),name='update_delete_comment'),

    
    path('admin/', admin.site.urls),
]
