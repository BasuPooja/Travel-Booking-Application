from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from .models import Booking
from travels.models import TravelOption

@login_required
@transaction.atomic
def book_travel(request, pk):
    travel = get_object_or_404(TravelOption, pk=pk)
    if request.method == 'POST':
        try:
            seats = int(request.POST.get('seats', '1'))
        except ValueError:
            messages.error(request, "Please enter a valid number of seats.")
            return redirect('travel_detail', pk=pk)

        if seats <= 0:
            messages.error(request, "Seats must be greater than zero.")
            return redirect('travel_detail', pk=pk)

        travel = TravelOption.objects.select_for_update().get(pk=pk)
        if seats > travel.available_seats:
            messages.error(request, "Not enough seats available.")
            return redirect('travel_detail', pk=pk)

        total_price = seats * float(travel.price)

        Booking.objects.create(
            user=request.user,
            travel_option=travel,
            number_of_seats=seats,
            total_price=total_price,
        )
        travel.available_seats -= seats
        travel.save()
        messages.success(request, "Booking confirmed!")
        return redirect('my_bookings')
    return render(request, 'bookings/book_form.html', {'travel': travel})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})

@login_required
@transaction.atomic
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id, user=request.user)
    if booking.status == 'Cancelled':
        return redirect('my_bookings')
    if request.method == 'POST':
        travel = TravelOption.objects.select_for_update().get(pk=booking.travel_option.pk)
        booking.status = 'Cancelled'
        booking.save()
        travel.available_seats += booking.number_of_seats
        travel.save()
        messages.info(request, "Booking cancelled and seats restored.")
        return redirect('my_bookings')
    return render(request, 'bookings/confirm_cancel.html', {'booking': booking})
