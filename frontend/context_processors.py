from django.conf import settings

from .models import Department, Services


def Departments(request):
    return {'departments': Department.objects.filter(active=True)[:5]}


def Service(request):
    return {'services': Services.objects.filter(status="Published")[:5]}
