from django.shortcuts import render
from django.http import HttpResponse

from .models import Image,Category


def index(request):
    return render(request,'index.html')


def login(request):
    cat=Category.objects.all()
    context = {"Category":cat}

    return render(request,'login.html', context=context)   


def home(request):
    all_images = Image.objects.all()
    cat=Category.objects.all()
    context = {"Images": all_images,"Category":cat}
    return render(request,'home.html', context=context)  

def category(request,cid):
    print(cid)
    cat = Category.objects.all()
    category=Category.objects.get(pk=cid)
    print(category,"eeeeee")
    image=Image.objects.filter(cat=category)
    context = {"Images": image,"Category":cat}
    return render(request,'home.html', context=context)

def download(request,my_id):
    title=Image.objects.get(pk=my_id)
    # image=Images.objects.filter()
    context={"title":title}
    return render(request,'download.html',context)    
     
   


# Create your views here.
