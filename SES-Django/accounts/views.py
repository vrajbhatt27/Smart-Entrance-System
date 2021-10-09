from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def registerUser(request):
    if request.method =="POST":
        firstName= request.POST["first_name"]
        lastName = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmPassword = request.POST["password_confirmation"]
        if password == confirmPassword:
            if User.objects.filter(email=email).exists():
                print("user already exist...")
                return render(request,'registeration.html')
            else:
                print("registeration successful")
                user = User.objects.create_user(username=email,first_name=firstName,last_name=lastName,email=email,password=password)
                user.save()
                return redirect("/")
        else:
            print("password not matched")
            return render(request,'registeration.html')        
    else:
        return render(request,'registeration.html')

def loginUser(request):
    if request.method == "POST":
        email= request.POST.get("email")                
        password= request.POST.get("password")
        user = authenticate(username=email, password=password)
        print(user)
        if user is not None:
            login(request,user)
            print("in side")
            return redirect("/home")
            #  A backend authenticated the credentials
        else:
            return render(request,"login.html")
            # No backend authenticated the credentials

    return render(request,'login.html')
def logoutUser(request):
    logout(request)
    return redirect("/")