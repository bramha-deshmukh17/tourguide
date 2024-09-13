"""
URL configuration for tourguide project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include,path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path("", views.index, name="index"),
   
    #customer section
    path('customer/signup/', views.signup,name="signup"),
    path('register/', views.register,name="register"),
    path('login/', views.login,name="login"),

    path('forgotpassword/', views.forgotPage,name="forgotPage"),
    path('getforget/', views.forgotPassword,name="forgotPassword"),
    path('updatepassword/', views.uppassword,name="updatepassword"),

    path('logout/', views.logout,name="logout"),

    path('home/', views.home,name="home"),
    path('contact/', views.contact,name="contact"),
    path('about/', views.about,name="about"),
    path('profile/', views.profile,name="profile"),
    path('bookings/', views.bookings,name="bookings"),
    path('cacelbooking/', views.cacelBook,name="cancelBookings"),
    path('rate/', views.rate,name="rate"),

    path('cutomerProfile/', views.cutomerProfile,name="cutomerProfile"),
    path('updatePassword/', views.updatePassword,name="updatePassword"),

    path("restaurants/", views.restaurant, name="restaurant"),
    path("restaurants/search/", views.search, name="restaurantSearch"),
    path("restaurants/details/", views.details, name="restaurantDetails"),

    path("hotels/", views.hotel, name="hotel"),
    path("hotels/search/", views.search, name="hotelSearch"),
    path("hotels/details/", views.details, name="restaurantDetails"),
    
    path("places/", views.place, name="place"),
    path("places/search/", views.search, name="PlaceSearch"),
    path("places/details/", views.details, name="restaurantDetails"),

    #tourguide section
    path('tourguide/signup/', views.tsignup,name="tsignup"),
    path('tourguide/register/', views.tregister,name="tregister"),
    path('tourguide/login/', views.tlogin,name="tlogin"),

    path('tourguide/forgotpassword/', views.tforget,name="tforget"),
    path('tourguide/getforget/', views.tforgotPassword,name="forgotPassword"),
    path('tourguide/updatepassword/', views.tuppassword,name="tuppassword"),

    path('tourguide/details/', views.tdetails,name="tDetails"),
    path('tourguide/book/', views.tbook,name="tBook"),
    path('tourguide/book/status/', views.bookStatus,name="tBook status"),
    path('status/', views.status,name="status"),
    path('pay/', views.pay,name="pay"),

    path('tourguide/home/', views.thome,name="thome"),
    path('tourguide/contact/', views.tcontact,name="tcontact"),
    path('tourguide/profile/', views.tprofile,name="tprofile"),
    
    path('tourguide/tprofile/', views.upTprofile,name="upTprofile"),
    path('tourguide/tpassword/', views.upTpassword,name="upTpassword"),
    path('tourguide/tphoto/', views.tphoto,name="tphoto"),

    #admin section
    path('admin/login/', views.alogins,name="alogins"),
    path('admin/signin/', views.asignin,name="asignin"),
    path('admin/home/', views.ahome,name="ahome"),
    path('admin/viewtourguide/', views.viewtourguide,name="viewtourguide"),

    path('admin/hotel/', views.ahotel,name="ahotel"),
    path('addhotel/', views.addHotel,name="addHotel"),
    path('update/hotel/', views.updateHotel,name="updateHotel"),
    path('hotel/photo/', views.hotelPhoto,name="hotelPhoto"),

    path('admin/restaurant/', views.arestaurant,name="arestaurant"),
    path('addrestaurant/', views.addRestaurant,name="addrestaurant"),
    path('update/restaurant/', views.updateRestaurant,name="updaterestaurant"),
    path('restaurant/photo/', views.restaurantPhoto,name="restaurantPhoto"),

    path('admin/places/', views.aplaces,name="aplaces"),
    path('addplace/', views.addPlace,name="addplace"),
    path('update/place/', views.updatePlace,name="updateplace"),
    path('place/photo/', views.placePhoto,name="placePhoto"),

    #other
    path('test/', views.test,name="test"),
    path('database/', admin.site.urls,name="database"),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
