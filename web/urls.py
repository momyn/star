from django.urls import path
from django.conf.urls.static import static

from un import settings
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path(r'^product/', views.category, name='product'),
    path(r'^tovar/(?P<slug>[-\w]+)/$', views.index1, name='tovar'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
