from rest_framework.viewsets import ModelViewSet, ViewSet
from user.models import User
from rooms.models import Room
from api.serializers.userserializer import UserSerializer, RegisterSerializer, LoginSerialier
from api.serializers.roomserializer import RoomSerializer 
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken,TokenError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action

class UserViewSet(ModelViewSet):

    http_method_names =['post', 'patch', 'get', 'put']
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    serializer_class = UserSerializer
    querySet = User.objects.all()

    def get_object(self):
        user = User.objects.get_object_by_public_id(self.kwargs['pk'])
        return user


    @action(detail=True, methods=['post'])
    def book_room(self,request, pk=None):
        user = self.get_object()

        try:
            room_data = request.data
            room_data['user'] = user.id
            serializer = RoomSerializer(data=room_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['get'])
    def get_rooms(self, request, pk=None):
        try:
            room_data = Room.objects.all()
            serializer = RoomSerializer(room_data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":"No records found"}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=False, methods=['get'])
    def get_room(self, request, pk=None):
        id = request.data.get('id')
        if id :
            
            room = Room.objects.get(id=id)
            serializer = RoomSerializer(room)
            # serializer.is_valid(raise_exception=True)
            # print(serializer.data)
            return Response({"message":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"error"})
        
        



class RegisterViewSet(ViewSet):

    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def create(self, request):
        request.data['password'] =  make_password(request.data['password'])
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'user':serializer.data}, status=status.HTTP_201_CREATED)
    

class LoginViewSet(ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    serializer_class = LoginSerialier

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            return InvalidToken(e)
        except Exception as e:
            return Response({"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
