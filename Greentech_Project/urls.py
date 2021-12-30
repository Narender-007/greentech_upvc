"""Greentech_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from Upvc_application.views import *

from django.urls import path
from Upvc_application import views
from django.urls import path
# from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("index1",views.Indexss),
    path("index",Indexss),
    path("About_Us",About_Us),
    path("Contact_us",Contact_us),
    path("Features",Features),
    path("Gallery",Gallery),
    path("Products",Products),
    path("Testimonials",Testimonials),
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
    path("socketsendingsss", views.sender, name="socketsending"),
    path("signup",views.signup,name="signup"),
    path('enter_otp', views.otp_call, name='otp_confirmed'),
    path('socketsending', views.sendingSocket,name='socketsending'),
    path('socket', views.socket,name='socket'),


    # Your URLs...
    # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),


]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)