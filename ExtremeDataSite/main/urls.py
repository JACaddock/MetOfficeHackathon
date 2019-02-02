from django.urls import path

from . import views


app_name = 'main'
urlpatterns = [
    # ex: /main/
    path('', views.index, name='index'),
    # ex: /main/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /main/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /main/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    
    path('benjamin', views.BenjaminRespect, name='BenjaminRespect'),
    ]