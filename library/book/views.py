from django.core.checks import messages
from django.shortcuts import redirect, render
from authentication.models import CustomUser
from book.forms import BookForm
from book.models import Book
from order.models import Order


def book_form(request, id=0):
    if request.user.is_authenticated and CustomUser.get_by_email(request.user.email).role == 1:
        if request.method == 'GET':
            if id == 0:
                form = BookForm()
            else:
                book = Book.get_by_id(id)
                form = BookForm(instance=book)
            return render(request, 'book/book_edit_or_create.html', {'form': form})
        else:
            if id == 0:
                form = BookForm(request.POST)
            else:
                book = Book.get_by_id(id)
                form = BookForm(request.POST, instance=book)
            if form.is_valid():
                form.save()
    return redirect('books')


def all_books(request):
    if request.user.is_authenticated:
        raw_books = Book.objects.all()
        data = []
        for book in raw_books:
            print(book.authors.all())
            authors = ', '.join([f'{author.name} {author.surname}' for author in book.authors.all()])
            print(authors)
            data.append({'id': book.id,
                         'name': book.name,
                         'description': book.description,
                         'authors': authors,
                         'count': book.count})
        context = {
            'data': data
        }
        return render(request, 'book/books.html', context=context)
    return redirect("login")


def book_info(request, id):
    if request.user.is_authenticated:
        book = Book.objects.get(id=id)
        authors = ', '.join([f'{author.name} {author.surname}' for author in book.authors.all()])
        available = book.count - Order.objects.filter(book=book, end_at=None).count()
        context = {'id': book.id,
                   'name': book.name,
                   'description': book.description,
                   'authors': authors,
                   'count': book.count,
                   'available': available}
        return render(request, 'book/book_form.html', context=context)
    return redirect("login")


def books_ordered_by_user_id(request, id):
    if request.user.is_authenticated and request.user.role == 1:
        if user := CustomUser.get_by_id(id):
            orders = Order.objects.filter(user=user, end_at=None)
            print(orders)
            return render(request, 'book/books_ordered.html', {'data': orders})
        else:
            messages.error(request, 'ERROR! No user found')
    return redirect("books")