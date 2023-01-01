from django.urls import path
from .views import index, add_blog, increment_likes, delete_blog


urlpatterns = [
    path('', index, name='index'),
    path('add_blog/', add_blog, name='add_blog'),
    path('increment_likes/', increment_likes, name='increment_likes'),
    path('delete_blog/', delete_blog, name='delete_blog'),
]
