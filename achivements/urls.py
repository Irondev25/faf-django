from django.urls import path

from .views import *


#awards
urlpatterns = [
    path('detail/award/<int:pid>/', AwardDetailView.as_view(), name='award-detail'),
    path('create/award/', AwardCreateView.as_view(), name='award-create'),
    path('update/award/<int:pid>/', AwardUpdateView.as_view(), name='award-update'),
    path('delete/award/<int:pid>/', AwardDeleteView.as_view(), name='award-delete'),
    path('filter/award/<int:year>/', filter_awards,name='award-filter'),
]

#Conference
urlpatterns += [
    path('detail/conference/<int:cid>/',
         ConferenceDetailView.as_view(), name='conference-detail'),
    path('create/conference/', ConferenceCreateView.as_view(),
         name='conference-create'),
    path('update/conference/<int:cid>/',
         ConferenceUpdateView.as_view(), name='conference-update'),
    path('delete/conference/<int:cid>/',
         ConferenceDeleteView.as_view(), name='conference-delete'),
     path('filter/conference/<int:year>', filter_conferences, name='conference-filter'),
]

#journal
urlpatterns += [
    path('detail/journal/<int:pid>/',
         JournalDetailView.as_view(), name='journal-detail'),
    path('create/journal/', JournalCreateView.as_view(),
         name='journal-create'),
    path('update/journal/<int:pid>/',
         JournalUpdateView.as_view(), name='journal-update'),
    path('delete/journal/<int:pid>/',
         JournalDeleteView.as_view(), name='journal-delete'),
    path('filter/journal/<int:year>',
         filter_journals, name='journal-filter'),
]

#workshop
urlpatterns += [
    path('detail/workshop/<int:pid>/',
         WorkshopDetailView.as_view(), name='workshop-detail'),
    path('create/workshop/', WorkshopCreateView.as_view(),
         name='workshop-create'),
    path('update/workshop/<int:pid>/',
         WorkshopUpdateView.as_view(), name='workshop-update'),
    path('delete/workshop/<int:pid>/',
         WorkshopDeleteView.as_view(), name='workshop-delete'),
    path('filter/workshop/<int:year>',
         filter_workshops, name='workshop-filter'),
]



