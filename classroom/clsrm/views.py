from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from clsrm.models import Wheel, Nav, Mustbuy, Shop, MainShop


def index(request):
    return render(request,'home/home.html')


def home(request):
    #轮播
    wheels = Wheel.objects.all()
    #导航
    navs = Nav.objects.all()
    #必购
    mustbuys = Mustbuy.objects.all()
    #部分商品
    shops = Shop.objects.all()

    shophead = shops[0]

    shoptabs = shops[1:3]

    shopclass = shops[3:7]

    shopcomend = shops[7:11]

    #商品主体
    mainshows = MainShop.objects.all()
    data = {
        'wheels':wheels,
        'navs':navs,
        'mustbuys':mustbuys,
        'shophead':shophead,
        'shoptabs':shoptabs,
        'shopclass':shopclass,
        'shopcommends':shopcomend,
        'mainshows':mainshows,
    }
    return render(request,'home/home.html',data)


def market(request):
    return render(request, 'market/market.html')


def mine(request):
    return render(request, 'mine/mine.html')


def cart(request):
    return render(request, 'cart/cart.html')