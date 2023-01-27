from django.shortcuts import render, redirect
from django.db.models import Q
from .models import *
from django import forms
from .forms import *
# Create your views here.

def product_list(request):
    categories = Category.objects.all()
    category = request.GET.get('category')
    products = Product.objects.all()
    products = Product.objects.all()
    products = products.filter(category=category) if category else products
    features = Feature.objects.all()
    feature = request.GET.get('feature')
    search = request.GET.get('search')
    product_id = request.GET.get('product')

    cart_items = CartItem.objects.filter(customer=request.user)
    total_price = sum([item.total_price() for item in cart_items])
    total_quantity = sum([item.quantity for item in cart_items])

    if product_id:
        product = Product.objects.get(pk=product_id)
        cart_item = CartItem.objects.filter(product=product)
        if not cart_item:
            cart_item = CartItem.objects.create(customer=request.user , product=product , quantity=1 )
            cart_item.save
            return redirect('product_list')
        for item in cart_item:
            item.quantity += 1
            item.save()
    products = products.filter(Q(title__icontains=search) | Q(description__icontains=search)) if search else products
    return render(request, 'product_list.html',{ 'cart_items': cart_items, 'total_quantity': total_quantity,
        'total_price':total_price,'products': products, "categories": categories , 'features' : features, "search":search })


def cart(request):
    cart_items = CartItem.object.filter(customer=request.user)
    total_price = sum([item.total_price() for item in cart_items])
    total_quantity = sum([item.quantity for item in cart_items])

    return render(
        request,
        'product_list.html',
        {'cart_items': cart_items, 'total_quantity': total_quantity,
        'total_price':total_price}
    )
def delete_cart_item(request,pk):
    cart_item = CartItem.objects.get(pk=pk).delete()
    return redirect('product_list')

def create_order(request):
    cart_items = CartItem.objects.filter(customer=request.user)
    total_price = sum([item.total_price() for item in cart_items])
    amount = sum([item.quantity for item in cart_items])
    form = OrderForm(request.POST)

    if request.method == 'POST' and form.is_valid():
        order = Order.objects.create(
            address=request.POST.get('address'),
            phone = request.POST.get('phone'),
            total_price=total_price,
            customer=request.user
        )
        for cart_items in cart_items:
            OrderProduct.objects.create(
                order = order,
                product = cart_items.product,
                amount = cart_items.quantity,
                total = cart_items.total_price(),
            )
        cart_items.delete()
        return redirect('product_list')
    return render(request, 'order_creation_page.html',{
        'cart_items': cart_items,
        'total_price': total_price,
        'amount': amount,
        'form': form
    })

def product_detail(request,pk):
    product = Product.objects.get(pk=pk)
    
    # if request.user.is_authenticated():
    #     if not product.view_set.filter(user=request.user).exists():
    #         product.view_set.create(user=request.user)
        
    return render(request, 'product_detail.html',{'product': product})

def rate_product(request, pk):
    product = Product.objects.get(pk=pk)
    reviews = Review.objects.filter(product=product)

    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.product = product
            rating.save()
            return redirect('rate_product',pk=pk)
    form = RateForm()
    return render(request, 'rate.html',{'form': form , 'product': product , 'reviews': reviews})