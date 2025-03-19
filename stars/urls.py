from django.urls import path
from stars import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='addpage'),
    path('login/', views.login, name='login'),
    path('person/<slug:person_slug>/', views.show_person, name='person'),
    path('category/<slug:cat_slug>/', views.show_categories, name='category'),
]

