from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema')),        
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),    
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/', include('accounts.urls')),        
    path('resources/',include('resources.urls')),
    path('announcements/',include('announcements.urls')),
    path('blog/',include('blog.urls')),
]   
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)