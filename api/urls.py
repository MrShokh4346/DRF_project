from rest_framework.routers import SimpleRouter
from .views import UserViewset, BooksViewset

router = SimpleRouter()
router.register(r'users', UserViewset, basename='users')
router.register(r'', BooksViewset, basename='book')

urlpatterns = router.urls