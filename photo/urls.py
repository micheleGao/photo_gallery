from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # localhost:8000/artist
    path('artists/', views.ArtistList.as_view(), name='artist_list'),
    path('artists/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail'),
    path('gallery/', views.GalleryList.as_view(), name='gallery_list'),
    path('gallery/<int:pk>', views.GalleryDetail.as_view(), name='gallery_detail'),
    path('reviews/', views.ReviewList.as_view(), name='review_list'),
    path('reviews/<int:pk>', views.ReviewDetail.as_view(), name='review_detail'),
]