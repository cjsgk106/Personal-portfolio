from django.shortcuts import render, get_object_or_404
from .models import Myr
from .models import Mysql

def rblog(request):
    rlan = Myr.objects
    return render(request, 'blog/rblog.html', {'rlan':rlan})

def rdetail(request, r_id):
    rlan_detail = get_object_or_404(Myr, pk=r_id)
    return render(request, 'blog/rdetail.html', {'rlan_detail':rlan_detail})

def sqlblog(request):
    sql = Mysql.objects
    return render(request, 'blog/sqlblog.html', {'sql':sql})

def sqldetail(request, sql_id):
    sql_detail = get_object_or_404(Mysql, pk=sql_id)
    return render(request, 'blog/sqldetail.html', {'sql_detail':sql_detail})
