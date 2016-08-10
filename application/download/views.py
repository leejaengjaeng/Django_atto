from django.shortcuts import render,redirect
from django.http import HttpResponse
from application.download.models import singcontents
from application.download.models import doccontents
# Create your views here.
def delThis(request):
    return render(request,'download/downmain.html')

def downcontents(request):
    contentList=singcontents.objects.all()
    return render(request,'download/downcontents.html',{'contents':contentList,'flag':0})

def downdocs(request):
    docscontents=doccontents.objects.all()
    return render(request,'download/downcontents.html',{'contents':docscontents,'flag':1})

def teacher(request):
    return render(request,'download/teacherPage.html',{})

def community(request):
    return render(request, 'download/communityPage.html', {})
