from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:project_id>', views.detail, name='projectdetail'),
]
