from django.urls import path

from .views import (
    index,
    detail,
    tags,
    create_flower,
    edit_flower,
    delete_flower
)


urlpatterns = [
    # ? Home Route
    path('', index , name="home"),

    # ? Flower Detail Route
    path('flower/details/<slug:slug>/', detail, name='detail'),

    # ? Tags Route
    path('tags/<slug:slug>/', tags, name='tags'),

    # ? Create Flower Route
    path('flower/create/', create_flower, name='create'),

    # ? Update Flower Route
    path('flower/edit/<int:pk>/', edit_flower, name='edit'),

    # ? Delete Existing Flower Route
    path('flower/delete/<int:pk>/', delete_flower, name='delete'),
]

