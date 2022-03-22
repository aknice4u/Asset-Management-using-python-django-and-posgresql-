from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from assetsmgt import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-category', views.add_category, name='add-category'),
    path('save_category', views.save_category),
    path('edit/<int:id>/', views.update_category, name='update_category'),
    path('save_updated', views.save_updated),
    path('delete/<int:id>/', views.delete_category, name='delete_category'),
    path('add-brand', views.create_brand, name="add-brand"),
    path('edit/brand/<int:id>/', views.edit_brand, name='edit_brand'),
    path('update-brand', views.update_brand),
    path('delete/brand/<int:id>/', views.delete_brand, name='delete_brand'),
    path('delete/brand/<int:id>/', views.delete_brand, name='delete_brand'),
    path('add-asset', views.add_asset, name='add-asset'),
    path('fetch-brands', views.fetch_brands, name='fetch-brands'),
    path('list-assets', views.list_assets, name='list-assets'),
    path('edit-asset/<int:id>/', views.edit_asset, name='edit-asset'),
    path('login', views.view_login, name='login'),
    path('add-department', views.add_department, name='add-department'),
    path('update-department/<int:id>/', views.update_department, name='update-department'),
    path('delete-department/<int:id>/', views.delete_department, name='delete-department'),
    path('add-branch', views.add_branch, name='add-branch'),
    path('update-branch/<int:id>/', views.update_branch, name='update-branch'),
    path('delete-branch/<int:id>/', views.delete_branch, name='delete-branch'),


]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
