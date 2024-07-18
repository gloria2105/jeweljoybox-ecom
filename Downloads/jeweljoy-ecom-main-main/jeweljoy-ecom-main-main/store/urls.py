from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from .views import (
    ProductViewSet, ProductListView, ProductCreateView, home, test,
    product_detail, product_create, product_update, product_delete,
    products, register, login_view, logout_view, add_to_cart, cart, checkout, who, complete_order  # Asegúrate de importar complete_order
)

router = DefaultRouter()
router.register(r'products-api', ProductViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('home/', views.home, name='home'),
    path('test/', test, name='test'),
    path('productos/', views.products, name='productos'),
    path('products-list/', views.products_list, name='products-list'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('complete_order/', complete_order, name='complete_order'),  # Ruta para completar el pedido
    path('api/', include(router.urls)),
    path('who/', views.who, name='who'),
]
