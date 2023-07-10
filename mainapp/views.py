import secrets
import time

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User, Flight, Tickets, Airports, CancelledTickets
from .forms import UserSignupForm, UserLoginForm, AdminLoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse
import time, datetime
from django.contrib import messages


# User Use Cases
def index(request):
    return render(request, 'index.html')


def user_signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been successfully created!')
            return redirect('user_login')
    else:
        form = UserSignupForm()
    return render(request, 'user_signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login Successful')
                return redirect('flight_search')
            else:
                messages.error(request, 'Invalid username or password')
                form.add_error(None, 'Invalid username or password')
    else:
        form = UserLoginForm()
    return render(request, 'user_login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('index')


@login_required(login_url='user_login')
def flight_search(request):
    airports = Airports.objects.all()
    bookings = Tickets.objects.filter(user=request.user)
    if request.method == 'POST':
        origin = request.POST['origin']
        destination = request.POST['destination']
        departure_date = request.POST['departure_date']
        print(f"#DATE {departure_date}#")
        year, month, date = map(int, departure_date.split('-'))
        weekday = datetime.date(year, month, date).weekday()
        departure_time = request.POST['departure_time']
        flights = Flight.objects.filter(departure_date=departure_date)
        return render(request, 'flight_search_results.html', {'flights': flights})
    return render(request, 'flight_search.html', {'airports': airports, 'bookings': bookings})


@login_required(login_url='user_login')
def flight_booking(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    print(flight.flight_number)
    print(request.user)
    print(request.user.is_authenticated)
    print(request.method)
    if request.method == 'POST':
        print("Posted")
        seats_available = flight.seats_count
        seat_number = seats_available
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        ticket_fare = flight.fare + 80
        booking = Tickets.objects.create(user=request.user, flight=flight, passenger=name, p_mail=email, p_phone=phone,
                                         age=age, sex=gender, fare_charges=ticket_fare,
                                         seat_number=seat_number)
        booking.ref_no = secrets.token_hex(3).upper()
        if seats_available > 0:
            booking.status = 'CONFIRMED'
        else:
            booking.status = 'CANCELED'
        booking.save()
        flight.seats_count = seats_available - 1
        flight.save()
        booking = Tickets.objects.filter(user=request.user)
        return redirect('make_payment', flight_id=flight.id)
    return render(request, 'flight_booking.html', {'flight': flight})


@login_required(login_url='user_login')
def make_payment(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    fare_charges = flight.fare + 80
    if request.method == 'POST':
        return redirect('payment_status', flight_id=flight.id)
    return render(request, 'payment.html', {'flight': flight, 'fare': fare_charges})


@login_required(login_url='user_login')
def payment_status(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    time.sleep(5)
    return render(request, 'payment_process.html', {'flight': flight})


@login_required(login_url='user_login')
def my_bookings(request):
    bookings = Tickets.objects.filter(user=request.user)
    return render(request, 'my_bookings.html', {'bookings': bookings})


def cancel_ticket(request, booking_id):
    booking = Tickets.objects.get(id=booking_id)
    flight = Flight.objects.get(id=Tickets.objects.get(id=booking_id).flight.id)
    seats_available = flight.seats_count
    flight.seats_count = seats_available + 1
    flight.save()
    booking.status = 'CANCELLED'
    CancelledTickets.objects.create(user=booking.user, ref_no=booking.ref_no, flight=booking.flight,
                                    passenger=booking.passenger, seat_number=booking.seat_number)

    booking.delete()
    # booking.save()
    return redirect('my_bookings')


def view_ticket(request, booking_id):
    booking = Tickets.objects.get(id=booking_id)
    return render(request, 'view_ticket.html', {'booking': booking})


# Admin Use Cases
def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_staff:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = AdminLoginForm()
    return render(request, 'admin_login.html', {'form': form})


@login_required(login_url='admin_login')
def admin_dashboard(request):
    flights = Flight.objects.all()
    bookings = Tickets.objects.all()
    cancelled = CancelledTickets.objects.all()
    return render(request, 'admin_dashboard.html', {'flights': flights, 'bookings': bookings, 'cancelled': cancelled})


@login_required(login_url='admin_login')
def add_flight(request):
    if request.method == 'POST':
        flight_number = request.POST.get('flight_number')
        airline = request.POST.get('air_line')
        departure_city = request.POST.get('departure_city')
        arrival_city = request.POST.get('arrival_city')
        departure_date = request.POST.get('departure_date')
        departure_time = request.POST.get('departure_time')
        arrival_date = request.POST.get('arrival_date')
        arrival_time = request.POST.get('arrival_time')
        seats_count = request.POST.get('seats_available')
        fare = request.POST.get('fare')
        cities = []
        if departure_city not in cities or arrival_city not in cities:
            if departure_city not in cities:
                cities.append(departure_city)
            if arrival_city not in cities:
                cities.append(arrival_city)
        for i in cities:
            if not Airports.objects.filter(airport_name=i).exists():
                airports = Airports.objects.create(airport_name=i)
                airports.save()
        flight = Flight(flight_number=flight_number, airline=airline,
                        departure_city=Airports.objects.get(airport_name=cities[0]),
                        arrival_city=Airports.objects.get(airport_name=cities[1]),
                        departure_date=departure_date, departure_time=departure_time, arrival_date=arrival_date,
                        arrival_time=arrival_time, seats_count=seats_count,
                        fare=fare)
        flight.save()
        return redirect('admin_dashboard')
    return render(request, 'add_flight.html')


@login_required(login_url='admin_login')
def remove_flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    flight.delete()
    return redirect('admin_dashboard')


def login_portal(request):
    return render(request, 'login_portal.html')
