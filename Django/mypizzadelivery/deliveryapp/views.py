from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import PizzaModel, CustomerModel, OrderModel

# Create your views here.


def adminloginview(request):
    return render(request, 'deliveryapp/adminlogin.html')


def authenticateadmin(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None and user.username == "admin":
        login(request, user)
        return redirect('adminhomepage')
    else:
        messages.add_message(request, messages.ERROR, "Invalid Credentials")
        return redirect('adminloginpage')


def adminhomapeview(request):
    if not request.user.is_authenticated or request.user.username != "admin":
        return redirect('adminloginpage')
    context = {'pizzas': PizzaModel.objects.all()}
    return render(request, 'deliveryapp/adminhomepage.html', context)


def logoutadmin(request):
    logout(request)
    return redirect('adminloginpage')


def addpizza(request):
    name = request.POST['name']
    price = request.POST['price']
    PizzaModel(name=name, price=price).save()
    return redirect('adminhomepage')


def deletepizza(request, pizzapk):
    PizzaModel.objects.filter(id=pizzapk).delete()
    return redirect('adminhomepage')


def homepageview(request):
    return render(request, 'deliveryapp/homepage.html')


def signupuser(request):
    username = request.POST['username']
    password = request.POST['password']
    phoneno = request.POST['phoneno']
    if User.objects.filter(username=username).exists() or username == "admin":
        messages.add_message(request, messages.ERROR, "User Already Exists")
        return redirect('homepage')
    User.objects.create_user(username=username, password=password).save()
    lastobject = len(User.objects.all())-1
    CustomerModel(id=User.objects.all()[int(lastobject)].id, phoneno=phoneno).save()
    messages.add_message(request, messages.ERROR, "User Successfuly Created")
    return redirect('homepage')


def userloginview(request):
    return render(request, 'deliveryapp/userlogin.html')


def authenticateuser(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None and user.username != "admin":
        login(request, user)
        return redirect('customerpage')
    else:
        messages.add_message(request, messages.ERROR, "Invalid Credentials")
        return redirect('userloginpage')


def customerwelcomeview(request):
    if not request.user.is_authenticated:
        return redirect('userloginpage')
    username = request.user.username
    context = {'username': username, 'pizzas': PizzaModel.objects.all()}
    return render(request, 'deliveryapp/customerwelcome.html', context)


def logoutuser(request):
    logout(request)
    return redirect('userloginpage')


def placeorder(request):
    if not request.user.is_authenticated:
        return redirect('userloginpage')
    username = request.user.username
    phonenum = CustomerModel.objects.filter(userid=request.user.id)[0].phoneno
    address = request.POST['address']
    ordereditems = ""
    for pizza in PizzaModel.objects.all():
        pizzaid = pizza.id
        name = pizza.name
        price = pizza.price
        quantity = request.POST.get(str(pizzaid), " ")
        if quantity != "0" and str(quantity) != " ":
            ordereditems = ordereditems + name + " price: " + str(int(quantity)*int(price)) + " quantity : " + str(quantity) + ". "
    OrderModel(username=username, phoneno=phonenum, address=address, ordereditems=ordereditems).save()
    messages.add_message(request, messages.ERROR, "Order Successfuly Placed")
    return redirect('customerpage')


def customerorders(request):
    orders = OrderModel.objects.filter(username=request.user.username)
    username = request.user.username
    context = {'username': username, 'orders': orders}
    return render(request, 'deliveryapp/customerorders.html', context)


def manageorders(request):
    orders = OrderModel.objects.all()
    context = {'orders': orders}
    return render(request, 'deliveryapp/manageorders.html', context)


def acceptorder(request, orderpk):
    order = OrderModel.objects.filter(id=orderpk)[0]
    order.status='Accepted'
    order.save()
    return redirect(request.META['HTTP_REFERER'])


def declineorder(request, orderpk):
    order = OrderModel.objects.filter(id=orderpk)[0]
    order.status='Declined'
    order.save()
    return redirect(request.META['HTTP_REFERER'])