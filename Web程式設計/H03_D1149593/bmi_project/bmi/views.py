from django.shortcuts import render, redirect
from .forms import PersonForm
from .models import Person
from django.db.models import ExpressionWrapper, F, FloatField
import random

def bmi_form(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bmi_form')
    else:
        form = PersonForm()
    return render(request, 'bmi/bmi_form.html', {'form': form})

def delete_data(request):
    if request.method == 'POST':
        Person.objects.all().delete()
        return redirect('bmi_form')
    return render(request, 'bmi/delete_data.html')

def bmi_statistics(request):
    bmi_expr = ExpressionWrapper(
        F('weight') / ((F('height') / 100) ** 2), output_field=FloatField()
    )
    low_bmi = Person.objects.annotate(bmi=bmi_expr).filter(bmi__lt=18.5)
    normal_bmi = Person.objects.annotate(bmi=bmi_expr).filter(bmi__gte=18.5, bmi__lt=24)
    high_bmi = Person.objects.annotate(bmi=bmi_expr).filter(bmi__gte=24)
    context = {
        'LowBMI': low_bmi,
        'NormalBMI': normal_bmi,
        'HighBMI': high_bmi
    }
    return render(request, 'bmi/bmi_statistics.html', context)

def generate_data(request):
    first_name = ["Charlotte", "Olivia", "Mia", "Grace", "Amelia", "Oliver", "Bruce", "Jack", "Henry", "Thomas"]
    last_name = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson"]
    for fname in first_name:
        height = round(random.uniform(140, 190), 2)
        weight = round(random.uniform(40, 90), 2)
        lname = last_name[random.randint(0, 9)]
        Person.objects.create(name=fname+" "+lname, height=height, weight=weight)
    return redirect('bmi_form')