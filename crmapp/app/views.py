# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from .decorators import unauthenticated_user, allowed_users, admin_only

from .models import *
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def customers_list(request):
    if request.method == 'GET':
        data = User.objects.all()        
        serializer = ProfileSerializer(data, context={'request': request} ,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print('Validation errors:', serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', "DELETE"])
def customer_details(request, pk):

    try:
        customer = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProfileSerializer(customer, context={'request': request})
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProfileSerializer(customer, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
def products_list(request):
    if request.method == 'GET':
        data = Product.objects.all()        
        serializer = ProductSerializer(data, context={'request': request} ,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print('Validation errors:', serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', "DELETE"])
def product_details(request, pk):

    try:
        customer = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductSerializer(customer, context={'request': request})
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProductSerializer(customer, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



# @login_required(login_url='login')
# @admin_only # if customer the redirect to user-page and if admin redirect to view_func
# def home(request):
#     last_five_orders = Purchased.objects.all().order_by('-date_ordered')[:5]
#     orders = Purchased.objects.all()
#     customers = Customer.objects.all()

#     total_customers = customers.count()
#     total_orders = orders.count()

#     delivered = orders.filter(status='Delivered').count()
#     pending = orders.filter(status='Pending').count()

#     context = {
#         'last_five_orders':last_five_orders,
#         'orders':orders,
#         'customers':customers,
#         'total_customers':total_customers,
#         'total_orders':total_orders,
#         'delivered':delivered,
#         'pending':pending
#     }

#     return render(request, 'accounts/dashboard.html', context)

# @login_required
# def profile(request):
#     profile = get_object_or_404(Profile, user=request.user)
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         form = ProfileForm(instance=profile)
#     return render(request, 'profile.html', {'form': form})

# @login_required
# def notifications(request):
#     notifications = Notifications.objects.filter(user=request.user)
#     return render(request, 'notifications.html', {'notifications': notifications})

# @login_required
# def product_list(request):
#     products = Product.objects.filter(admin=request.user)
#     return render(request, 'product_list.html', {'products': products})

# @login_required
# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk, admin=request.user)
#     return render(request, 'product_detail.html', {'product': product})

# @login_required
# def product_create(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.admin = request.user
#             product.save()
#             return redirect('product_list')
#     else:
#         form = ProductForm()
#     return render(request, 'product_form.html', {'form': form})

# @login_required
# def product_update(request, pk):
#     product = get_object_or_404(Product, pk=pk, admin=request.user)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect('product_list')
#     else:
#         form = ProductForm(instance=product)
#     return render(request, 'product_form.html', {'form': form})

# @login_required
# def product_delete(request, pk):
#     product = get_object_or_404(Product, pk=pk, admin=request.user)
#     if request.method == 'POST':
#         product.delete()
#         return redirect('product_list')
#     return render(request, 'product_confirm_delete.html', {'product': product})


