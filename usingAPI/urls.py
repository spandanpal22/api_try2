from django.contrib import admin
from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework import routers
from APIs import views

"""
router = routers.DefaultRouter()
router.register('users', views.StockList)
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stocks/', views.StockList.as_view()),
    path('stocks/<int:pk>', views.StockList.as_view()),
    path('stock/', views.stock_detail),
    path('stock/<int:pk>', views.stock_detail),
    # path('stocks/', include('rest_framework.urls', namespace='rest_framework')),
]
urlpatterns = format_suffix_patterns(urlpatterns)
