from django.contrib import admin
from electronics_shop.models import Factory, RetailNetwork, IndividualEntrepreneur, Contacts, Product


class CityFilter(admin.SimpleListFilter):
    title = 'Фильтр по city'
    parameter_name = 'contacts'
    field_name = 'contacts'

    def lookups(self, request, model_admin):
        queryset = Contacts.objects.all()
        filter_data = set()
        for contact in queryset:
            filter_data.add((contact.city, contact.city))
        return filter_data

    def queryset(self, request, queryset):
        city = self.value()
        if city:
            return queryset.filter(contacts__city=city)
        return queryset.all()


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'contacts', 'creation_time')
    list_filter = ('id', 'creation_time', CityFilter)
    search_fields = ('id', 'creation_time')


@admin.register(RetailNetwork)
class RetailNetworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'factory_supplier', 'individual_entreprereur_supplier', 'provider_debt', 'creation_time')
    list_display_links = ('id', 'factory_supplier', 'individual_entreprereur_supplier')
    list_filter = ('id', 'factory_supplier', 'individual_entreprereur_supplier', 'provider_debt', 'creation_time', CityFilter)
    search_fields = ('id', 'factory_supplier', 'individual_entreprereur_supplier', 'provider_debt', 'creation_time')
    actions = ('pay_off_debt',)

    @admin.action(description='Погасить задолженность перед поставщиком')
    def pay_off_debt(self, request, queryset):
        queryset.update(provider_debt=0)

@admin.register(IndividualEntrepreneur)
class IndividualEntrepreneurAdmin(admin.ModelAdmin):
    list_display = ('id', 'factory_supplier', 'retail_network_supplier', 'provider_debt', 'creation_time')
    list_display_links = ('id', 'factory_supplier', 'retail_network_supplier')
    list_filter = ('id', 'factory_supplier', 'retail_network_supplier', 'provider_debt', 'creation_time', CityFilter)
    search_fields = ('id', 'factory_supplier', 'retail_network_supplier', 'provider_debt', 'creation_time')
    actions = ('pay_off_debt',)

    @admin.action(description='Погасить задолженность перед поставщиком')
    def pay_off_debt(self, request, queryset):
        queryset.update(provider_debt=0)

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'country', 'city', 'street', 'home_number')
    list_filter = ('city',)


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'model', 'release_date')
