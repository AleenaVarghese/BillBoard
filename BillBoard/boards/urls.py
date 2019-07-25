from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# #set namespace
app_name = 'boards'

from rest_framework import routers

router = routers.DefaultRouter()
router.register('listboards',views.listboards)#mension path in space given between''

urlpatterns = [
    path('',include(router.urls)),      
]
if settings.DEBUG:
   urlpatterns += staticfiles_urlpatterns()
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)