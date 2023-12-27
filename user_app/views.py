from django.contrib.auth import login as loginr, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from my_app.models import product_table, carousels, fixed_images as f, about_us
from django.contrib.auth import forms
from django.contrib import messages
from user_app.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from cart.models import Cart, Order
from .models import Profile, User
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def forgot_password(request):
    return render(request, 'forgot_password.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # Save user to Database
            username = form.cleaned_data.get('username') # Get the username that is submitted
            messages.success(request, f'Your account has been created! You are now able to log in') # Show sucess message when account is created
            return redirect('login_url') # Redirect user to Login page
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    total_products=product_table.objects.all().count()
    total_users = Profile.objects.all().count()
    total_orders = Order.objects.all().count()
    total_sales = Order.objects.filter(order_status='Delivered').count()
    orders=Order.objects.all().order_by('-id').filter(order_status='Pending')
    contacts = about_us.objects.all().order_by('-id')

    Context = {
        'total_products': total_products,
        'total_users': total_users,
        'total_orders': total_orders,
        'total_sales': total_sales,
        'orders': orders,
        'contacts': contacts
    }
    

    return render(request, 'dashboard.html', Context)

@user_passes_test(lambda u: u.is_superuser)
def manage_orders(request):
    orders = Order.objects.all().order_by('-id')
    return render(request, 'manage_orders.html', {'orders': orders})

@user_passes_test(lambda u: u.is_superuser)
def manage_orders_item(request, id):
    order = Order.objects.get(id=id)
    if request.method == 'POST':
        order.order_status = request.POST.get('order_status', '')
        order.save()
        return redirect('manage_orders')
    return render(request, 'manage_orders_item.html', {'order': order})

@user_passes_test(lambda u: u.is_superuser)
def manage_users(request):
    users = User.objects.all().order_by('-id')
    return render(request, 'manage_users.html', {'users': users})


@login_required
def index_user(request):
    Context={
        'datas':product_table.objects.all(),
        'carousels':carousels.objects.order_by('?'),
        'fixed_images':f.objects.all(),
    }
    return render(request,"index_user.html",Context)


@login_required
def product_details_user(request,id):
    products=product_table.objects.get(id=id)

    if request.method == "POST":
        messages.success(request, f"{products.name} added to your cart.")
        return redirect("cart:add_to_cart", product_id=product_table.id)

    Context={
        'products':products
    }
    return render(request,"product_details_user.html",Context)

@login_required
def processors_user(request):
    Context={
        'datas':product_table.objects.filter(category='processors')
    }
    return render(request,"products_user.html",Context)

@login_required
def motherboards_user(request):
    Context={
        'datas':product_table.objects.filter(category='motherboards')
    }
    return render(request,"products_user.html",Context)

@login_required
def monitors_user(request):
    Context={
        'datas':product_table.objects.filter(category='monitors')
    }
    return render(request,"products_user.html",Context)

@login_required
def desktops_user(request):
    Context={
        'datas':product_table.objects.filter(category='desktops')
    }
    return render(request,"products_user.html",Context)

@login_required
def ram_user(request):
    Context={
        'datas':product_table.objects.filter(category='ram')
    }
    return render(request,"products_user.html",Context)

@login_required
def storage_user(request):
    Context={
        'datas':product_table.objects.filter(category='storage')
    }
    return render(request,"products_user.html",Context)

@login_required
def about_us_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        user = about_us(name=name, email=email, message=message)
        user.save()
        return redirect('index_url')
    elif request.method == 'GET':
        return render(request,"about_us_user.html")
    return render(request,"about_us_user.html")

@login_required
def sort_to_high(request):
    Context={
        'datas':product_table.objects.order_by('-price')
    }
    return render(request,"index_user.html",Context)

@login_required
def sort_to_low(request):
    Context={
        'datas':product_table.objects.order_by('price')
    }
    return render(request,"index_user.html",Context)

#get the profile details of the user and redirect to the profile page
@login_required
def profile_user(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile_user') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile_user.html', context)

