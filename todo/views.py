from django.shortcuts import render

# Create your views here.

from .forms import forme
from .models import car_info
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone


#what happens when we click add
def add(request):

    #After the user clicks "add"
    form=forme(request.POST)
    if form.is_valid():
        if float(request.POST["consommation"]) >= 0:
            #The form is a model form, it will automatically save the information
            form.save()
        else:
            return render(request, 'todo/liste.html', {'liste':car_info.objects.all(), 'form':forme(), 'error': "Consommation must be a positive number", })

        #Return to list after adding
    return HttpResponseRedirect(reverse('todo:liste'))
    

def liste(response):
    #What to display at first
    return render(response, 'todo/liste.html', {'form':forme(), 'liste':car_info.objects.all()})

def delete(request, num):
    #num is the car_info rank, used as an argument
    car_info.objects.get(pk=num).delete()

    #after deleting, come back to the liste page
    return HttpResponseRedirect(reverse('todo:liste'))

def draw(request):

    #Use js to draw a bar chart
    label = []
    data = []
    for a in car_info.objects.all():
        label.append(a.brand)
        data.append(float(a.consommation))
    return render(request, 'todo/chart.html', {'labels':label, 'data':data})
        
    
