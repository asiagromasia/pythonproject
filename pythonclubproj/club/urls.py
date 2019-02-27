from django.urls import path
from . import views



urlpatterns=[
    path('', views.index, name='index'),
    # index is different than the rest so now you have to do the name of the view
    path('resources/', views.resources, name='resources'),
    path('newresource/', views.newresource, name='newresource'),
    path('meetings/', views.meetings, name='meetings' ),
    path('meetingdetail/<int:id>', views.meetingdetail, name='details'),
    path('newMeeting/', views.newMeeting, name='newmeeting'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
     ]

# urlpatterns=[
#     path('', views.index, name='index'),
#     # index is different than the rest so now you have to do the name of the view
#     path('techtypes/', views.techtypes, name='techtypes'),
#     path('getproducts',views.getproducts, name='getproducts'),
#     path('productdetail/<int:id>', views.productdetail, name='details'),
 #    path('newProduct/', views.newProduct, name='newproduct'),
# ]