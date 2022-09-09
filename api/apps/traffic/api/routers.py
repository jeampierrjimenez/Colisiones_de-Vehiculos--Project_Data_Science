from rest_framework.routers import DefaultRouter
from apps.traffic.api.views import *
from django.urls import re_path, path


router = DefaultRouter()

urlpatterns = router.urls + [re_path('^boro_year_month/(?P<boro>.+)/(?P<year>.+)/(?P<month>.+)/$',
                                     TrafficBoroYearMonth.as_view()),
                             re_path('^boro_year_month_hour/(?P<boro>.+)/(?P<year>.+)/(?P<month>.+)/(?P<hour>.+)/$',
                                     TrafficBoroYearMonthHour.as_view()),
                             re_path('^boro_year_month_alt/(?P<boro>.+)/(?P<year>.+)/(?P<month>.+)/$',
                                     TrafficAltBoroYearMonth.as_view()),
                             path('model/', ModelViewSet.as_view()),
                             ]
#re_path('^boro_year/(?P<boro>.+)/(?P<year>.+)/$',
#                              TrafficBoroYear.as_view()),