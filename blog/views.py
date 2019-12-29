from django.shortcuts import render, get_object_or_404
from .models import Myr
from .models import Mysql
from .models import Mypy

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

def pyblog(request):
    python = Mypy.objects
    return render(request, 'blog/pyblog.html', {'python':python})

def pydetail(request, py_id):
    py_detail = get_object_or_404(Mypy, pk=py_id)
    return render(request, 'blog/pydetail.html', {'py_detail':py_detail})
