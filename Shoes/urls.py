from django.urls import path
from Shoes import views

urlpatterns=[
    path('indexpage/',views.indexpage,name="indexpage"),
    path('Adminpage/',views.Adminpage,name="Adminpage"),
    path('Admin_save/',views.Admin_save,name="Admin_save"),
    path('Admindata/', views.Admindata, name="Admindata"),
    path('editAdmindata/<int:dataid>/', views.editAdmindata, name="editAdmindata"),
    path('updateAdmin/<int:dataid>/', views.updateAdmin, name="updateAdmin"),
    path('deleteAdminData/<int:dataid>/', views.deleteAdminData, name="deleteAdminData"),
    path('category/', views.category, name="category"),
    path('categoryitem/', views.categoryitem, name="categoryitem"),
    path('items/', views.items, name="items"),
    path('edititems/<int:dataid>/', views.edititems, name="edititems"),
    path('updatecategory/<int:dataid>/', views.updatecategory, name="updatecategory"),
    path('deledata/<int:dataid>/', views.deledata, name="deledata"),
    path('adproduct/', views.adproduct, name="adproduct"),
    path('products/', views.products, name="products"),
    path('productview/', views.productview, name="productview"),
    path('editproduct/<int:dataid>/', views.editproduct, name="editproduct"),
    path('updateproduct/<int:dataid>/', views.updateproduct, name="updateproduct"),
    path('deleproduct/<int:dataid>/', views.deleproduct, name="deleproduct"),
    path('loginadmin/', views.loginadmin, name="loginadmin"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('customerlogout/', views.customerlogout, name="customerlogout")

]