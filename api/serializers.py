from multiprocessing.dummy import JoinableQueue
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models.mango import Mango
from .models.contract import Contract
from .models.bid import Bid
from .models.contract_bid import ContractBid
from .models.user import User

class MangoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mango
        fields = ('id', 'name', 'color', 'ripe', 'owner')

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('id', 'title', 'description', 'deadline', 'jobtype', 'price', 'can_bid', 'tags', 'owner')

class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ('id', 'title', 'contract_ref', 'description', 'bid_amount', 'owner')

class SpecialContractBidSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractBid
        fields = ('__all__')

class ContractBidSerializer(serializers.ModelSerializer):
    contract = ContractSerializer(source='contract_id')
    bid = BidSerializer(source='bid_id')
    class Meta:
        model = ContractBid
        fields = ('id', 'contract', 'bid', 'status')


class UserSerializer(serializers.ModelSerializer):
    # This model serializer will be used for User creation
    # The login serializer also inherits from this serializer
    # in order to require certain data for login
    class Meta:
        # get_user_model will get the user model (this is required)
        # https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#referencing-the-user-model
        model = get_user_model()
        fields = ('id', 'email', 'name', 'is_dev', 'password')
        extra_kwargs = { 'password': { 'write_only': True, 'min_length': 5 } }

    # This create method will be used for model creation
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

class UserRegisterSerializer(serializers.Serializer):
    # Require email, password, and password_confirmation for sign up
    email = serializers.CharField(max_length=300, required=True)
    name = serializers.CharField(max_length=20, required=True)
    is_dev = serializers.BooleanField(default=False)
    password = serializers.CharField(required=True)
    password_confirmation = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        # Ensure password & password_confirmation exist
        if not data['password'] or not data['password_confirmation']:
            raise serializers.ValidationError('Please include a password and password confirmation.')

        # Ensure password & password_confirmation match
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError('Please make sure your passwords match.')
        # if all is well, return the data
        return data

class ChangePasswordSerializer(serializers.Serializer):
    model = get_user_model()
    old = serializers.CharField(required=True)
    new = serializers.CharField(required=True)
