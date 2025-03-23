from django.urls import path
from stars import views


urlpatterns = [
    path('', views.StarsHome.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('addpage/', views.AddPage.as_view(), name='addpage'),
    path('person/<slug:person_slug>/', views.ShowPerson.as_view(), name='person'),
    path('category/<slug:cat_slug>/', views.StarsCategory.as_view(), name='category'),
]

