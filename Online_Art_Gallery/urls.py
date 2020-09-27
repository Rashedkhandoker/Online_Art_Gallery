"""Online_Art_Gallery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Profile import views as ProfileView
from Artwork  import views as Artworkview
from Blog import views as Blog_views
from Event import views as EventView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('CreateProfile/', ProfileView.createprofile,name='CreateProfile'),
    path('ShowProfile/',ProfileView.showProfile,name='ShowProfile'),
    path('signup/', ProfileView.registration,name='signup'),
    #path('InsertUsers/', ProfileView.insertUser), #User insert er table dekhabe
    path('ShowArtwork/',Artworkview. showArtwork,name='ShowArtwork'),
    path('InsertArtwork/',Artworkview.insertArtwork,name='InsertArtwork'),
    path('ShowBlogs/', Blog_views.showBlog,name='ShowBlogs'),
    path('InsertBlogs/', Blog_views.insertBlog,name='InsertBlog'),
    path('Exhibition/',EventView.showevent,name='Exhibition'),
    path('Competition/',EventView.showcompetition,name='Competition'),
    path('accounts/',include('django.contrib.auth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
