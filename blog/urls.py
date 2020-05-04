from django.urls import path, include
from . import views
from django.contrib import admin
from django.contrib import auth

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), 
    path('accounts/login/', include('django.contrib.auth.urls')),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #ただのURL、pkは投稿の番号
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
]