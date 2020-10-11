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
from Artwork import views as Artworkview
from Blog import views as Blog_views
from Event import views as EventView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Homepage/',ProfileView.showHome,name='Homepage'),
    path('CreateProfile/', ProfileView.createprofile,name='CreateProfile'),
    path('showprofile/',ProfileView.showProfile,name='ShowProfile'),
    path('signup/', ProfileView.registration,name='signup'),
    path('ShowArtwork/',Artworkview. showArtwork,name='ShowArtwork'),
    path('ShowArtwork/<int:artwork_id>', Artworkview.showDetails, name='detail_view'),
    path('InsertArtwork/',Artworkview.insertArtwork,name='InsertArtwork'),
    path('ShowBlogs/', Blog_views.showBlog,name='ShowBlogs'),
    path('ShowBlogs/<int:b_id>', Blog_views.showDetails, name='detail_view'),
    path('InsertBlogs/', Blog_views.insertBlog,name='InsertBlogs'),
    path('Competition/',EventView.showcompetition,name='Competition'),
    path('Competition/<int:comp_id>', EventView.showDetails, name='detail_view'),
    path('SubmitCompetition/', EventView.submitart, name='SubmitCompetition'),
    path('ShowSubmission/', EventView.showSubmission, name='ShowSubmission'),
    path('ShowSubmission/<int:s_id>', EventView.showDetails2, name='detail_view'),
    path('review/<int:s_id>', EventView.review_after_submit, name='review'),
    path('accounts/',include('django.contrib.auth.urls'))


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

