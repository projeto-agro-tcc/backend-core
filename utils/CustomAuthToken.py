from django.contrib.auth.models import Group
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        my_group = Group.objects.filter(user=user).values()
        group_arr = []
        for group in my_group:
            group_arr.append(group['name'])
        return Response({
            'token': token.key,
            'username': user.username,
            'email': user.email,
            'groups': group_arr
        })
