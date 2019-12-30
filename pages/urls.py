from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rules', views.rules, name='rules'),
    path('fixtures', views.fixtures, name='fixtures'),
    path('live_matches', views.live_matches, name='live_matches'),
    path('ranking', views.ranking, name='ranking'),
    path('registration', views.registration, name='registration'),
    path('save_reg', views.save_reg, name='save_reg'),
    path('venue', views.venue, name='venue')
    
]