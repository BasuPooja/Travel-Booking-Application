from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import TravelOption
from .forms import TravelSearchForm

def travel_list(request):
    form = TravelSearchForm(request.GET or None)
    qs = TravelOption.objects.all()
    if form.is_valid():
        t = form.cleaned_data.get('type')
        src = form.cleaned_data.get('source')
        dst = form.cleaned_data.get('destination')
        date = form.cleaned_data.get('date')
        if t:
            qs = qs.filter(type=t)
        if src:
            qs = qs.filter(source__icontains=src)
        if dst:
            qs = qs.filter(destination__icontains=dst)
        if date:
            qs = qs.filter(date_time__date=date)
    return render(request, 'travels/travel_list.html', {'form': form, 'travels': qs})

def travel_detail(request, pk):
    travel = get_object_or_404(TravelOption, pk=pk)
    return render(request, 'travels/travel_detail.html', {'travel': travel})
