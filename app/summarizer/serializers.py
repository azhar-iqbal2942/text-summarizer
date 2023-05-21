from rest_framework import serializers


class TextSummarizerSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=200)
    summary_length = serializers.IntegerField(min_value=20)
