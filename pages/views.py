from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


from listings.models import Listing
from realtors.models import Realtor

def index(request):
    listing = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings' : listing
    }
    return render(request,'pages/index.html',context)

def about(request):
    #get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp= True)
    context = {
        'realtors' : realtors,
        'mvp_realtors':mvp_realtors
    }
    return render(request,'pages/about.html',context)