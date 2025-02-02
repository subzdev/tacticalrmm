from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
import requests
import json
from ..models import Integration 

class GetOrganizations(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        integration = Integration.objects.get(name="Cisco Meraki")

        result = requests.get(
            integration.base_url + "organizations/",
            verify=False,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "X-Cisco-Meraki-API-Key": integration.api_key
            }, timeout=(2,30),
        ).json()

        return Response(result)

class GetOrganization(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, organization_id, format=None):
        integration = Integration.objects.get(name="Cisco Meraki")

        result = requests.get(
            integration.base_url + "organizations/" + organization_id,
            verify=False,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "X-Cisco-Meraki-API-Key": integration.api_key
            }, timeout=(2,30),
        ).json()

        return Response(result)


class GetNetworks(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        integration = Integration.objects.get(name="Cisco Meraki")

        result = requests.get(
            integration.base_url + "organizations/" + pk + "/networks",
            verify=False,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "X-Cisco-Meraki-API-Key": integration.api_key
            }, timeout=(2,30),
        ).json()

        return Response(result)

class GetDevices(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk,format=None):
        integration = Integration.objects.get(name="Cisco Meraki")

        result = requests.get(
            integration.base_url + "/organizations/" + pk + "/devices/statuses/",
            verify=False,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "X-Cisco-Meraki-API-Key": integration.api_key
            }, timeout=(2,30),
        ).json()

        return Response(result)

class GetOverview(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, timespan, format=None):
        integration = Integration.objects.get(name="Cisco Meraki")

        if "t0" and "t1" in str(timespan):
            url = integration.base_url + "organizations/" + pk +"/summary/top/devices/byUsage?perPage=1000&" + str(timespan)
        else:
            url = integration.base_url + "organizations/" + pk +"/summary/top/devices/byUsage?perPage=1000&timespan=" + str(timespan)

        result = requests.get(
            url,
            verify=False,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "X-Cisco-Meraki-API-Key": integration.api_key
            }, timeout=(2,30),
        ).json()

        return Response(result)

class GetNetworkUplinks(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        integration = Integration.objects.get(name="Cisco Meraki")

        result = requests.get(
            integration.base_url + "organizations/" + pk + "/uplinks/statuses",
            verify=False,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "X-Cisco-Meraki-API-Key": integration.api_key
            }, timeout=(2,30),
        ).json()

        return Response(result)

class GetTopClients(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, timespan, format=None):
        integration = Integration.objects.get(name="Cisco Meraki")

        if "t0" and "t1" in str(timespan):
            url = integration.base_url + "organizations/" + pk +"/summary/top/clients/byUsage?" + str(timespan)
        else:
            url = integration.base_url + "organizations/" + pk +"/summary/top/clients/byUsage?timespan=" + str(timespan)

        result = requests.get(
            url,
            verify=False,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "X-Cisco-Meraki-API-Key": integration.api_key
            }, timeout=(2,30),
        ).json()

        return Response(result)


class GetClient(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, mac, format=None):
        integration = Integration.objects.get(name="Cisco Meraki")

        try:
            result = requests.get(
                integration.base_url + "/organizations/" + pk + "/clients/search?mac=" + mac,
                verify=False,
                headers={
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "X-Cisco-Meraki-API-Key": integration.api_key
                }, timeout=(2,30),
            ).json()
            
            return Response(result)
        except ValueError:
            return Response()

class GetNetworkApplicationTraffic(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, network_id, timespan, format=None):
        integration = Integration.objects.get(name="Cisco Meraki")

        if "t0" in str(timespan):
            url = integration.base_url + "networks/" + network_id + "/traffic?perPage=1000&" + str(timespan)
        else:
            url = integration.base_url + "networks/" + network_id + "/traffic?perPage=1000&timespan=" + str(timespan)

        result = requests.get(
            url,
            verify=False,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "X-Cisco-Meraki-API-Key": integration.api_key
            }, timeout=(2,30),
        ).json()

        return Response(result)

class GetNetworkClientTraffic(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, network_id, timespan, format=None):
        integration = Integration.objects.get(name="Cisco Meraki")

        if "t0" and "t1" in str(timespan):
            url = integration.base_url + "networks/" + network_id +"/clients?perPage=1000&" + str(timespan)
        else:
            url = integration.base_url + "networks/" + network_id +"/clients?perPage=1000&timespan=" + str(timespan)
        
        result = requests.get(
            url,
            verify=False,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "X-Cisco-Meraki-API-Key": integration.api_key
            }, timeout=(2,30),
        ).json()

        return Response(result)

class GetNetworkEvents(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, network_id, timespan, format=None):
        integration = Integration.objects.get(name="Cisco Meraki")

        if "startingAfter" in str(timespan):
            url = integration.base_url + "networks/"+ network_id +"/events?perPage=1000&productType=appliance&" + str(timespan)
        else:
            url = integration.base_url + "networks/"+ network_id +"/events?perPage=1000&productType=appliance"

        result = requests.get(
            url,
            verify=False,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "X-Cisco-Meraki-API-Key": integration.api_key
            }, timeout=(2,30),
        ).json()

        return Response(result)

class GetClientPolicy(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, network_id, client_mac, format=None):
        integration = Integration.objects.get(name="Cisco Meraki")

        result = requests.get(
            integration.base_url + "networks/" + network_id + "/clients/" + client_mac + "/policy",
            verify=False,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "X-Cisco-Meraki-API-Key": integration.api_key
            }, timeout=(2,30),
        ).json()

        return Response(result)

    def put(self, request, network_id, client_mac, format=None):
        integration = Integration.objects.get(name="Cisco Meraki")

        request_dict = {"devicePolicy": request.data['devicePolicy']}
        payload = json.dumps(request_dict, indent=4)

        result = requests.put(
            integration.base_url + "networks/" + network_id + "/clients/" + client_mac + "/policy",
            verify=False,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "X-Cisco-Meraki-API-Key": integration.api_key
            }, data=payload, timeout=(2,30),
        ).json()
        
        return Response(result)