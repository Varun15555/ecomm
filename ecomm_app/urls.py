from django.urls import path
from . import views
from ecomm import settings
from django.conf.urls.static import static
#from .views import SimpleView
#from ecomm_app import views


urlpatterns = [
    path('about',views.about),
    path('contact',views.contact),
    path('delete/<rid>',views.delete),
    path('addition/<x>/<y>',views.addition),
    path('myview',views.SimpleView.as_view()),
    path('hello',views.hello),
    path('',views.home),
    path('pdetails',views.product_details),
    path('register',views.register),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('catfilter/<cv>',views.catfilter),
    path('sort/<sv>',views.sort),
    path('range',views.range),
    path('pdetails/<pid>',views.product_details),
    path('addtocart/<pid>',views.addtocart),
    path('viewcart',views.viewcart),
    path('remove/<cid>',views.remove),
    path('updateqty/<qv>/<cid>',views.updateqty),
    path('placeorder',views.placeorder),
    path('makepayment',views.makepayment),
    path('sendmail/<uemail>',views.sendusermail)

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
