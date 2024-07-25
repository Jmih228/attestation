from electronics_shop.serializers import (ContactsSerializer,
                                          ProductsSerializer,
                                          FactorySerializer,
                                          RetailNetworkSerializer,
                                          IndividualEntrepreneurSerializer,)
from electronics_shop.models import (Product, Contacts, Factory, RetailNetwork, IndividualEntrepreneur)
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from users.permissions import IsActive


class ContactsCreateAPIView(generics.CreateAPIView):
    serializer_class = ContactsSerializer
    permission_classes = [IsAuthenticated, IsActive]


class ContactsListAPIView(generics.ListAPIView):
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    permission_classes = [IsAuthenticated, IsActive]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']


class ContactsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ContactsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ContactsDeleteAPIView(generics.DestroyAPIView):
    queryset = Contacts.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ProductsCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductsSerializer
    permission_classes = [IsAuthenticated, IsActive]


class ProductsListAPIView(generics.ListAPIView):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ProductsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ProductsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ProductsDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class FactoryCreateAPIView(generics.CreateAPIView):
    serializer_class = FactorySerializer
    permission_classes = [IsAuthenticated, IsActive]


class FactoryListAPIView(generics.ListAPIView):
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    permission_classes = [IsAuthenticated, IsActive]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['contacts__country',]


class FactoryUpdateAPIView(generics.UpdateAPIView):
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class FactoryRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class FactoryDeleteAPIView(generics.DestroyAPIView):
    queryset = Factory.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class RetailNetworkCreateAPIView(generics.CreateAPIView):
    serializer_class = RetailNetworkSerializer
    permission_classes = [IsAuthenticated, IsActive]


class RetailNetworkListAPIView(generics.ListAPIView):
    serializer_class = RetailNetworkSerializer
    queryset = RetailNetwork.objects.all()
    permission_classes = [IsAuthenticated, IsActive]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['contacts__country',]


class RetailNetworkUpdateAPIView(generics.UpdateAPIView):
    serializer_class = RetailNetworkSerializer
    queryset = RetailNetwork.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class RetailNetworkRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = RetailNetworkSerializer
    queryset = RetailNetwork.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class RetailNetworkDeleteAPIView(generics.DestroyAPIView):
    queryset = RetailNetwork.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class IndividualEntrepreneurCreateAPIView(generics.CreateAPIView):
    serializer_class = IndividualEntrepreneurSerializer
    permission_classes = [IsAuthenticated, IsActive]


class IndividualEntrepreneurListAPIView(generics.ListAPIView):
    serializer_class = IndividualEntrepreneurSerializer
    queryset = IndividualEntrepreneur.objects.all()
    permission_classes = [IsAuthenticated, IsActive]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['contacts__country',]


class IndividualEntrepreneurUpdateAPIView(generics.UpdateAPIView):
    serializer_class = IndividualEntrepreneurSerializer
    queryset = IndividualEntrepreneur.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class IndividualEntrepreneurRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = IndividualEntrepreneurSerializer
    queryset = IndividualEntrepreneur.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class IndividualEntrepreneurDeleteAPIView(generics.DestroyAPIView):
    queryset = IndividualEntrepreneur.objects.all()
    permission_classes = [IsAuthenticated, IsActive]
