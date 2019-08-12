from abc import ABC

from rest_framework import serializers
from core.models import ComModel


class ComSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField()
    # content = serializers.CharField(max_length=200)
    # created = serializers.DateTimeField()
    # port = serializers.IntegerField()
    # zhubao = serializers.CharField(max_length=200)

    class Meta:
        model = ComModel
        fields = '__all__'
        # fields = ('email', 'content', 'created', 'port')
        # write_only_fields = ('email', 'content', 'created', 'port')
        # extra_kwargs = {'email': {'write_only': True}, 'content': {'write_only': True}, 'port': {'write_only': True}, 'created': {'write_only': True}}

    # def create(self, validated_data):
    #     return ComModel.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.created = validated_data.get('created', instance.created)
    #     instance.port = validated_data.get('port', instance.port)
    #     instance.save()
    #     return instance

    # def validate_content(self, value):
    #     if 'django' not in value.lower():
    #         raise serializers.ValidationError("content post is not about Django")
    #     return value
