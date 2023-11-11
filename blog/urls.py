from django.urls import path, include

from . import views


app_name = "blog"


urlpatterns = [
    path('blog-list/', views.BlogList.as_view(), name="bloglist"),
    path('new/', views.CreateBlog.as_view(), name="newblog"),
    path('<slug:slug>', views.BlogDetail.as_view(), name="blog-detail"),
    path('<slug:slug>/edit-blog/', views.BlogUpdate.as_view(), name="update-blog")
]
