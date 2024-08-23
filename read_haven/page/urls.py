from django.urls import path
from .views import CategoryListView

app_name = "page"

urlpatterns = [
    path('', CategoryListView.as_view(), name="home"),
]