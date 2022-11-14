from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from tenant.custom_response import response
from tenant.models import SiteUser
from tenant.serializer import MyTokenObtainPairSerializer, SiteUserSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    ''' Custom JWT Token Obtained Pair View  '''
    serializer_class = MyTokenObtainPairSerializer


class SiteUserView(generics.ListCreateAPIView, generics.UpdateAPIView):
    ''' User view for creating manager , normal user , superadmin user etc  '''
    queryset = SiteUser.objects.filter()
    serializer_class = SiteUserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_object(self):
        return SiteUser.objects.get(email=self.request.user.email)

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(instance=SiteUser.objects.get(email=self.request.user.email))
        return response(serializer.data, status=status.HTTP_200_OK)
