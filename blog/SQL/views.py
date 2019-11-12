from django.shortcuts import render, get_object_or_404
from .models import sqlmodel

def sqlblog(request):
    sql = sqlmodel.objects
    return render(request, 'SQL/sqlblog.html', {'sql':sql})

def detail(request, blog_id):
    sqldetail = get_object_or_404(sqlmodel, pk=blog_id)
    return render(request, 'SQL/detail.html', {'sqldetail':sqldetail})
