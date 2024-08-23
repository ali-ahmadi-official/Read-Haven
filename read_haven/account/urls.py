from django.urls import path
from django.contrib.auth import views
from .views import (
    SignUpView, ProfileView, ProfileDetailView, OrderBookListView,CartBookListView, MyBookListView, BookCreateView, BookUpdateView, BookDeleteView,
    add_to_orders, add_to_cart
)

app_name = "account"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]

urlpatterns += [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("dashboard/", ProfileView.as_view(), name="dashboard"),
    path("profile/", ProfileDetailView.as_view(), name='profile'),
    path("orders/", OrderBookListView.as_view(), name='orders'),
    path("cart/", CartBookListView.as_view(), name="cart"),
    path("my-books/", MyBookListView.as_view(), name="my_books"),
    path("new-book/", BookCreateView.as_view(), name="new_book"),
    path("<slug:slug>/update-book/", BookUpdateView.as_view(), name="update_book"),
    path("<slug:slug>/delete-book/", BookDeleteView.as_view(), name="delete_book"),

    path('add-to-orders/<int:book_id>/', add_to_orders, name='add_to_orders'),
    path('add-to-cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
]