from rest_framework.viewsets import ModelViewSet
from .models import Books
from django.contrib.auth import get_user_model
from .serializers import BookSerilaizer, UserSerilaizer
from .permissions import CustomPermission

# Create your views here.

class UserViewset(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerilaizer

class BooksViewset(ModelViewSet):
    permission_classes = [CustomPermission,]
    queryset = Books.objects.all()
    serializer_class = BookSerilaizer
