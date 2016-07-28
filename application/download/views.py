from django.shortcuts import render,redirect
from django.http import HttpResponse
from application.download.models import singcontents
# Create your views here.
def delThis(request):
    return render(request,'download/downmain.html')

def downcontents(request):
    contentList=singcontents.objects.all()
    return render(request,'download/downcontents.html',{'contents':contentList})