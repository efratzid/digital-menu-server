from django.urls import path
from . import views

urlpatterns = [
    path('categories', views.get_categories),
    path('dishes', views.get_dishes),
    # path('dishes/<int:id>', views.get_dishes().as_view()),
]