# from django.urls  import  path
# from . import views

# urlpatterns=[ 
#     path('login/',views.login_api),
#     path('user/',views.get_user_data)
# ]

from rest_framework import routers

from .views import LeadViewset

router = routers.DefaultRouter()
router.register('leads', LeadViewset, 'leads')

urlpatterns = router.urls
