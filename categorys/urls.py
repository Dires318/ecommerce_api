from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:key>/",views.detailIn),
    path("<str:key>/", views.detail, name="detail"),

]


