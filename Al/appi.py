from rest_framework import routers
from apps.product_order.views import OrderModelViewset,  OrderProductViwset
from apps.user.views import UserManagerViewset,  UserModelViwset
from apps.product.views import CategoryViewset,  ProductViewset

router = routers.SimpleRouter()


router.register('orderModel', OrderModelViewset)
router.register(' orderProduct',  OrderProductViwset)
router.register('userManager', UserManagerViewset)
router.register('userModel',UserModelViwset)
router.register('category',CategoryViewset )
router.register('product', ProductViewset)




urlpatterns = []
urlpatterns += router.urls