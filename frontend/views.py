import sweetify
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import never_cache
from django.views.generic import DetailView
from frontend.models import Services

from frontend.models import Carousel

from frontend.models import Department
from frontend.models import Inquiry

from frontend.emailsender import EmailSender

@never_cache
def HomeView(request):
    services = Services.objects.filter(status='Published')[:6]
    department = Department.objects.filter(headline=True, active=True)[:6]
    carousel = Carousel.objects.filter(active=True)
    context = {'services': services, 'carousel': carousel, 'department': department}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        services = request.POST.get('services')
        Inquiries = Inquiry.objects.create(name=name, email=email, phone_number=phone_number, services=services)
        Inquiries.save()
        EmailSender.inquiry(email=email)
        sweetify.success(request, 'Success!', text='Your request has been successfully submitted. One of our agents '
                                                   'will be in touch with you shortly',
                         button='OK',  timer=10000, timerProgressBar='true',)
        # Return success response using Sweet Alert
        return render(request, 'frontend/home.html', {'sweet_alert': True, 'context': context})
    return render(request, 'frontend/home.html', context)


def AboutView(request):
    return render(request, 'frontend/about.html')


def ServicesView(request):
    return render(request, 'frontend/services.html')


def ContactView(request):
    return render(request, 'frontend/contact.html')


def error_404_view(request, exception):
    return render(request, 'frontend/404.html')


class ServiceDetailView(DetailView):
    model = Services
    template_name = "frontend/service_detail.html"

    def post(self, request, slug):
        self.post = get_object_or_404(Services, slug=slug)
        return super().get(request, slug)

    def get(self, request, *args, **kwargs):
        self.main_post = Services.objects.get(slug=kwargs.get('slug'))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["service"] = self.main_post
        context["services"] = Services.objects.filter(status="Published").exclude(slug=self.main_post.slug)[:6]
        return context


class DepartmentDetailView(DetailView):
    model = Department
    template_name = "frontend/department_detail.html"

    def post(self, request, slug):
        self.post = get_object_or_404(Department, slug=slug)
        return super().get(request, slug)

    def get(self, request, *args, **kwargs):
        self.main_post = Department.objects.get(slug=kwargs.get('slug'))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["department"] = self.main_post
        context["departments"] = Department.objects.filter(headline=True, active=True).exclude(
            slug=self.main_post.slug)[:6]
        return context


def all_services(request):
    services = Services.objects.filter(status='Published')
    context = {'services': services, }
    return render(request, 'frontend/all_services.html', context)


def all_departments(request):
    department = Department.objects.filter(active=True)
    context = {'departments': department, }
    return render(request, 'frontend/departments.html', context)


def error_404_view(request, exception):
    return render(request, 'frontend/404.html')


def error_500_view(request):
    return render(request, 'frontend/500.html')


def error_403_view(request, exception):
    return render(request, 'frontend/403.html')
