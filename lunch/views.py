from django.shortcuts import render, get_object_or_404, redirect
from .forms import LunchRequestForm
from .models import Lunchrequest

def lunchrequest_new(request):
    if request.method == "POST":
        form = LunchRequestForm(request.POST)
        if form.is_valid():
            lunch = form.save(commit=False)
            lunch.save()
            return redirect('lunch_confirm', pk=lunch.pk)
    else:
        form = LunchRequestForm()
    return render(request, 'lunch/lunch_form.html', {'form': form})

def lunch_confirm(request, pk):
    lunch = get_object_or_404(Lunchrequest, pk=pk)
    return render(request, 'lunch/lunch_confirm.html', {'lunch': lunch})

# Create your views here.
