from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'championship.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'events.views.index', name='index'),
    url(r'^torneo/(?P<id_event>\d+)/$','teams.views.viewStandings', name='viewStandings'),
    url(r'^torneo/(?P<id_event>\d+)/fixture/$','matches.views.viewFixture', name='viewFixture'),
    url(r'^torneo/(?P<id_event>\d+)/images/$','images.views.viewImage', name='viewImage'),
    url(r'^torneo/(?P<id_event>\d+)/players/$','players.views.viewPlayesGoals', name='viewPlayesGoals'),
    url(r'^torneo/(?P<id_event>\d+)/cards/$','cards.views.viewCards', name='viewCards'),
    url(r'^admin/', include(admin.site.urls)),
)
