from django.urls import path
from electronics_shop.apps import ElectrinicsShopConfig
from electronics_shop.views import (ContactsViewSet, ProductsViewSet, FactoriesViewSet,
                                    RetailNetworkViewSet, IndividualEntrepreneurViewSet)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'contacts', ContactsViewSet, basename='contacts')
router.register(r'products', ProductsViewSet, basename='products')
router.register(r'factories', FactoriesViewSet, basename='factories')
router.register(r'retail_networks', RetailNetworkViewSet, basename='retail_networks')
router.register(r'individual_entrepreneurs', IndividualEntrepreneurViewSet, basename='individual_entrepreneurs')

app_name = ElectrinicsShopConfig.name

urlpatterns = [

] + router.urls
