from django.contrib.auth import login as loginr, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import carousels,product_table, fixed_images as f, about_us as about
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages


# Create your views here.

def index(request):
    Context={
        'datas':product_table.objects.all(),
        'carousels':carousels.objects.order_by('?'),
        'fixed_images':f.objects.all(),
    }
    return render(request,"index.html",Context)

def search(request):
    query = request.GET['query']
    datas = product_table.objects.filter(product_name__icontains=query)
    Context={
        'datas':datas
    }
    return render(request,"search.html",Context)

def product_details(request,id):
    products=product_table.objects.get(id=id)
    Context={
        'products':products
    }
    return render(request,"product_details.html",Context)

def processors(request):
    Context={
        'datas':product_table.objects.filter(category='processors')
    }
    return render(request,"products.html",Context)

def motherboards(request):
    Context={
        'datas':product_table.objects.filter(category='motherboards')
    }
    return render(request,"products.html",Context)

def monitors(request):
    Context={
        'datas':product_table.objects.filter(category='monitors')
    }
    return render(request,"products.html",Context)

def desktops(request):
    Context={
        'datas':product_table.objects.filter(category='desktops')
    }
    return render(request,"products.html",Context)

def ram(request):
    Context={
        'datas':product_table.objects.filter(category='ram')
    }
    return render(request,"products.html",Context)

def storage(request):
    Context={
        'datas':product_table.objects.filter(category='storage')
    }
    return render(request,"products.html",Context)

def sort_to_high(request):
    datas = product_table.objects.values().all().order_by('-price')
    Context={
        'datas':datas,
        'carousels':carousels.objects.order_by('?'),
        'fixed_images':f.objects.all(),
    }
    return render(request,"index.html",Context)

def sort_to_low(request):
    datas = product_table.objects.values().all().order_by('price')
    Context={
        'datas':datas,
        'carousels': carousels.objects.order_by('?'),
        'fixed_images': f.objects.all(),
    }
    return render(request,"index.html",Context)

# sort_to_high for products.html
def sort_to_high1(request):
    category = product_table.request.GET.get('category')
    Context={
        'datas':product_table.objects.order_by('-price').filter(category=category)
    }
    return render(request,"products.html",Context)

# sort_to_low for products.html
def sort_to_low1(request):
    category = product_table.request.GET.get('category')
    Context={
        'datas':product_table.objects.order_by('price').filter(category=category)
    }
    return render(request,"products.html",Context)


def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=name, password=password)
        if user is not None:
            loginr(request, user)
            if user.is_superuser:
                return redirect('dashboard_url')
            else:
                return redirect('index_user_url')
        else:
            messages.error(request, 'Invalid Username or password')
            return render(request,"login.html")
    elif request.method == 'GET':
        return render(request,"login.html")




@login_required 
def admin_logout(request):
    logout(request)
    return render(request,"login.html")

@user_passes_test(lambda u: u.is_superuser)
def read(request):
    Context={
        'datas':product_table.objects.all()
    }
    count=product_table.objects.all().count()
    return render(request,"read.html",Context)

@user_passes_test(lambda u: u.is_superuser)
def create(request):
    if request.method=='POST':
        product_name = request.POST.get('product_name','')
        description = request.POST.get('description','')
        price = request.POST.get('price','')
        category = request.POST.get('category','')
        photo = request.FILES['photo']
        user = product_table(product_name=product_name,description=description,price=price,photo=photo, category=category)
        user.save()
        return redirect('read_url')
    elif request.method=='GET':
        return render(request,"create.html")

@user_passes_test(lambda u: u.is_superuser)
def update(request,id):
    user_data = product_table.objects.get(id=id)
    if request.method=='POST':
        user_data.product_name = request.POST.get('product_name','')
        user_data.description = request.POST.get('description','')
        user_data.price = request.POST.get('price','')
        user_data.category = request.POST.get('category','')
        user_data.photo = request.FILES['photo']
        user_data.save()
        return redirect('read_url')
    elif request.method=='GET':
        Context={
            'datas':user_data,
        }
        return render(request,"update.html",Context)

@user_passes_test(lambda u: u.is_superuser)
def delete(request,id):
    product_table.objects.get(id=id).delete()
    return redirect('read_url')


@user_passes_test(lambda u: u.is_superuser)
def carousel_page(request):
    Context={
        'carousels':carousels.objects.all()
    }
    return render(request,"carousel.html",Context)


@user_passes_test(lambda u: u.is_superuser)
def carousel_create(request):
    if request.method=='POST':
        title = request.POST.get('title','')
        photo = request.FILES['photo']
        user = carousels(title=title, photo=photo)
        user.save()
        return redirect('carousel_page')
    elif request.method=='GET':
        return render(request,"create_carousel.html")

@user_passes_test(lambda u: u.is_superuser)
def carousel_update(request,id):
    user_data = carousels.objects.get(id=id)
    if request.method=='POST':
        user_data.title = request.POST.get('title','')
        user_data.photo = request.FILES['photo']
        user_data.save()
        return redirect('carousel_page')
    elif request.method=='GET':
        Context={
            'datas':user_data
        }
        return render(request,"carousel_update.html",Context)

@user_passes_test(lambda u: u.is_superuser)
def carousel_delete(request,id):
    carousels.objects.get(id=id).delete()
    return redirect('carousel_page')

@user_passes_test(lambda u: u.is_superuser)
def fixed_images(request):
    fixed_images = f.objects.all()
    Context={
        'fixed_images': fixed_images
    }
    return render(request,"fixed_images.html",Context)

@user_passes_test(lambda u: u.is_superuser)
def add_fixed_images(request):
    if request.method=='POST':
        photo = request.FILES['photo']
        title = request.POST.get('title','')
        user = f(photo=photo, title=title)
        user.save()
        return redirect('fixed_images')
    elif request.method=='GET':
        return render(request,"add_fixed_images.html")
    
@user_passes_test(lambda u: u.is_superuser)
def delete_fixed_images(request,id):
    f.objects.get(id=id).delete()
    return redirect('fixed_images')

def about_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        user = about(name=name, email=email, message=message)
        user.save()
        return redirect('index_url')
    elif request.method == 'GET':
        return render(request,"about_us.html")
    return render(request,"about_us.html")