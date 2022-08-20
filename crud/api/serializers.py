from rest_framework import serializers
from crud.models import Account


class AccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['name', 'surname', 'email', 'date', 'application_aim']

