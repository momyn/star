from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from un import settings
from web import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('delivery/', views.delivery, name='delivery'),
    path(r'^product/$', views.category, name=('category')),
    path('<slug:url>/', views.index1, name='index1'),
    # path('/product/$/<slug:url>/', views.category2, name='category2'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
