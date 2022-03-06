from django.urls import path
#from . import views
from .views import AddPostView, HomeView, ArticleDetailView, UpdatePostView, DeletePostView, LogoutView, ProfilView, AddCategoryView, CategoryView, CatView

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name = 'home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name = 'article-detail'),
    path('add_post', AddPostView.as_view(), name = 'add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name = 'update_post'),
    path('article/<int:pk>/romove', DeletePostView.as_view(), name = 'delete_post'),
    path('logout', LogoutView.as_view(), name = 'logout1'),         #my
    path('profil', ProfilView.as_view(), name = 'profil'),          #my
    path('add_category', AddCategoryView.as_view(), name = 'add_category'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('cat/', CatView.as_view(), name='cat'),                    #my
]
