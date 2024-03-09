from django.urls import path
from .views import *


app_name = 'frontend'

urlpatterns = [
    path("", HomeView, name="home"),
    path("about", AboutView, name="about"),
    path("services", ServicesView, name="services"),
    # path("faq", faq_view, name="faq"),
    path("contact", ContactView, name="contact"),
    path("services/<slug>", ServiceDetailView.as_view(), name='service_detail'),
    path("department/<slug>", DepartmentDetailView.as_view(), name='department_detail'),
    path("denmark-services", all_services, name="all_services"),
    path("denmark-departments", all_departments, name="all_departments"),
]