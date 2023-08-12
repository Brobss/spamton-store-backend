from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from produto import views

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from produto.views import (
    CategoriaViewSet,
    ProdutoViewSet,
    ImagemViewSet,
    FabricanteViewSet,
)

from usuario.router import router as usuario_router

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"produtos", ProdutoViewSet)
router.register(r"imagens", ImagemViewSet)
router.register(r"fabricantes", FabricanteViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include(usuario_router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
