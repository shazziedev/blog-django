from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
 

from cre.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeScreen.as_view(template_name='home.html'),name="home"),
    path('blog/',include('cre.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
