from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Contacts(models.Model):

    email = models.EmailField(verbose_name='Электронная почта')
    country = models.CharField(max_length=150, **NULLABLE, verbose_name='Страна')
    city = models.CharField(max_length=150, verbose_name='Город')
    street = models.CharField(max_length=150, **NULLABLE, verbose_name='Улица')
    home_number = models.CharField(max_length=150, **NULLABLE, verbose_name='Номер дома')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.email


class Product(models.Model):

    title = models.CharField(max_length=150, verbose_name='Название продукта')
    model = models.CharField(max_length=150, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода продукта на рынок')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class Factory(models.Model):

    title = models.CharField(max_length=150, verbose_name='Название завода')
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE, verbose_name='Контакты')
    products = models.ManyToManyField(Product, **NULLABLE, verbose_name='Продукты')
    creation_time = models.TimeField(auto_now_add=True, verbose_name='Время создания')
    individual_entreprereur_supplier = models.ForeignKey('IndividualEntrepreneur', **NULLABLE,
                                                         on_delete=models.DO_NOTHING, verbose_name='ИП поставщик')
    retail_network_supplier = models.ForeignKey('RetailNetwork', **NULLABLE,
                                                on_delete=models.DO_NOTHING, verbose_name='Сеть розничной продукции')
    provider_debt = models.FloatField(**NULLABLE, verbose_name='Задолженность перед поставщиком')

    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'

    def __str__(self):
        return self.title


class RetailNetwork(models.Model):

    title = models.CharField(max_length=150, verbose_name='Название сети')
    contacts = models.OneToOneField(Contacts, on_delete=models.CASCADE, verbose_name='Контакты')
    products = models.ManyToManyField(Product, **NULLABLE, verbose_name='Продукты')
    factory_supplier = models.ForeignKey(Factory, **NULLABLE,
                                         on_delete=models.DO_NOTHING, verbose_name='Завод поставщик')
    individual_entreprereur_supplier = models.ForeignKey('IndividualEntrepreneur', **NULLABLE,
                                                         on_delete=models.DO_NOTHING, verbose_name='ИП поставщик')
    provider_debt = models.FloatField(**NULLABLE, verbose_name='Задолженность перед поставщиком')
    creation_time = models.TimeField(auto_now_add=True, verbose_name='Время создания')

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'

    def __str__(self):
        return self.title


class IndividualEntrepreneur(models.Model):

    title = models.CharField(max_length=150, verbose_name='Название ИП')
    contacts = models.OneToOneField(Contacts, on_delete=models.CASCADE, verbose_name='Контакты')
    products = models.ManyToManyField(Product, **NULLABLE, verbose_name='Продукты')
    factory_supplier = models.ForeignKey(Factory, on_delete=models.DO_NOTHING,
                                         **NULLABLE, verbose_name='Завод поставщик')
    retail_network_supplier = models.ForeignKey(RetailNetwork, **NULLABLE,
                                                on_delete=models.DO_NOTHING, verbose_name='Сеть розничной продукции')
    provider_debt = models.FloatField(**NULLABLE, verbose_name='Задолженность перед поставщиком')
    creation_time = models.TimeField(auto_now_add=True, verbose_name='Время создания')

    class Meta:
        verbose_name = 'Индивидуальный предпринематель'
        verbose_name_plural = 'Индивидуальные предпринематели'

    def __str__(self):
        return self.title
