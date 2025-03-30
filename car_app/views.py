from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from .models import ServiceBooking
from django.http import JsonResponse
from django.core.mail import send_mail
import json
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm
from .models import ContactMessage
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return render(request, "home.html")  # Your main home page
    else:
        return redirect("register")  # Redirect to register page by default

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def booking(request):
    return render(request, 'booking.html')

def technicians(request):
    return render(request, 'team.html')

def testimonials(request):
    return render(request, 'testimonial.html')

def badrequest(request):
    return render(request, '404.html')

def contact(request):
    return render(request, 'contact.html')

def book_service(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        service_type = request.POST.get('service_type')
        service_date = request.POST.get('service_date')
        special_request = request.POST.get('special_request')

        if name and email and service_type and service_date:
            ServiceBooking.objects.create(
                name=name,
                email=email,
                service_type=service_type,
                service_date=service_date,
                special_request=special_request
            )
            messages.success(request, "Your service booking was successful!", extra_tags="booking")
        else:
            messages.error(request, "All fields are required!")

        return redirect('service')  # ✅ Redirect to service page after booking
    return render(request, 'service.html')



def contact_submit(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, "Your message has been sent successfully!")
        else:
            messages.error(request, "All fields are required!")

        return redirect('contact')  # Redirect back to the contact page
    return render(request, 'contact.html')


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Get email input

        if not email:
            return JsonResponse({"error": "Email is required."}, status=400)

        # Email Content
        user_subject = "Subscription Successful"
        user_message = "Thank you for subscribing to CarServ! Stay tuned for updates."

        try:
            # Send email
            send_mail(
                subject=user_subject,
                message=user_message,
                from_email='murugangv555@gmail.com',  # Replace with your email
                recipient_list=[email],  
                fail_silently=False,
            )

            # Return success response in JSON format
            return JsonResponse({"message": "Thank you for subscribing! Please check your email."})
        
        except Exception as e:
            return JsonResponse({"error": f"An error occurred: {e}"}, status=500)

    return render(request, 'base.html')



def help_request(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_email = data.get("email")
        user_message = data.get("message")

        # Send email to admin
        send_mail(
            subject=f"Help Request from {user_email}",
            message=user_message,
            from_email=user_email,
            recipient_list=["murugangv555@gmail.com"],
            fail_silently=False,
        )

        return JsonResponse({"message": "Success"})
    
    return JsonResponse({"message": "Invalid request!"}, status=400)


# User Registration View
def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect logged-in users to home
    
    form = RegisterForm(request.POST or None)  # Don't reset the form
    
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login after registration
            messages.success(request, "Registration successful!")
            return redirect('home')
        else:
            messages.error(request, "Registration failed. Please check the form.")
    
    return render(request, 'register.html', {'form': form})

# User Login View
from django.contrib import messages

def login_view(request):
    

    form = LoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                messages.success(request, "Login successful!")
                print("✅ DEBUG: Login successful message added.")  # Debug print
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")  # Add error message
                print("🚨 DEBUG: Invalid username or password message added!")  # Debug print
                
    print("🚨 DEBUG: All messages ->", list(messages.get_messages(request)))  # Debug print

    return render(request, 'login.html', {'form': form})


# User Logout View
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')



def privacy_policy(request):
    return render(request, 'privacy_policy.html')


def terms_conditions(request):
    return render(request, 'terms_conditions.html')



