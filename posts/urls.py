# from django.contrib import admin
# from django.urls import path
# from django.conf.urls.static import static
# from blog import settings
# # from posts.views import (main_page_view, 
# #                          posts_view, 
# #                          hashtags_view, 
# #                          post_detail_view, 
# #                          post_create_view)
from django.urls import include, path
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'hashtags', HashtagViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]