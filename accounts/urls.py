from django.urls import path, include
from . import views
app_name = "accounts"
urlpatterns = [
    path('signup', views.register, name="signup"),
    path('login', views.signin, name="login"),
    path('logout', views.signout, name="logout"),
    path('profile', views.profile, name="profile"),
    path('edit-profile', views.profileEdit, name="edit-profile"),
    path('myblogs', views.MyBlogs.as_view(), name="myblogs"),
]

