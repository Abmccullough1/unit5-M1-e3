
from django.contrib import admin
from django.urls import path
from app.views import near_hundred,string_splosion,cat_dog,lone_sum

urlpatterns = [
    path("lone_sum/<int:a>/<int:b>/<int:c>", lone_sum),
    path("catdog/<str:cd>", cat_dog),
    path("splosion/<str:word>", string_splosion),
    path("near/<int:num>/", near_hundred),
    path("admin/", admin.site.urls),
]
