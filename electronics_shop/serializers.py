from rest_framework.serializers import ModelSerializer, SerializerMethodField
from electronics_shop.models import Contacts, Product, Factory, RetailNetwork, IndividualEntrepreneur
from electronics_shop.validators import ProviderDebtValidator


class ContactsSerializer(ModelSerializer):

    class Meta:
        model = Contacts
        fields = '__all__'


class ProductsSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class FactorySerializer(ModelSerializer):
    country = SerializerMethodField()
    validators = [ProviderDebtValidator(field='provider_debt')]

    class Meta:
        model = Factory
        fields = ('title', 'contacts', 'products', 'provider_debt', 'creation_time', 'country')

    def get_country(self, instance):
        return instance.contacts.country


class RetailNetworkSerializer(ModelSerializer):
    country = SerializerMethodField()
    validators = [ProviderDebtValidator(field='provider_debt')]

    class Meta:
        model = RetailNetwork
        fields = ('title', 'contacts', 'products', 'factory_supplier',
                  'individual_entreprereur_supplier', 'provider_debt', 'creation_time', 'country')

    def get_country(self, instance):
        return instance.contacts.country


class IndividualEntrepreneurSerializer(ModelSerializer):
    country = SerializerMethodField()
    validators = [ProviderDebtValidator(field='provider_debt')]

    class Meta:
        model = IndividualEntrepreneur
        fields = ('title', 'contacts', 'products', 'factory_supplier',
                  'retail_network_supplier', 'provider_debt', 'creation_time', 'country')

        def get_country(self, instance):
            return instance.contacts.country
