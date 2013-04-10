from django.conf.urls import patterns, include, url
from statistic import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web_statistic.views.home', name='home'),
    # url(r'^web_statistic/', include('web_statistic.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.show_page),
    url(r'^login/$', views.show_login_page),
    url(r'^signup/$', views.show_signup_page),
    url(r'^blog/$', views.show_blog_page),
    url(r'^user_login/$', views.user_login),
    url(r'^logout/$', views.user_logout),
    url(r'^signup_user/$', views.user_registration)
)
