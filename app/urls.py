from django.urls import path
from app import views

urlpatterns = [
    path('', views.StoreView.as_view(), name='store'),
    path('store/<int:pk>/', views.StaffView.as_view(), name='staff'),
    path('calendar/<int:pk>/', views.CalendarView.as_view(), name='calendar'), # 追加
    path('calendar/<int:pk>/<int:year>/<int:month>/<int:day>/', views.CalendarView.as_view(), name='calendar'), # 追加
    path('booking/<int:pk>/<int:year>/<int:month>/<int:day>/<int:hour>/', views.BookingView.as_view(), name='booking'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
]
