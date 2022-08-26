from rest_framework.routers import DefaultRouter
from apps.collisions.api.views import *
from django.urls import re_path, path

router = DefaultRouter()

#router.register(r'zone_crash', ZoneCrashViewSet, basename='collisions')
#re_path('^collisions_range/(?P<fecha_inicio>.+)/(?P<fecha_final>.+)/$',
                                     #CollisionsForDayViewSet.as_view())

urlpatterns = router.urls + [re_path('^collisions_for_day/(?P<fecha>.+)/$',
                                     CollisionsForDayViewSet.as_view()),
                             path('time_crash/', TimeCrashPercViewSet.as_view()),
                             path('zone_crash/', ZoneCrashViewSet.as_view()),
                             path('public_damage/', PublicDamageViewSet.as_view()),
                             path('licence_state/', LicenceStatesViewSet.as_view()),
                             path('factor_genere/', FactorBySexViewSet.as_view()),
                             path('type/', DataMonthlyByTypeViewSet.as_view()),
                             path('status/', DataMonthlyByStatusViewSet.as_view()),
                             path('genere/', DataMonthlyBySexViewSet.as_view()),
                             path('state_person/', DataMonthlyByInjuryViewSet.as_view())]

