from django.urls import include, path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('r/', views.rblog, name='rblog'),
    path('sql/', views.sqlblog, name='sqlblog'),
    path('r/<int:r_id>/', views.rdetail, name='rdetail'),
    path('sql/<int:sql_id>/', views.sqldetail, name='sqldetail'),
]

urlpatterns += staticfiles_urlpatterns()
