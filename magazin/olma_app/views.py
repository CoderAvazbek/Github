from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Product, Cart


# Create your views here.
def main_page(request):
    product = Product.objects.all()
    context = {'product': product}
    return render(request, 'index.html', context=context)


def note_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'detail.html', {'product': product})




@login_required
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user, product=product) 
    if not created:
        pass
    
    return redirect('home')

@login_required
def cart_list(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    return render(request, 'cart.html', {'cart': cart})

def remove_from_cart(request, id):
    cart = get_object_or_404(Cart, id=id)
    cart.delete()
    return redirect('cart-list')


 

def search(request):
    query = request.GET.get("q")
    products = None
    if query:
        products = Product.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {"products": products, "query": query})