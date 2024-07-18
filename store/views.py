from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Product, Cart, CartItem, Customer, Order
from rest_framework import viewsets
from .serializers import ProductSerializer
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'image', 'price']
    template_name = 'store/product_form.html'
    success_url = '/store/products/'

def test(request):
    return render(request, 'store/test.html')

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'store/product_form.html', {'form': form})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'store/product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect('product_list')
    return render(request, 'store/product_confirm_delete.html', {'product': product})

def products(request):
    return render(request, 'store/products.html')

def register(request):
    return render(request, 'store/register.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'store/home.html')

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')


@login_required
def cart(request):
    cart = Cart.objects.filter(user=request.user).first()
    cart_items = cart.cartitem_set.all() if cart else []
    return render(request, 'store/cart.html', {'cart': cart, 'cart_items': cart_items})

@login_required
def checkout(request):
    cart = Cart.objects.filter(user=request.user).first()
    if cart:
        return render(request, 'store/checkout.html', {'cart': cart})
    else:
        return redirect('cart')

def who(request):
    return render(request, 'store/who.html')

def products_list(request):
    return render(request, 'store/products_list.html')

@login_required
def complete_order(request):
    # Buscar el carrito más reciente para el usuario
    cart = Cart.objects.filter(user=request.user).last()
    if cart:
        cart.completed = True
        cart.save()
        return render(request, 'store/order_completed.html', {'cart': cart})
@login_required
def checkout(request):
    print("Accediendo a la vista checkout")
    cart = Cart.objects.filter(user=request.user, completed=False).first()
    if cart:
        print("Carrito encontrado:", cart)
        return render(request, 'store/checkout.html', {'cart': cart})
    else:
        print("No se encontró carrito, redirigiendo a cart")
        return redirect('cart')


