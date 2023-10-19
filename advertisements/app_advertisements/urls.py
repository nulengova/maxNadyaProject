from django.urls import path
from .views import index, top_sellers, advertisement, post

urlpatterns = [
    path('index/', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement/', advertisement, name='advertisement'),
    path('advertisement-post/', post, name='post'),
]