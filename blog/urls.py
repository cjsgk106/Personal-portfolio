from django.urls import include, path
from . import views

urlpatterns = [
    path('r/', views.rblog, name='rblog'),
    path('sql/', views.sqlblog, name='sqlblog'),
    path('python/', views.pyblog, name='pyblog'),
    path('r/<int:r_id>/', views.rdetail, name='rdetail'),
    path('sql/<int:sql_id>/', views.sqldetail, name='sqldetail'),
    path('python/<int:py_id>/', views.pydetail, name='pydetail'),
]
