from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Booking
from django.contrib import messages

# Create your views here.

def booking(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        booking = Booking(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        booking.save()
        messages.success(request, 'Thanx for your Booking We got your request for booking R.K PUB & Bar.. will contact you as soon as possible.!')
    return render(request, 'booking.html')
 