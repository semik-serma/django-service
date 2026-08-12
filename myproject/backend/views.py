from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def services(request):
    return render(request, 'home/services.html')

def contact(request):
    return render(request, 'home/about.html')

def product_detail(request, product_id='aeroflow-max'):
    context = {
        'product_id': product_id,
        'title': 'AEROFLOW MAX',
        'subtitle': 'Active Noise Canceling Headphones',
        'rating': '4.8',
        'reviews_count': '1,450',
        'original_price': '399',
        'price': '299.00',
        'savings': '100',
        'description': 'Immerse yourself in pure sound. Experience industry-leading Active Noise Cancellation, 40-hour battery life, and unparalleled comfort.'
    }
    return render(request, 'home/product_detail.html', context)