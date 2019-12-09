
from django.contrib import admin
from django.conf.urls import url,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from articles import views as article_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^articles/',include('articles.urls')),
    url(r'^about/$',views.about),
    url(r'^$',article_views.articles_list,name="home"),
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)