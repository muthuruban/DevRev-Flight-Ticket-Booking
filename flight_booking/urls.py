from django.urls import path
from mainapp import views

app_name = 'mainapp'

urlpatterns = [
    #
    path('logins/login_portal/', views.login_portal, name='login_portal'),

    # User Use Cases
    path('', views.index, name='index'),
    path('user/signup/', views.user_signup, name='user_signup'),
    path('user/login/', views.user_login, name='user_login'),
    path('user/logout/', views.user_logout, name='user_logout'),
    path('flight/search/', views.flight_search, name='flight_search'),
    path('flight/<int:flight_id>/booking/', views.flight_booking, name='flight_booking'),
    path('my/bookings/', views.my_bookings, name='my_bookings'),

    # path('flight/<int:flight_id>/booking/', views.book_ticket, name='book_ticket'),

    # Admin Use Cases
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/add_flight/', views.add_flight, name='add_flight'),
    path('admin/remove_flight/<int:flight_id>/', views.remove_flight, name='remove_flight'),
    path('logout/', views.user_logout, name='logout'),

    # Bookings
    path('flight/<int:flight_id>/booking/make_payment/', views.make_payment, name='make_payment'),
    path('flight/<int:flight_id>/booking/payment_status/', views.payment_status, name='payment_status'),
    path('booking/cancel_ticket/<int:booking_id>/', views.cancel_ticket, name='cancel_ticket'),
    path('booking/<int:booking_id>/view_ticket/',views.view_ticket, name='view_ticket'),
]
