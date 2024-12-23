
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item

def index(request):
    items = Item.objects.all()
    return render(request, "index.html", {"items": items})

def add_item(request):
    if request.method == "POST":
        name = request.POST["name"]
        Item.objects.create(name=name)
        return redirect("index")
    return render(request, "add_item.html")

def edit_item(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == "POST":
        item.name = request.POST["name"]
        item.save()
        return redirect("index")
    return render(request, "edit_item.html", {"item": item})

def delete_item(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == "POST":
        item.delete()
        return redirect("index")
    return render(request, "delete_item.html", {"item": item})
