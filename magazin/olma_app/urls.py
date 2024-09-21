from django.urls import path
from .views import main_page, note_detail, add_to_cart, cart_list, remove_from_cart, search

urlpatterns = [
    path('', main_page, name='home'),
    path('<int:id>/', note_detail, name='note_detail'),
    path('add_cart/<int:id>/', add_to_cart, name='add-to-cart'),
    path('cart/', cart_list, name='cart-list'),
    path('delete_cart/<int:id>/', remove_from_cart, name='delete-cart'),

     path('search/', search, name='search')
]
