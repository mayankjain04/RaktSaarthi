from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db import IntegrityError
from django.views import View

from manager.models import User, Donor, Recipient

def home(request):
    return render(request, 'manager/ayush.html')

def index(request):
    return render(request, 'manager/index.html')

def hospitals(request):
    return render(request, 'manager/hospitals.html')

def contact(request):
    return render(request, 'manager/jha-form.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            message = 'user not found'
            return render(request, 'manager/login.html', {
                'message':message,
            })
    return render(request, 'manager/login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirm"]
        if password != confirmation:
            return render(request, "manager/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "manager/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "manager/register.html")

class DonorView(View):
    def post(self, request):
        name = request.POST.get("name")
        medical_history = request.POST.get("medical_history")
        blood_group = request.POST.get("blood_group")
        location = request.POST.get("location")
        availability_status = request.POST.get("availability_status")
        last_donation_date = request.POST.get("last_donation_date")

        # Save to the Donor model
        Donor.objects.create(
            name=name,
            medical_history=medical_history,
            blood_group=blood_group,
            location=location,
            availability_status=availability_status,
            last_donation_date=last_donation_date if last_donation_date else None
        )

        return redirect("success")  # Redirect to a success page

class RecipientView(View):
    def post(self, request):
        name = request.POST.get("name")
        urgency_level = request.POST.get("urgency_level")
        location = request.POST.get("location")
        blood_type_required = request.POST.get("blood_type_required")

        # Save to the Recipient model
        Recipient.objects.create(
            name=name,
            urgency_level=urgency_level,
            location=location,
            blood_type_required=blood_type_required
        )

        return redirect("success")  # Redirect to a success page

    def get(self, request):
        return render(request, "blood-donation.html")