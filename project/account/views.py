from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import customers
# Create your views here.



def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fullname = request.POST.get('fullname')
        location = request.POST.get('location')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        gender = request.POST.get('gender')  # This corresponds to the choice field

        # Check if the user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Magaca isticmaalaha ayaa hore u jiray!')
            return render(request, 'account/register.html')

        # Create a new user if username is not taken
        user = User.objects.create_user(username=username, password=password)
        user.save()
        # Create a new customer with the correct fields
        new_customer = customers(Fullname=fullname, user=user, Location=location, Phone=phone, gender=gender)
        new_customer.save()
        messages.success(request, 'Koontada si guul leh ayaa loo sameeyay!')
        return redirect('login')

    return render(request, 'account/register.html')



def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password =  request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None:

            login(request,user)
            return redirect("Home")

        else:
            message = messages.error(request, "Isticmaalka ama erayga sirta ah ee aan ansax ahayn")
            return render(request,'account/Signin.html',{"message":message})




    return render(request,'account/Signin.html',{})






def logout_view(request):
    logout(request)
    return redirect('login')