from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from .todo import TodoForm
from .models import Todo


def render_window(request: HttpRequest, page: dict[str]):
    return render(request, "index.html", page)


def index(request: HttpRequest):
    item_list = Todo.objects.order_by("-date")
    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
    }

    if request.method == "POST":
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()

            page["forms"] = form
            return render_window(request, page)

    return render_window(request, page)


def remove(request: HttpRequest, item_id: int):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect("/")
