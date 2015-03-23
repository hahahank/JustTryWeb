from django.conf.urls import include, url,patterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('', 
    # home
    (r'^$', 'main.views.login'),

    # app
    (r'^main/', include('main.urls')),

)