from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart, Order, previous_order as previous
from my_app.models import product_table
from django.urls import reverse
from django.contrib.auth.models import User
import io
import datetime
from django.http import HttpResponseRedirect, HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template


@login_required
def add_to_cart(request, id):
    product = get_object_or_404(product_table, id=id)
    cart = Cart.objects.filter(user=request.user, product=product).first()
    if cart:
        cart.quantity += 1
        cart.save()
    else:
        cart = Cart(user=request.user, product=product, quantity=1, price=product.price, amount=product.price * 1)
        cart.save()
    messages.success(request, f"{product.product_name} added to your cart.")
    return redirect("cart_detail")

#cart detail with total price and increase decrease functionality
@login_required
def cart_detail(request):
    cart_items = Cart.objects.filter(user=request.user).all()
    total_price = 0
    product_total_quantity = 0
    if cart_items is not None:
        for item in cart_items:
            total_price += item.quantity * item.price
            product_total_quantity += item.quantity
            item.amount = item.quantity * item.price
    
        context = {
            "cart_items": cart_items,
            "total_price": total_price,
            "cart_count": cart_items.count(),
            "product_total_quantity": product_total_quantity,
        }
        return render(request, "cart/cart_detail.html", context)
        cart.save()
    else:
        return render(request, "cart/checkout.html")
    

@login_required
def decrease_quantity(request, id):
    cart_item = get_object_or_404(Cart, id=id)
    cart_item.quantity -= 1
    total_price = cart_item.price * cart_item.quantity
    unit_amount = cart_item.price
    if cart_item.quantity >= 1:
        
        cart_item.save()
        return redirect("cart_detail")
    elif cart_item.quantity < 1:
        cart_item.delete()
        return redirect("cart_detail")
    
    return redirect("cart_detail")

@login_required
def increase_quantity(request, id):
    cart_item = get_object_or_404(Cart, id=id)
    cart_item.quantity += 1
    total_price = cart_item.price * cart_item.quantity
    unit_amount = cart_item.price
    cart_item.save()
    return redirect("cart_detail")

@login_required
def remove_from_cart(request, id):
    cart_item = get_object_or_404(Cart, id=id)
    cart_item.delete()
    return redirect("cart_detail")




@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user).all()
    total_price = 0

    if cart_items is not None:
        for item in cart_items:
            total_price += item.price * item.quantity
        context = {
            "cart_items": cart_items,
            "total_price": total_price,
            "cart_count": cart_items.count()
        }
        return render(request, "cart/cart_detail.html", context)
    else:
        return render(request, "cart/checkout.html")

@login_required
def cart_empty(request):
    return render(request, "cart/cart_empty.html")



@login_required
def confirm_to_pay(request):
    cart_items = Cart.objects.filter(user=request.user).all()
    total_price = 0
    product_total_quantity = 0
    if cart_items is not None:
        for item in cart_items:
            total_price += item.quantity * item.price
            product_total_quantity += item.quantity
            item.amount = item.quantity * item.price
    
        context = {
            "cart_items": cart_items,
            "total_price": total_price,
            "cart_count": cart_items.count(),
            "product_total_quantity": product_total_quantity,
        }
        return render(request, "cart/confirm_to_pay.html", context)
    else:
        return render(request, "cart/cart_detail.html")

# def for after a user payment is successful it will save the order details and the amount into the order table according to the table properties and delete the cart items
@login_required
def order(request):
    total_price = 0
    cart_items = Cart.objects.filter(user=request.user).all()
    created_at = datetime.datetime.now()
    if cart_items is not None:
        for item in cart_items:
            total_price += item.price * item.quantity
            item.amount = item.quantity * item.price
            order = Order(user=request.user, product_names = item.product, products_number = item.quantity, total = total_price, created_at = created_at, amount = item.amount, price = item.price)
            order.save()
            item.delete()
        return render(request, "cart/payment_success.html")

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).all()
    user = previous.objects.filter(user=request.user).all()
    delivered_at = datetime.datetime.now()
    for order in orders:
        if order.order_status == "Delivered":
            user = previous(user = order.user, product_names = order.product_names, products_number = order.products_number, total = order.total, delivered_at = delivered_at, amount = order.amount, price = order.price)
            user.save()
            order.delete()
        
    Context = {
        "orders": orders
    }
    return render(request, "cart/order_list.html", Context)


@login_required
def previous_order(request):
    previous_order = previous.objects.filter(user=request.user).all()
    context = {
        "previous_order": previous_order
    }
    return render(request, "cart/previous_order.html", context)

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

@login_required
def download_invoice(request):
    orders = Order.objects.filter(user=request.user).all()
    user_details = User.objects.get(username=request.user)
    total_price = 0
    for order in orders:
        total_price += order.total
    mydict = {
        "orders": orders,
        "created_at": datetime.datetime.now(),
        "total_price": total_price,
        "user_details": user_details
    }
    pdf = render_to_pdf('cart/invoice.html', mydict)
    return HttpResponse(pdf, content_type='application/pdf')
