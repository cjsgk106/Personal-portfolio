from django.shortcuts import render

def myresume(request):
    return render(request, 'resume/myresume.html')
