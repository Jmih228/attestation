from rest_framework.serializers import ValidationError


class ProviderDebtValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):

        tmp_val = dict(value).get(self.field)
        if tmp_val:
            raise ValidationError('Обновление задолженности перед поставщиком запрещено')
