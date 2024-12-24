from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, CommentViewSet, LastViewedProductsView, BannerViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'banners', BannerViewSet)

urlpatterns = [
    path('last-viewed-products/', LastViewedProductsView.as_view(), name='last-viewed-products'),
    path('categories/<str:category_name>/<int:product_id>/', ProductViewSet.as_view({'get': 'retrieve_product_in_category'}), name='category-product-detail'),
    path('', include(router.urls)),
]
