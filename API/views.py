from rest_framework import viewsets
from API import serializers, models
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# ------- Model Serializer ------


class StudentViewset(viewsets.ModelViewSet):
    serializer_class = serializers.StudentSerializer
    queryset = models.Student.objects.all()

    #  ------ Basic Authentication ------
    authentication_classes = [BasicAuthentication]
    # By default permission_classes = [AllowAny]
    permission_classes = [IsAuthenticated]

# AllowAny -> Anyone can access the API
# IsAuthenticated -> User, Admin and Superuser can login
# IsAdminUser -> Only Staff user(Admin) or Superuser can access the API
# IsAuthenticatedOrReadOnly -> Authenticated user can change, Non-authenticated user can only read the API
# DjangoModelPermissions -> We can control in admin panel that which user can user either of the GET, POST, PUT, PATCH, DELETE methods in the Viewset
# DjangoModelPermissionsOrAnonReadOnly -> same as DjangoModelPermissions, but allows unauthenticated user to read-only the API
