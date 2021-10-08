from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<slug:slug>/', views.detail, name='detail'),
    path('category/<str:categories>/', views.category, name='categoris'),
    path('create/', views.create, name='create'),
    path('update/<int:update>', views.update, name='update'),
    path('delete/<int:delete>', views.delete, name='delete'),
    path('login/', views.buatlogin, name='login'),
    path('logout/', views.logoutview, name='logout'),
    path('register/', views.signup, name='register'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password/password_reset_form.html'), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password/password_reset_confirm.html'), name='password_reset_confirm'),

    path('reset/done', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),

]