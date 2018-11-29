from django.shortcuts import render

from django.http import HttpResponse


def zone_index(request):
    return HttpResponse("zone index.")


def site_index(request):
    return HttpResponse("site index.")
