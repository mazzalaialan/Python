from django.contrib import admin
from django.urls import path
from .views import adminloginview, authenticateadmin, adminhomapeview, logoutadmin, addpizza, deletepizza, homepageview, signupuser, userloginview, authenticateuser, customerwelcomeview, logoutuser, placeorder, customerorders, manageorders, acceptorder, declineorder

urlpatterns = [
    path('admin/', adminloginview, name='adminloginpage'),
    path('adminauthenticate/', authenticateadmin),
    path('admin/homepage/', adminhomapeview, name='adminhomepage'),
    path('adminlogout/', logoutadmin),
    path('addpizza/', addpizza),
    path('deletepizza/<int:pizzapk>/', deletepizza),
    path('', homepageview, name='homepage'),
    path('signupuser/', signupuser),
    path('userlogin/', userloginview, name='userloginpage'),
    path('userauthenticate/', authenticateuser),
    path('userlogout/', logoutuser),
    path('customer/welcome/', customerwelcomeview, name='customerpage'),
    path('placeorder/', placeorder),
    path('customerorders/', customerorders),
    path('manageorders/', manageorders),
    path('acceptorder/<int:orderpk>/', acceptorder),
    path('declineorder/<int:orderpk>/', declineorder),
]