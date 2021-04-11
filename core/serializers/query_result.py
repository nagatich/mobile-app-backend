from rest_framework import serializers

from core.models import QueryResult

class QueryResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueryResult
        exclude = [
            'id',
            'user'
        ]
