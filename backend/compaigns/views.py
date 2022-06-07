from ast import Try
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CampaignSerializer, SubscriberSerializer
from .models import Subscriber, Campaign
from drf_yasg.utils import swagger_auto_schema

# Create your views here.


@api_view(['GET'])
def getAllCampangAPI(request):
    campaigns = Campaign.objects.all()
    serializer = CampaignSerializer(campaigns, many=True)
    data = serializer.data
    if data:
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(method='post', request_body=CampaignSerializer)
@api_view(['POST'])
def createCampaignAPI(request):
    serializer = CampaignSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = serializer.data
        return Response(data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getDetailCampaignAPI(request, pk):
    campaigns = Campaign.objects.filter(pk=pk).first()
    if campaigns:
        serializer = CampaignSerializer(campaigns, many=False)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getDetailCampaignSlugAPI(request, slug):
    campaigns = Campaign.objects.filter(slug=slug).first()
    if campaigns:
        serializer = CampaignSerializer(campaigns, many=False)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)

@swagger_auto_schema(method='put', request_body=CampaignSerializer)
@api_view(['PUT'])
def updateCampaignsAPI(request, pk):
    campaigns = Campaign.objects.get(id=pk)
    if not campaigns:
        return Response({"title: Model not found"})
    serializer = CampaignSerializer(instance=campaigns, data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def campaignPatchAPI(request, pk):
    try:
        campaigns = Campaign.objects.get(id=pk)
    except Campaign.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CampaignSerializer(
        instance=campaigns, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)

    return Response(serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def campaignDeleteAPI(request, pk):
    try:
        campaigns = Campaign.objects.get(id=pk)
    except Campaign.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    campaigns.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@swagger_auto_schema(method='post', request_body=SubscriberSerializer)
@api_view(['POST'])
def createSubscriberAPI(request):
    serializer = SubscriberSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        data = serializer.data
        return Response(data, status = status.HTTP_201_CREATED)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getAllSubscriberAPI(request):
    subscribers = Subscriber.objects.all()
    serializer = SubscriberSerializer(subscribers, many=True)
    data = serializer.data
    if data:
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    