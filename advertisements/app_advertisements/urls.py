from django.urls import path
from .views import index, top_sellers, register,login,profile, advertisement, post

urlpatterns = [
    path('',index, name = 'main-page'),
    path('top-sellers.html/', top_sellers, name = 'top-sellers'),
    path('register.html',register, name = 'register'),
    path('login.html',login, name = 'login'),
    path('profile.html',profile, name = 'profile'),
    path('advertisement.html',advertisement, name = 'advertisement'),
    path('advertisement-post.html',post, name = 'post' )
]