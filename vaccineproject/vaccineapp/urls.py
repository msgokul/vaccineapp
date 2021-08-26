from django.urls import path,include
from vaccineapp import views
urlpatterns = [
   path('',views.index,name='home'),
   path('register/',views.register,name='register'),
   path('login/',views.login,name='login'),
   path('logout/',views.logout,name='logout'),
   path('booking/',views.booking,name='booking'),
   path('profile/',views.profile,name='profile'),
   path('booking/result/',views.result,name='result'),

   path('ajax/load-taluks/', views.load_taluks, name='ajax_load_taluks'),  # AJAX

]