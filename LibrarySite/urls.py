"""
LibrarySite URLS config
"""

from django.conf.urls import url
from . import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^123213/$',views.test, name='testPage'),
    url(r'^register/$', views.userRegistration, name='registration'),
    url(r'', include('blog.urls', namespace="blog")),
    url(r'search_results/',views.search, name='search'),
    url(r'^login/$', views.LoginRequest),
    url(r'^login/#signup/$', views.userRegistration),
    url(r'^accounts/login/$', views.LoginRequest),
    url(r'^logout/$', views.LogoutRequest),
    url(r'^profile/$', views.profile),
    url(r'^books/$', views.books, name='bookpage'),
    url(r'^books/(?P<pk>\d+)/$', views.book_detail, name='book_detail'),
    url(r'^news/$', views.news, name='news'),
    url(r'^resetpassword/passwordsent/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^resetpassword/$', 'django.contrib.auth.views.password_reset'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
