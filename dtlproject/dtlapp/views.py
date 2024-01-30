from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(req):
    username=input("Enter username: ")
    return render(req,"index.html",{"username":username})
    # context={"username":username}
    # return render(req,"index.html",context)


def index(req):
    username= "admin"
    products = ["mobile","laptop","PC", "keyboard"]
    movies = {"kgf":5,"jawan":4,"leo":5}
    fruitdata=fruits()
    context={"username":username, "products":products, 
             "movies":movies, "fruitdata":fruitdata}
    return render(req,"index.html",context)


def fruits():
    fruitlist = ("grapes","mango")
    return fruitlist

def login(req):
    username=input("Enter username")
    todaysdate= datetime.now()
    context={"username":username,'todaysdate':todaysdate}
    return render(req,"login.html",context)