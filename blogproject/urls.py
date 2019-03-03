from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import blogapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    path('blog/<int:blog_model_id>/', blogapp.views.detail, name="detail"),
    path('blog/new/', blogapp.views.new, name="new"),
    path('blog/create/', blogapp.views.create, name="create"),
    path('blog/newblog/', blogapp.views.blogpost, name="newblog"),
    path('blog/<int:blog_model_id>/edit/', blogapp.views.edit, name='edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
