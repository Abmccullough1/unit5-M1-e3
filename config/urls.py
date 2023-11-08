
from django.contrib import admin
from django.urls import path
from app.views import near_hundred,string_splosion,cat_dog,lone_sum

urlpatterns = [
    path("Logic 2/ lone-sum/<int:a>/<int:b>/<int:c>", lone_sum),
    path("String 2/ cat-dog/<str:cd>", cat_dog),
    path("Warmup 2/ String-Splosion/<str:word>", string_splosion),
    path("Warmup 1/ near-hundred/<int:num>/", near_hundred),
    path("admin/", admin.site.urls),
]
