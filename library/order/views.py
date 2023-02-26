import datetime
from django.shortcuts import render, redirect
from authentication.models import CustomUser
from book.models import Book
from order.forms import OrderForm
from order.models import Order


def order_form(request, id):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == 'GET':
            order = Order.get_by_id(id)
            form = OrderForm(instance=order)
            return render(request, 'order/order_edit.html', {'form': form})
        else:
            order = Order.get_by_id(id)
            form = OrderForm(request.POST, instance=order)
            if form.is_valid():
                form.save()
    return redirect('all_orders')


def order_book(request, id):
    if request.user.is_authenticated:
        print(request.user)
        user = CustomUser.objects.get(id=request.user.id)
        book = Book.objects.get(id=id)
        today = datetime.datetime.now()
        planed_date = today + datetime.timedelta(days=14)
        order = Order.create(user, book, plated_end_at=planed_date)
        print(order)
        return render(request, 'order/order_created.html')
    return redirect("login")


def close_order(request, id):
    if request.user.is_authenticated and request.user.role == 1:
        order = Order.objects.get(id=id)
        order.end_at = datetime.datetime.now()
        order.save()
        return redirect("home")
    return redirect("home")


def all_orders(request):
    if request.user.is_authenticated and request.user.is_staff:
        orders = Order.objects.all()
        context = {
            'data': orders
        }
        return render(request, 'order/all_orders.html', context=context)
    elif request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user)
        context = {
            'data': orders
        }
        return render(request, 'order/all_orders.html', context=context)


def my_orders(request):
    if request.user.is_authenticated:
        print(request.user)
        user = CustomUser.objects.get(id=request.user.id)
        orders = Order.objects.filter(user=user)
        context = {
            'data': orders
        }
        return render(request, 'order/my_orders.html', context=context)
    return redirect("home")
