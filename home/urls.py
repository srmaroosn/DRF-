from unicodedata import name
from django import views
from django import urls
from django.urls import include
from django.urls import path
from .import views
from .views import BookAPIview,BookAPIviewdetails, BookViewSet,Booklistmixin,BookDetailMixin, BooklistCreate,BookDetail
from rest_framework.routers import DefaultRouter


router =DefaultRouter()
router.register(r'book_viewsets', views.BookViewSet, basename='book_viewsets')


urlpatterns = [
    path('book/', views.blist, name='blist'),
    path('book_details/<int:pk>/',views.blist_details, name='blist_details'),
    path('book-api-view/', BookAPIview.as_view(),name='book-api-view'),

    path('book-api-view-detail/<int:id>/', BookAPIviewdetails.as_view(), name='book-api-view-detail'),
    path('book-view-mixins/', Booklistmixin.as_view(),name='book-view-mixins'),

    path('book-view-detail-mixins/<int:pk>/',BookDetailMixin.as_view(),name='book-view-detail-mixins'),
    path('booklist/', BooklistCreate.as_view(),name='booklist'),
    path('booklistdetail/<int:pk>/',BookDetail.as_view(),name='booklistdeatils'),
    #viewsets
    path('viewset/', include(router.urls))

]