from django.urls import path
from ShoesWebpage import views

urlpatterns=[
    path('', views.mainpage, name="mainpage"),
    path('contactpage/', views.contactpage, name="contactpage"),
    path('contactview/', views.contactview, name="contactview"),
    path('Allproduct/', views.Allproduct, name="Allproduct"),
    path('singleproduct/<itemcatg>', views.singleproduct, name="singleproduct"),
    path('prodetails/<int:dataid>', views.prodetails, name="prodetails"),
    path('login/', views.login, name='login'),
    path('loginsave/', views.loginsave, name='loginsave'),
    path('logoutfn/', views.logoutfn, name='logoutfn'),
    path('customerlogin/', views.customerlogin, name='customerlogin'),
    path('contact_save/', views.contact_save, name="contact_save"),
    path('cart/', views.cart, name="cart"),
    path('cartview/',views.cartview,name='cartview'),
    path('deleteitem/<int:dataid>', views.deleteitem, name='deleteitem')

]