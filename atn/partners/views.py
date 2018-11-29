from django.shortcuts import render

from django.http import HttpResponse


def client_index(request):
    return HttpResponse("client index.")


def customer_index(request):
    return HttpResponse("customer index.")
