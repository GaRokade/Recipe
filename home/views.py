from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    peoples=[{'name':'gayatri','age':19},
             {'name':'sam','age':20},
             {'name':'soham','age':12},
             {'name':'om','age':30},
             {'name':'vishal','age':10},]
    
    text="""For more straightforward sizing in CSS, we switch the global box-sizing value from content-box to border-box. This ensures padding does not affect the final computed width of an element, but it can cause problems with some third-party software like Google Maps and Google Custom Search Engine.

On the rare occasion you need to override it, use something like the following:
    """
   
    return render(request,'home/index.html',context={'page':'Django Tutorial','peoples':peoples,'text':text})

def about(request):
    context={'page':'about us' }
    return render(request,'home/about.html',context)

def contact(request):
    context={'page':'contact details' }
    return render(request,'home/contact.html',context)

def base(request):
    
    return render(request,'home/base.html')