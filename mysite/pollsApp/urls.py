# File created anew, this file is a URLconf which is the way to get Django know about how to display urls. URLconf maps URL patterns to views

from django.urls import path
from . import views

app_name = 'pollsApp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='details'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

# Previously, in the urlpatterns
    # # ex: /pollsApp/
    # path("", views.index, name='index'),
    # # ex: /pollsApp/5/
    # path('specifics/<int:question_id>/', views.detail, name='detail'),        # the 'name' value is called by the {% url %} template tag
    # # ex: /pollsApp/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # #ex: /pollsApp/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),