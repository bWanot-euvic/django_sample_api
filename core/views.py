
from rest_framework.response import Response
from rest_framework import generics, status,  authentication, permissions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
    token = super().get_token(user)
    return token

class MyTokenObtainPairView(generics.GenericAPIView):

  serializer_class = MyTokenObtainPairSerializer
  www_authenticate_realm = "api"

  def get(self, request):
    serializer = self.get_serializer(data={
      'username': 'guest', 
      'password': 'guest'
      })

    serializer.is_valid(raise_exception=True)
    access = serializer.validated_data['access']
    return Response({'access': access}, status=status.HTTP_200_OK)

class LatestArticleAPIView(APIView):
  authentication_classes = [JWTAuthentication, authentication.SessionAuthentication]
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    data = {
      "slug": '675900e8-c149-0486-ad49-f7614cdc24b1',
      "title": 'Lorem ipsum',
      "description": 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua',
      "body": 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?',
      "tagList": ['dolores', 'nesciunt', 'accusantium', 'perspiciatis'],
      "createdAt": '2023-07-025T12:45:17.090Z',
      "updatedAt":'2023-08-08T08:23:05.090Z',
      "favorited":False,
      "favoritesCount" : 0,
      "author": {
        'username':'Bartosz Wanot', 
        'bio':'Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.', 
        'image': 'https://cdn.iconscout.com/icon/free/png-256/free-avatar-370-456322.png', 
        'following': False
      },
    }
    return Response({'success': True, "data": data}, status=status.HTTP_200_OK)