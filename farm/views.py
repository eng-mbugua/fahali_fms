from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone

from .models import Livestock, Crop, Resource, VetRecord, FinancialRecord, MarketItem
from .forms import LivestockForm


# Create your views here.

def index(request):
    return render(request,'index.html')
def dashboard(request):
    #Financial Summary
    financials = FinancialRecord.objects.all()
    income = financials(type='Income').aggregate(total=Sum('amount'))['total'] or Decimal('0')
    expenses = financials(type='Expense').aggregate(total=Sum('amount'))['total'] or Decimal('0')
    profit = income - expenses

    #Counts
    livestock_count = Livestock.objects.count()
    active_crops_count = Crop.objects.count()

    context = {
        'income': income,
        'expenses': expenses,
        'profit': profit,
        'livestock_count': livestock_count,
        'active_crops_count': active_crops_count,
    }

    return render(request, 'dashboard.html', context)

def crops(request):
    crops_list = Crop.objects.all()
    return render(request,'crops.html', {"crops_list":crops_list})
def add_crop(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        fieldLocation = request.POST.get('fieldLocation')
        plantingDate = request.POST.get('plantingDate')
        expectedHarvestDate = request.POST.get('expectedHarvestDate')

        Crop.objects.create(type=type, fieldLocation=fieldLocation, plantingDate=plantingDate, expectedHarvestDate=expectedHarvestDate)
        return redirect('crops')
    return render(request,'crops.html')
def delete_crop(request, id):
    if request.method == "POST":
        crops_list = get_object_or_404(Crop, id=id)
        crops_list.delete()
        return redirect('crops')
    return render(request,'crops.html', {})


def livestock(request):
    livestock_list = Livestock.objects.all()
    return render(request,'livestock.html', {"livestock_list":livestock_list})
def add_livestock(request):
    if request.method == "POST":
        category = request.POST.get('category')
        tagId = request.POST.get('tagId')
        breed = request.POST.get('breed')
        age = request.POST.get('age')
        location = request.POST.get('location')
        healthStatus = request.POST.get('healthStatus')
        owner= request.POST.get('owner')

        Livestock.objects.create(category=category, tagId=tagId, breed=breed, age=age, location=location, healthStatus=healthStatus, owner=owner)
        return redirect('livestock')


    return render(request,'livestock.html', {})
def delete_livestock(request, id):
    if request.method == "POST":
        livestock_list = get_object_or_404(Livestock, id=id)
        livestock_list.delete()
        return redirect('livestock')
    return render(request,'livestock.html', {})

def resources(request):
    resources_list = Resource.objects.all()
    return render(request,'resources.html', {"resources_list":resources_list})
def add_resource(request):
    if request.method == "POST":
        name = request.POST.get('name')
        type = request.POST.get('type')
        quantity = request.POST.get('quantity')
        unit= request.POST.get('unit')

        Resource.objects.create(name=name, type=type, quantity=quantity, unit=unit)
        return redirect('resources')
    return render(request,'resources.html', {})
def delete_resource(request, id):
    if request.method == "POST":
        resources_list = get_object_or_404(Resource, id=id)
        resources_list.delete()
        return redirect('resources')
    return render(request,'resources.html', {})

def vet(request):
    vet_list = VetRecord.objects.all()
    return render(request,'vet.html', {"vet_list":vet_list})
def add_vet_record(request):
    if request.method == "POST":
        livestockId = request.POST.get('livestockId')
        treatment = request.POST.get('treatment')
        date = request.POST.get('date')
        veterinarian = request.POST.get('veterinarian')
        cost = request.POST.get('cost')

        VetRecord.objects.create(livestockId=livestockId, treatment=treatment, date=date, veterinarian=veterinarian, cost=cost)
        return redirect('vet')
    return render(request,'vet.html', {})
def delete_vet_record(request, id):
    if request.method == "POST":
        vet_list = get_object_or_404(VetRecord, id=id)
        vet_list.delete()
        return redirect('vet')
    return render(request,'vet.html', {})


def financials(request):
    financials = FinancialRecord.objects.all()
    total_income = financials(type='Income').aggregate(total=Sum('amount'))['total'] or Decimal('0')
    total_expenses = financials(type='Expense').aggregate(total=Sum('amount'))['total'] or Decimal('0')
    net_profit = total_income - total_expenses

    # simple percentages for placeholder chart
    total = (total_income + total_expenses) or Decimal('1')
    income_pct = int((total_income / total) * 100)
    expense_pct = int((total_expenses / total) * 100)

    context = {
        'financials_list': financials_list,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'net_profit': net_profit,
        'income_pct': income_pct,
        'expense_pct': expense_pct,
    }
    return render(request, 'financials.html', context)


def add_financial(request):
    if request.method == 'POST':
        ftype = request.POST.get('type')
        date = request.POST.get('date') or timezone.now().date()
        amount = request.POST.get('amount') or 0
        category = request.POST.get('category')
        description = request.POST.get('description', '')
        FinancialRecord.objects.create(
            type=ftype,
            date=date,
            amount=amount,
            category=category,
            description=description
        )
        messages.success(request, "Financial record added.")
    return redirect('financials')

def marketplace(request):
    market_item_list = MarketItem.objects.all()
    return render(request, 'marketplace.html', {"market_item_list":market_item_list})


