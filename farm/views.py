from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Livestock, Crop, Resource, VetRecord, FinancialRecord, MarketItem


# Create your views here.

def index(request):
    return render(request,'index.html')
def dashboard(request):
    return render(request,'dashboard.html')
def crops(request):
    crops_list = Crop.objects.all()
    return render(request,'crops.html', {"crops_list":crops_list})
def livestock(request):
    livestock_list = Livestock.objects.all()
    return render(request,'livestock.html', {"livestock_list":livestock_list})
def resources(request):
    resources_list = Resource.objects.all()
    return render(request,'resources.html', {"resources_list":resources_list})
def vet(request):
    vet_list = VetRecord.objects.all()
    return render(request,'vet.html', {"vet_list":vet_list})
def financials(request):
    financials_list = FinancialRecord.objects.all()
    return render(request, 'financials.html', {"financials_list":financials_list})
def marketplace(request):
    market_item_list = MarketItem.objects.all()
    return render(request, 'marketplace.html', {"market_item_list":market_item_list})

