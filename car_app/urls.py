from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import help_request
from django.urls import path
from .views import register_view, login_view, logout_view
from .views import privacy_policy, terms_conditions



urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('booking', views.booking, name='booking'),
    path('technicians', views.technicians, name='technicians'),
    path('testimonials', views.testimonials, name='testimonials'),
    path('badrequest', views.badrequest, name='badrequest'),
    path('contact', views.contact, name='contact'),

    path('service/book/', views.book_service, name='book_service'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
    path('subscribe/', views.subscribe, name='subscribe'),

    path("help-request/", help_request, name="help_request"),

    
     #Authentication 
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),


    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('terms-conditions/', terms_conditions, name='terms_conditions'),

    

    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)