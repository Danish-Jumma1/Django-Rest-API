from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("view/",views.ListTodoAPIView.as_view(),name="product_list"),
]