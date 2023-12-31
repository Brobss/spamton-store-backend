from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from uploader.router import router as uploader_router

from uploader import views

from uploader.views import ImageUploadViewSet

from produto import views

from usuario.views import UsuarioViewSet

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from produto.views import (
    CategoriaViewSet,
    ProdutoViewSet,
    FabricanteViewSet,
    CompraViewSet,
)


from usuario.router import router as usuario_router

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"fabricantes", FabricanteViewSet)
router.register(r"produtos", ProdutoViewSet)
router.register(r"compras", CompraViewSet)
router.register(r"usuarios", UsuarioViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include(usuario_router.urls)),
    path("api/media/", include(uploader_router.urls)),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
