from django.urls import include, path
from . import views

urlpatterns = [
    path('blog/', views.sqlblog, name='sqlblog'),
    path('<int:blog_id>/', views.detail, name='sqldetail'),
]
