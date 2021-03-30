from rest_framework import serializers
from .models import (
    Video,
    Audio,
    Text,
    Page,
    Block,
)


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = '__all__'


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'


class BlockSerializer(serializers.ModelSerializer):
    video = VideoSerializer()
    audio = AudioSerializer()
    text = TextSerializer()

    class Meta:
        model = Block
        fields = (
            'video',
            'audio',
            'text',
        )


class PageDetailSerializer(serializers.ModelSerializer):
    blocks = BlockSerializer(many=True)

    class Meta:
        model = Page
        fields = (
            'title',
            'counter',
            'blocks',
        )


class PageListSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()

    class Meta:
        model = Page
        fields = (
            'title',
            'counter',
            'detail_url',
        )

    def get_detail_url(self, page):
        return f'/pages/{page.id}/'
