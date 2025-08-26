from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views.decorators.cache import never_cache
from .models import TravelOption
from .forms import TravelSearchForm

@never_cache
def travel_list(request):
    form = TravelSearchForm(request.GET or None)
    qs = TravelOption.objects.all()
    
    print(f"Initial queryset count: {qs.count()}")  # Debugging
    
    if form.is_valid():
        t = form.cleaned_data.get('type')
        src = form.cleaned_data.get('source')
        dst = form.cleaned_data.get('destination')
        date = form.cleaned_data.get('date')
        
        print(f"Form data - Type: {t}, Source: {src}, Destination: {dst}, Date: {date}")  # Debugging
        
        if t and t != '':  # Check if type is not empty
            qs = qs.filter(type=t)
            print(f"After type filter ({t}): {qs.count()}")  # Debugging
        
        if src and src != '':  # Check if source is not empty
            qs = qs.filter(source__icontains=src)
            print(f"After source filter ({src}): {qs.count()}")  # Debugging
        
        if dst and dst != '':  # Check if destination is not empty
            qs = qs.filter(destination__icontains=dst)
            print(f"After destination filter ({dst}): {qs.count()}")  # Debugging
        
        if date:  # Date field is already a date object, no need for empty check
            qs = qs.filter(date_time__date=date)
            print(f"After date filter ({date}): {qs.count()}")  # Debugging
    
    print(f"Final queryset count: {qs.count()}")  # Debugging
    return render(request, 'travels/travel_list.html', {'form': form, 'travels': qs})

def travel_detail(request, pk):
    travel = get_object_or_404(TravelOption, pk=pk)
    return render(request, 'travels/travel_detail.html', {'travel': travel})