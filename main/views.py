from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MenuItem, Order

def menu(request):
    items = MenuItem.objects.all()
    return render(request, 'orders/menu.html', {'items': items})

@login_required
def create_order(request):
    if request.method == 'POST':
        selected_items = request.POST.getlist('item')
        total_price = sum([float(MenuItem.objects.get(pk=item).price) for item in selected_items])
        order = Order.objects.create(user=request.user, total_price=total_price)
        order.items.add(*selected_items)
        return redirect('order_success')
    return render(request, 'orders/menu.html', {'items': MenuItem.objects.all()})

def order_success(request):
    return render(request, 'orders/order_success.html')
