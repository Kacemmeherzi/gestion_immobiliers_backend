from django.urls import path
from .views import predict_price

urlpatterns = [
    path('predict-price/', predict_price, name='predict_price'),
]