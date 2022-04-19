from django.contrib.auth import (
    authenticate,
    login,
    logout,
)

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


from .models import User
from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    UserProfileSerializer,
    UserChangePasswordSerializer,
    UserListSerializer,
)
from .renderers import UserRenderer
from .myPaginations import MyPageNumberPagination


# Create your views here.

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistrationView(APIView):
    # renderer_classes = (UserRenderer,)

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'msg': 'User created successfully'}, status=status.HTTP_201_CREATED)

        return Response({'msg': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    # renderer_classes = (UserRenderer,)

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                login(request, user)
                return Response({'token': token, 'msg': 'User login successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors': {'non_field_errors': ['Email or Password doesn\'t match']}}, status=status.HTTP_404_NOT_FOUND)
        return Response({'msg': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    # renderer_classes = (UserRenderer,)

    def get(self, request):
        serializer = UserProfileSerializer(instance=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserChangePasswordView(APIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    # renderer_classes = (UserRenderer,)

    def post(self, request):
        serializer = UserChangePasswordSerializer(
            data=request.data, 
            context={'user': request.user
        })

        if serializer.is_valid(raise_exception=True):
            return Response({'msg': 'Password Changed successfully'}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = MyPageNumberPagination
    # renderer_classes = (UserRenderer,)

    


class UserRetrieveView(RetrieveAPIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None):
        user = User.objects.get(id=pk)
        serializer = UserListSerializer(instance=user)

        return Response(serializer.data, status=status.HTTP_200_OK)

