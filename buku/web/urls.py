from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('detail/<slug:slug>/',views.detail,name='detail'),
    path('category/<str:categories>/', views.category, name='categoris'),
    path('create/', views.create, name='create'),
    path('update/<int:update>', views.update, name='update'),
    path('delete/<int:delete>', views.delete, name='delete'),
    path('login/',views.buatlogin ,name ='login'),
    path('logout/',views.logoutview ,name ='logout'),
    path('register/', views.signup, name='register'),

]