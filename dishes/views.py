from django.shortcuts import render
from .models import Category, Dish
from django.http.response import JsonResponse
from rest_framework import status

def get_categories(request):
    try:
        categories=Category.objects.all()
        return JsonResponse([category.serialize() for category in categories],safe=False)
    except Exception as ex:
        return JsonResponse({'message':f'The server thrown an exception: {ex}'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
def get_dishes(request):
    try:
       category_id=request.GET.get('category_id',None)
       if category_id is None:
         return JsonResponse({'message':f'category_id must be provide in query params'},status=status.HTTP_406_NOT_ACCEPTABLE,safe=False)
       number=int(category_id)
       category=Category.objects.get(id=number)
       dishes=Dish.objects.filter(category=category)
       return JsonResponse([dish.serialize() for dish in dishes],safe=False)
    except Category.DoesNotExist:
        return JsonResponse({'message':f'category_id does not exist'},status=status.HTTP_404_NOT_FOUND,safe=False)
    except Exception as ex:
        return JsonResponse(f'{ex}',status=status.HTTP_500_INTERNAL_SERVER_ERROR,safe=False)