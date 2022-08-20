from django.db.models import Sum, Count
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import RegistrationData, FarmRecords
from django.views.decorators.cache import never_cache
import logging


# Create your views here.

def Home(request):
    context = {
        "name": {"Farm Solutions records"},
            }
    return render(request, 'home.html', context)


def image(request):
    context = {
        "name": {"Farm Solutions images"},
            }
    return render(request, 'image.html', context)


@never_cache
def records(request):
    context = {
        "name": {"Farm Solutions"},
        "number": {"6700"}
    }
    return render(request, 'records.html', context)


@never_cache
def register(request):
    context = {
        "form": RegistrationForm
    }
    return render(request, 'signup.html', context)


@never_cache
def table(request):
    data = FarmRecords.objects.all()
    quantity = FarmRecords.objects.count()
    context = {
        "name": {"Farm Records Table"},
        "farm_data": data,
        "tquantity": quantity

    }
   # raise Exception("i want to know value" + str(quantity))
    return render(request, 'tables.html', context)


@never_cache
def addUSer(request):
    form = RegistrationForm(request.POST)

    if form.is_valid():
        myregister = RegistrationData(username=form.cleaned_data['username'],
                                      password=form.cleaned_data['password'],
                                      email=form.cleaned_data['email'],
                                      phone=form.cleaned_data['phone'])

        myregister.save()

    return redirect('home')
