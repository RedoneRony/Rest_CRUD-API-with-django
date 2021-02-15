from rest_framework import routers
from Django_Rest_App.viewsets import AdmissionViewset
router=routers.DefaultRouter()
router.register('admission',AdmissionViewset)


urlpatterns = router.urls

"""
PUT-UPDATE
GET- RETRIEVE / LIST SHOWING
POST-CREATE 
DELETE-delete

"""