from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from clsrm.models import Wheel


def index(request):
    return render(request,'home/home.html')


def home(request):
    wheels = Wheel.objects.all()
    return render(request,'home/home.html',{'wheels':wheels})


def market(request):
    return render(request, 'market/market.html')


def mine(request):
    return render(request, 'mine/mine.html')


def cart(request):
    return render(request, 'cart/cart.html')