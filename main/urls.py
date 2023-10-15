from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.homepage, name = "homepage"),
    path("robotaxi/", views.proj4, name = "proj4"),
    path("birdrobot/", views.proj3, name = "proj3"),
    path("cartoonify/", views.cartoonify, name = "cartoonify"),
    path("nlptext/", views.nlptext, name = "nlptext"),
    path("nfl_ml/", views.nfl_ml, name = "nfl_ml"),
    path("nlptext/preprocessing/", views.preprocessing, name = "preprocessing"),
    path("nlptext/annotation/", views.annotation, name = "annotation"),
    path("nlptext/analysis/", views.analysis, name = "analysis"),
    path("nlptext/train/", views.train, name = "train"),
    path("anytime/", views.anytime, name = "anytime"),
    path("resume/", views.resume, name = "resume"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
