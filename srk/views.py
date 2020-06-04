from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from .forms import emplForm
from .models import Employee


def home(request):
    return render(request, 'home.html',)

def empl_list(request):
    Employees = Employee.objects.all()
    return render(request, 'empl_list.html', {
        'Employees': Employees
    })


def empl_upload(request):
    if request.method == "POST":
        form = emplForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('empl_list')
        else:
            form = emplForm()
    form = emplForm()
    return render(request, 'empl_upload.html', {
        'form': form
    })


def delete_empl(request, pk): 
    if request.method =="POST":
        Employees = Employee.objects.get(pk=pk)
        Employees.delete()
    return redirect('empl_list')


def update_empl(request, pk):
    if request.method =='POST':
        Employees = Employee.objects.get(pk=pk)
        form = emplForm(request.POST, instance=Employees)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('empl_list') )

    template_name = 'empl_upload.html'
    context = {'form': emplForm(instance=Employees)}
    return render(request, 'empl_upload.html', context)




