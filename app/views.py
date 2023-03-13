from django.shortcuts import render

# Create your views here.
def Jinja_first(request):
    d={'name':'Gavya Sri','age':4}
    return render(request,'jinja_first.html',context=d)