from django.shortcuts import redirect, render
from django.contrib import messages
from authentication.models import CustomUser
from author.forms import AuthorForm
from author.models import Author


def create_author(request, author_id=0):
    if request.method == 'GET' and CustomUser.get_by_email(request.user.email).role == 1:
        if author_id == 0:
            form = AuthorForm()
        else:
            author = Author.objects.get(pk=author_id)
            form = AuthorForm(instance=author)
        return render(request, 'author/author_form.html', {'form': form})
    else:
        if author_id == 0:
            form = AuthorForm(request.POST)
        else:
            author = Author.objects.get(pk=author_id)
            form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
    return redirect('home')


def edit_author(request, id):
    error = ""

    if request.method == "POST" and CustomUser.get_by_email(request.user.email).role == 1:
        author = Author.objects.get(pk=id)
        author_updated = AuthorForm(request.POST, instance=author)
        if author_updated.is_valid():
            author_updated.save()
            return redirect("/")
        else:
            error = "Invalid data"

    author = Author.objects.get(pk=id)
    data = {
        'form': AuthorForm(instance=author),
        'error': error
    }

    return render(request, 'author/author_edit.html', data)


def author_id(request, id):
    if not request.user.is_authenticated:
        messages.info(request, "Log in first!")
        return redirect("login")
    if not CustomUser.get_by_email(request.user.email).role == 1:
        messages.info(request, "You don`t have permission!")
        return redirect("home")
    return render(request, "author/get_author_by_id.html", context={"author": Author.get_by_id(id)})


def get_all(request):
    if not request.user.is_authenticated:
        messages.info(request, "Log in first!")
        return redirect("login")
    if not CustomUser.get_by_email(request.user.email).role == 1:
        messages.info(request, "You don`t have permission!")
        return redirect("home")
    return render(request, "author/author.html", {"author": Author.get_all()})


def delete_author(request, id):
    if not request.user.is_authenticated:
        messages.info(request, "Log in first!")
        return redirect("login")
    if not CustomUser.get_by_email(request.user.email).role == 1:
        messages.info(request, "You don`t have permission!")
        return redirect("home")
    Author.delete_by_id(id)
    return redirect('all_author')
