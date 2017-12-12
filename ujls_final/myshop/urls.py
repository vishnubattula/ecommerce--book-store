from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Examples:
    # url(r'^$', 'myshop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^',include('shop.urls',namespace='shop')),
    url((r'^payment/'), include('payment.urls', namespace='payment')),
    url(r'^orders/',include('orders.urls',namespace='orders')),
    url(r'^cart',include('cart.urls',namespace='cart')),
    url((r'^coupons/'), include('coupons.urls', namespace='coupons')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
