from django.contrib import admin
from django.urls import path, re_path
from boards import views
from accounts import views as accounts_views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('signup/', accounts_views.signup, name='signup'),
    re_path(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    re_path(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
]
