"""
URL configuration for Tasin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from my_app import views
from user_app import views as user_views
from django.conf.urls.static import static
from cart import views as cart_views

app_name = 'my_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index_url'),
    path('index/', views.index,name='index_url'),
    path('product_details/<int:id>', views.product_details,name='product_details_url'),
    path('processors/', views.processors,name='processors_url'),
    path('motherboards/', views.motherboards,name='motherboards_url'),
    path('monitors/', views.monitors,name='monitors_url'),
    path('desktops/', views.desktops,name='desktops_url'),
    path('ram/', views.ram,name='ram_url'),
    path('storage/', views.storage,name='storage_url'),
    path('search/', views.search,name='search_url'),
    path('sort_to_high/', views.sort_to_high,name='sort_to_high_url'),
    path('sort_to_low/', views.sort_to_low,name='sort_to_low_url'),
    path('sort_to_high1/', views.sort_to_high1,name='sort_to_high1'),
    path('sort_to_low1/', views.sort_to_low1,name='sort_to_low1'),
    path('login/', views.login,name='login_url'),
    path('forgot_password/', user_views.forgot_password,name='forgot_password_url'),
    path("register/", user_views.register, name="register_url"),
    path('logout/', views.admin_logout,name='logout_url'),
    path('read/',views.read,name='read_url'),
    path('create/',views.create,name='create_url'),
    path('update/<int:id>',views.update,name='update_url'),
    path('delete/<int:id>',views.delete,name='delete_url'),
    path('about_us/', views.about_us,name='about_us_url'),
]

app_name = 'user_app'

urlpatterns += [
    path('index_user/', user_views.index_user,name='index_user_url'),
    path('dashboard/', user_views.dashboard,name='dashboard_url'),
    path('product_details_user/<int:id>', user_views.product_details_user,name='product_details_user_url'),
    path('processors_user/', user_views.processors_user,name='processors_user_url'),
    path('motherboards_user/', user_views.motherboards_user,name='motherboards_user_url'),
    path('monitors_user/', user_views.monitors_user,name='monitors_user_url'),
    path('desktops_user/', user_views.desktops_user,name='desktops_user_url'),
    path('ram_user/', user_views.ram_user,name='ram_user_url'),
    path('storage_user/', user_views.storage_user,name='storage_user_url'),
    path('about_us_user/', user_views.about_us_user,name='about_us_user_url'),
    path('profile_user/', user_views.profile_user,name='profile_user'),
    path('carousel_page/', views.carousel_page,name='carousel_page'),
    path('carousel_create/', views.carousel_create,name='carousel_create'),
    path('carousel_update/<int:id>', views.carousel_update,name='carousel_update'),
    path('carousel_delete/<int:id>', views.carousel_delete,name='carousel_delete'),
    path('fixed_images/', views.fixed_images,name='fixed_images'),
    path('add_fixed_images/', views.add_fixed_images,name='add_fixed_images'),
    path('delete_fixed_images/<int:id>', views.delete_fixed_images,name='delete_fixed_images'),
    path('manage_orders/', user_views.manage_orders,name='manage_orders'),
    path('manage_orders_item/<int:id>', user_views.manage_orders_item,name='manage_orders_item'),
    path('manage_users/', user_views.manage_users,name='manage_users'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


app_name = 'cart'

urlpatterns += [
    path('add_to_cart/<int:id>', cart_views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:id>', cart_views.remove_from_cart, name='remove_from_cart'),
    path('cart_detail/', cart_views.cart_detail, name='cart_detail'),
    path('increase_quantity/<int:id>', cart_views.increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<int:id>', cart_views.decrease_quantity, name='decrease_quantity'),
    path('checkout/', cart_views.checkout, name='checkout'),
    path('cart_empty/', cart_views.cart_empty, name='cart_empty'),
    path('confirm_to_pay/', cart_views.confirm_to_pay, name='confirm_to_pay'),
    path('order/', cart_views.order, name='order'),
    path('order_list/', cart_views.order_list, name='order_list'),
    path('previous_order/', cart_views.previous_order, name='previous_order'),
    path('download_invoice/', cart_views.download_invoice, name='download_invoice'),
    
]