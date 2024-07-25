from django.urls import path
from electronics_shop.apps import ElectrinicsShopConfig
from electronics_shop.views import (ContactsCreateAPIView, ContactsListAPIView, ContactsUpdateAPIView, ContactsRetrieveAPIView, ContactsDeleteAPIView,
                                    ProductsCreateAPIView, ProductsListAPIView, ProductsUpdateAPIView, ProductsRetrieveAPIView, ProductsDeleteAPIView,
                                    FactoryCreateAPIView, FactoryListAPIView, FactoryUpdateAPIView, FactoryRetrieveAPIView, FactoryDeleteAPIView,
                                    RetailNetworkCreateAPIView, RetailNetworkListAPIView, RetailNetworkUpdateAPIView, RetailNetworkRetrieveAPIView, RetailNetworkDeleteAPIView,
                                    IndividualEntrepreneurCreateAPIView, IndividualEntrepreneurListAPIView, IndividualEntrepreneurUpdateAPIView, IndividualEntrepreneurRetrieveAPIView, IndividualEntrepreneurDeleteAPIView)

app_name = ElectrinicsShopConfig.name

urlpatterns = [
    path('contacts_create/', ContactsCreateAPIView.as_view(), name='contacts_create'),
    path('contacts_list/', ContactsListAPIView.as_view(), name='contacts'),
    path('contact_update/<int:pk>/', ContactsUpdateAPIView.as_view(), name='contact_update'),
    path('contact_view/<int:pk>/', ContactsRetrieveAPIView.as_view(), name='contact_view'),
    path('contact_delete/<int:pk>/', ContactsDeleteAPIView.as_view(), name='contact_delete'),

    path('product_create/', ProductsCreateAPIView.as_view(), name='product_create'),
    path('proudcts_list/', ProductsListAPIView.as_view(), name='products'),
    path('product_update/<int:pk>/', ProductsUpdateAPIView.as_view(), name='product_update'),
    path('product_view/<int:pk>/', ProductsRetrieveAPIView.as_view(), name='product_view'),
    path('product_delete/<int:pk>/', ProductsDeleteAPIView.as_view(), name='product_delete'),

    path('factory_create/', FactoryCreateAPIView.as_view(), name='factory_create'),
    path('factories_list/', FactoryListAPIView.as_view(), name='factories'),
    path('factory_update/<int:pk>/', FactoryUpdateAPIView.as_view(), name='factory_update'),
    path('factory_view/<int:pk>/', FactoryRetrieveAPIView.as_view(), name='factory_view'),
    path('factory_delete/<int:pk>/', FactoryDeleteAPIView.as_view(), name='factory_delete'),

    path('retailnetwork_create/', RetailNetworkCreateAPIView.as_view(), name='retailnetwork_create'),
    path('retailnetworks_list/', RetailNetworkListAPIView.as_view(), name='retailnetworks'),
    path('retailnetwork_update/<int:pk>/', RetailNetworkUpdateAPIView.as_view(), name='retailnetwork_update'),
    path('retailnetwork_view/<int:pk>/', RetailNetworkRetrieveAPIView.as_view(), name='retailnetwork_view'),
    path('retailnetwork_delete/<int:pk>/', RetailNetworkDeleteAPIView.as_view(), name='retailnetwork_delete'),

    path('individualentrepreneur_create/', IndividualEntrepreneurCreateAPIView.as_view(), name='individualentrepreneur_create'),
    path('individualentrepreneur_list/', IndividualEntrepreneurListAPIView.as_view(), name='individualentrepreneurs'),
    path('individualentrepreneur_update/<int:pk>/', IndividualEntrepreneurUpdateAPIView.as_view(), name='individualentrepreneur_update'),
    path('individualentrepreneur_view/<int:pk>/', IndividualEntrepreneurRetrieveAPIView.as_view(), name='individualentrepreneur_view'),
    path('individualentrepreneur_delete/<int:pk>/', IndividualEntrepreneurDeleteAPIView.as_view(), name='individualentrepreneur_delete'),
]
