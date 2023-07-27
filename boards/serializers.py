from rest_framework.serializers import ModelSerializer
from .models import Board

class BoardSerializer(ModelSerializer) :
    class Meta :
        model = Board

        fields = "__all__"

        # depth = 1

        # fields = [
        #     "title",
        #     "contents",
        #     "author",
        # ]

        # exclude = [
        #     "modified_at",
        # ]