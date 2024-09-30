from electronics_shop.serializers import (ContactsSerializer,
                                          ProductsSerializer,
                                          FactorySerializer,
                                          RetailNetworkSerializer,
                                          IndividualEntrepreneurSerializer,)
from electronics_shop.models import (Product, Contacts, Factory, RetailNetwork, IndividualEntrepreneur)
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from users.permissions import IsActive


class ContactsViewSet(viewsets.ModelViewSet):
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    permission_classes = [IsAuthenticated, IsActive]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']


class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class FactoriesViewSet(viewsets.ModelViewSet):
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    permission_classes = [IsAuthenticated, IsActive]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['contacts__country',]


class RetailNetworkViewSet(viewsets.ModelViewSet):
    serializer_class = RetailNetworkSerializer
    queryset = RetailNetwork.objects.all()
    permission_classes = [IsAuthenticated, IsActive]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['contacts__country',]


class IndividualEntrepreneurViewSet(viewsets.ModelViewSet):
    serializer_class = IndividualEntrepreneurSerializer
    queryset = IndividualEntrepreneur.objects.all()
    permission_classes = [IsAuthenticated, IsActive]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['contacts__country',]
