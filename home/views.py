from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context = {"variable":"Hi Shreepad"}
    return render(request,'index.html',context)
    # return HttpResponse("this is Homepage")
def about(request):
    return HttpResponse("this is about us page")
def contact(request):
    return HttpResponse("this is contact us page")
   