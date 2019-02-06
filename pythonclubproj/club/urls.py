from django.urls import path
from . import views



urlpatterns=[
    path('', views.index, name='index'),
    # index is different than the rest so now you have to do the name of the view
    path('resources/', views.resources, name='resources'),
    path('meetings', views.meetings, name='getmeetings' ),
    path('minutes/<int:id>', views.minutes, name='minutes'),
]

# urlpatterns=[
#     path('', views.index, name='index'),
#     # index is different than the rest so now you have to do the name of the view
#     path('techtypes/', views.techtypes, name='techtypes'),
#     path('getproducts',views.getproducts, name='getproducts'),
#     path('productdetail/<int:id>', views.productdetail, name='details'),
# ]