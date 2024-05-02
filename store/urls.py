from django.contrib import admin
from django.urls import path
from .views.home import Index , store
from .views.signup import Signup
from .views.vendor import Vendor

from .views.otp import Otp
#from .views.otp import Otp_verify

#from .views import OTPVerificationView
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),

    path('signup', Signup.as_view(), name='signup'),
    path('vendor', Vendor.as_view(), name='vendor'),
    path('otp', Otp.as_view(), name='otp'),
    #path('otp/', OTPVerificationView.as_view(), name='otp_verification'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),

]
admin.site.site_header = "PetsGet"
admin.site.site_title = "PetsGet Portal"
admin.site.index_title = "PetsGet Portal"