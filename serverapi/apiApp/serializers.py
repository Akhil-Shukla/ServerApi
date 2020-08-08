from rest_framework import serializers,fields
from .models import *


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    brand_name=serializers.CharField(source='brand_id.name')
    brand_image=fields.FileField(source='brand_id.banner')
    store_image=fields.FileField(source='category_id.store_id.image')
    store_name=serializers.CharField(source='category_id.store_id.name')
    class Meta:
        model = Product
        fields = ('url', 'price','serial_number','product_image','brand_name','brand_image','store_image','store_name')

class BrandsSerializer(serializers.HyperlinkedModelSerializer):
    banner = fields.FileField(source='Brands.banner')

    class Meta:

        model=Brands
        fields=(
            'url',
            'name',
            'banner'
        )
class userSerializer(serializers.ModelSerializer):
    def __init__(self,email,password):
        super(userSerializer, self).__init__()
        self.email=email
        self.password=password
        self.email=serializers.EmailField(source='User.email')
        self.password=serializers.CharField(source='User.password')

    class Meta:
        model=Users
        fields=(
            'url',
            'email',
            'password'
        )

    def validate(self, data):
        email = data['email']
        password = data['password']

        errmsg = ''
        if not email:
            errmsg = str(('Current email must be given'))
        else:
            if not password:
                errmsg = ('Current password is incorrect')

        if errmsg:
            raise serializers.ValidationError(errmsg)

        return data