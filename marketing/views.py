# marketing/views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import DemoRequestForm

def home(request):
    return render(request, "home.html")

def steward(request):
    return render(request, "steward.html")

def pricing(request):
    return render(request, "pricing.html")

def contact(request):
    if request.method == "POST":
        form = DemoRequestForm(request.POST)
        if form.is_valid():
            demo = form.save()

            send_mail(
                subject="New Steward Demo Request",
                message=f"""
Name: {demo.name}
Organization: {demo.organization}
Email: {demo.email}

Message:
{demo.message}
""",
                from_email=None,
                recipient_list=["admin@clearcomsolutions.com"],
            )

            return redirect("home")
    else:
        form = DemoRequestForm()

    return render(request, "contact.html", {"form": form})