


from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from blog import settings
# from posts.views import (main_page_view, 
#                          posts_view, 
#                          hashtags_view, 
#                          post_detail_view, 
#                          post_create_view)
from django.urls import include
from posts.views import HashtagViewSet, PostViewSet
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions




router = routers.DefaultRouter()
router.register(r'hashtags', HashtagViewSet)
router.register(r'posts', PostViewSet)




schema_view = get_schema_view(
    openapi.Info(
        title="Ваше API",
        default_version='v1',
        description="Документация API",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('posts.urls')),

    # URL-адреса для Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='swagger-json'),

    # URL-адреса для ReDoc
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-ui'),
]






# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', main_page_view),
#     path('posts/',posts_view),
#     path('hashtag/',hashtags_view),
#     path('posts/<int:pk>/', post_detail_view),
#     path('posts/create/',post_create_view)
# ]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



