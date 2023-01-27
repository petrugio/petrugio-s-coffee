from . import views
from django.urls import path

urlpatterns = [
    path("", views.testimonial_list, name="testimonials"),
    # path('<slug:slug>/', views.testimonial_detail,
    #      name='testimonial_detail'),
    path('add/', views.add_testimonial, name='add_testimonial'),
]
