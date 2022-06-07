from django.urls import path
from .views import (getAllCampangAPI, createCampaignAPI, 
                    getDetailCampaignAPI, updateCampaignsAPI, 
                    campaignDeleteAPI, getDetailCampaignSlugAPI, 
                    createSubscriberAPI, getAllSubscriberAPI)

urlpatterns = [
   path('campaigns/all/', getAllCampangAPI, name="list-campaign"),
   path('campaigns/create', createCampaignAPI, name='campaign-create'),
   path('campaigns/detail/<int:pk>/', getDetailCampaignAPI, name='detail-campaign'),
   path('campaigns/details/<str:slug>/', getDetailCampaignSlugAPI, name='details-campaign'),
   path('campaigns/update/<int:pk>/', updateCampaignsAPI, name="campaign-update"),
   path('campaigns/delete/<pk>/', campaignDeleteAPI, name='campaign-delete'),
   path('campaigns/subscriper/create/', createSubscriberAPI, name="subscriber-create"),
   path('campaigns/subscriper/all/', getAllSubscriberAPI, name="subscriber-all"),
]