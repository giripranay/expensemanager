from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import table
from .forms import ContactForm
from datetime import datetime

# Create your views here.
def index(request):
    bills_list=table.objects.all()
    data={'lis':bills_list,}
    return render(request,'expensemanager/index.html',data)
def addnew(request):
    if request.method =='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            newitem=form.save(commit=False)
            newitem.save()
            return redirect('index')
    else:
        form=ContactForm()
    return render(request,'expensemanager/addnew.html',{'form':form})


def graph(request):
    
    food=table.objects.filter(CATEGORY="FOOD")
    dfood={'lis':food,}
    c1=0
    for row in dfood['lis']:
        c1 +=row.cost
    
    grocery=table.objects.filter(CATEGORY="GROCERY")
    dgrocery={'lis':grocery,}
    c2=0
    for row in dgrocery['lis']:
        c2 +=row.cost
 
    entertainment=table.objects.filter(CATEGORY="ENTERTAINMENT")
    dentertainment={'lis':entertainment,}
    c3=0
    for row in dentertainment['lis']:
        c3 +=row.cost
  
    petrol=table.objects.filter(CATEGORY="PETROL")
    dpetrol={'lis':petrol,}
    c4=0
    for row in dpetrol['lis']:
        c4 +=row.cost
    d={"food":c1 ,"grocery":c2,"entertainment":c3,"petrol":c4}
    
    return render(request,'expensemanager/graph.html',d)

def food(request):
    today_list=table.objects.filter(CATEGORY="FOOD")
    data={'lis':today_list,}
    return render(request,'expensemanager/food.html',data)

def grocery(request):
    today_list=table.objects.filter(CATEGORY="GROCERY")
    data={'lis':today_list,}
    return render(request,'expensemanager/grocery.html',data)

def petrol(request):
    today_list=table.objects.filter(CATEGORY="PETROL")
    data={'lis':today_list,}
    return render(request,'expensemanager/petrol.html',data)


def entertainment(request):
    today_list=table.objects.filter(CATEGORY="ENTERTAINMENT")
    data={'lis':today_list,}
    return render(request,'expensemanager/entertainment.html',data)
