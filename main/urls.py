from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.homepage, name = "homepage"),
    path("robotaxi/", views.proj4, name = "proj4"),
    path("birdrobot/", views.proj3, name = "proj3")
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
