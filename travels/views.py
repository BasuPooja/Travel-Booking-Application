from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.views.decorators.cache import never_cache
from django.core.paginator import Paginator
from .models import TravelOption
from .forms import TravelOptionForm, TravelSearchForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

def is_staff_user(user):
    return user.is_staff or user.is_superuser

@login_required
@user_passes_test(is_staff_user)
def add_travel_option(request):
    if request.method == 'POST':
        form = TravelOptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Travel option added successfully!')
            return redirect('travel_list')
    else:
        form = TravelOptionForm()
    
    return render(request, 'travels/add_travel_option.html', {'form': form})

@login_required
@user_passes_test(is_staff_user)
def manage_travel_options(request):
    qs = TravelOption.objects.all().order_by("date_time")

    # Apply filters
    form = TravelSearchForm(request.GET or None)
    if form.is_valid():
        t = form.cleaned_data.get("type")
        src = form.cleaned_data.get("source")
        dst = form.cleaned_data.get("destination")
        date = form.cleaned_data.get("date")

        if t and t != "":
            qs = qs.filter(type=t)
        if src and src != "":
            qs = qs.filter(source__icontains=src)
        if dst and dst != "":
            qs = qs.filter(destination__icontains=dst)
        if date:
            qs = qs.filter(date_time__date=date)

    # Pagination (7 per page)
    paginator = Paginator(qs, 7)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "travels/manage_travel_options.html",
        {"travel_options": page_obj, "form": form},
    )

@never_cache
def travel_list(request):
    qs = TravelOption.objects.all().order_by("date_time")
    form = TravelSearchForm(request.GET or None)

    if form.is_valid():
        t = form.cleaned_data.get("type")
        src = form.cleaned_data.get("source")
        dst = form.cleaned_data.get("destination")
        date = form.cleaned_data.get("date")

        if t and t != "":
            qs = qs.filter(type=t)
        if src and src != "":
            qs = qs.filter(source__icontains=src)
        if dst and dst != "":
            qs = qs.filter(destination__icontains=dst)
        if date:
            qs = qs.filter(date_time__date=date)

    # Pagination (7 per page)
    paginator = Paginator(qs, 7)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "travels/travel_list.html",
        {"form": form, "travels": page_obj},
    )

def travel_detail(request, pk):
    travel = get_object_or_404(TravelOption, pk=pk)
    return render(request, 'travels/travel_detail.html', {'travel': travel})
