from django.conf.urls import url
from regexapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ajax/question_hw$', views.question_hw, name='question_hw'),
]
