from rest_framework.routers import DefaultRouter
from apps.collisions.api.views import *
from django.urls import re_path, path

# Rutas(URL) de la API
router = DefaultRouter()

urlpatterns = router.urls + [re_path('^collisions_day/(?P<fecha>.+)/$',
                                     CollisionsForDayViewSet.as_view()),
                             re_path('^collisions_boro_year/(?P<boro>.+)/(?P<year>.+)/$',
                                     CollisionsForBoroYearViewSet.as_view()),
                             re_path('^collisions_boro_year_month/(?P<boro>.+)/(?P<year>.+)/(?P<month>.+)/$',
                                     CollisionsForBoroYearMonthViewSet.as_view()),
                             re_path('^public_damage/(?P<year>.+)/$',
                                     PublicDamageViewSet.as_view()),
                             path('time_crash/', TimeCrashPercViewSet.as_view()),
                             path('zone_crash/', ZoneCrashViewSet.as_view()),
                             path('licence_state/', LicenceStatesViewSet.as_view()),
                             path('factor_genere/', FactorBySexViewSet.as_view()),
                             path('type/', DataMonthlyByTypeViewSet.as_view()),
                             path('status/', DataMonthlyByStatusViewSet.as_view()),
                             path('genere/', DataMonthlyBySexViewSet.as_view()),
                             path('state_person/', DataMonthlyByInjuryViewSet.as_view()),
                             path('year_month_crash_count/', YearMonthCrashCountViewSet.as_view()),
                             path('day_crash_perc/', DayCrashPercViewSet.as_view()),
                             path('licence/', LicenceViewSet.as_view())]
