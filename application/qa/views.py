from django.shortcuts import render

# Create your views here.
def qa(request):

    return render(request, "qa/qa.html")