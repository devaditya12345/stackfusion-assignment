from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(APIView):
    def get(self, request):
        queryset = User.objects.all()

        return Response(UserSerializer(queryset, many=True).data)

    def post(self, request):
        serializer_obj = UserSerializer(data=request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data, status=200)
        else:
            return Response(serializer_obj.errors, status=404)
