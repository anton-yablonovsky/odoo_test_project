import json
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Building, Entrance, Apartment, User
from .serializers import BuildingSerializer, EntranceSerializer, ApartmentSerializer, ManagerSerializer, UserSerializer, GuardSerializer, InhabitantSerializer
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from rest_framework.exceptions import PermissionDenied

@require_POST
def login_view(request):
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")

    user = authenticate(username=username, password=password)

    if user:
        login(request, user)
        return JsonResponse({'success': True})

    return JsonResponse(
        {'success': False, 'message': 'Invalid credentials'}, status=401
    )


def logout_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"detail": "You're not logged in."}, status=400)
    logout(request)
    return HttpResponse(status=204)


def is_authenticated(request):
    return JsonResponse({"is_authenticated": request.user.is_authenticated})


@ensure_csrf_cookie
@require_http_methods(['GET'])
def set_csrf_token(request):
    """
    We set the CSRF cookie on the frontend.
    """
    return JsonResponse({'message': 'CSRF cookie set'})


@login_required
@require_GET
def get_user_role(request):
    user = request.user
    role = user.role
    return JsonResponse({'role': role})


@api_view(['GET'])
def get_buildings(request):
    buildings = Building.objects.all()
    serializer = BuildingSerializer(buildings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_building(request, building_id):
    """API endpoint to delete a building by ID"""
    try:
        building = Building.objects.get(id=building_id)
    except Building.DoesNotExist:
        return Response({"error": "Building not found"}, status=status.HTTP_404_NOT_FOUND)
    
    building.delete()
    return Response({"message": "Building deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET'])
def get_entrances(request):
    entrances = Entrance.objects.all()
    serializer = EntranceSerializer(entrances, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_entrance(request, entrance_id):
    """API endpoint to delete an entrance by ID"""
    try:
        entrance = Entrance.objects.get(id=entrance_id)
    except Entrance.DoesNotExist:
        return Response({"error": "Entrance not found"}, status=status.HTTP_404_NOT_FOUND)
    
    entrance.delete()
    return Response({"message": "Entrance deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_apartments(request):
    entrances = Apartment.objects.all()
    serializer = ApartmentSerializer(entrances, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_apartment(request, apartment_id):
    """API endpoint to delete an apartment by ID"""
    try:
        apartment = Apartment.objects.get(id=apartment_id)
    except Apartment.DoesNotExist:
        return Response({"error": "Apartment not found"}, status=status.HTTP_404_NOT_FOUND)
    
    apartment.delete()
    return Response({"message": "Apartment deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_building(request):
    serializer = BuildingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_entrance(request):
    serializer = EntranceSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def create_apartment(request):
    serializer = ApartmentSerializer(data=request.data)
    print(f"{request.data=}")

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print(f"{serializer.errors=}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_manager(request):
    serializer = ManagerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_guard(request):
    serializer = GuardSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_inhabitant(request):
    serializer = InhabitantSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        if user.role == "ADMIN":
            raise PermissionDenied("Cannot delete an admin user.")
        
        user.delete()
        return Response({"detail": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def get_manager_buildings(request):

    if request.user.role == 'manager':  # Ensure user is a manager
        print(f"{dir(request.user)=}")
        buildings = request.user.buildings.all()  # Access buildings via the relationship
        print(f"{buildings=}")
        serializer = BuildingSerializer(buildings, many=True)
        return Response(serializer.data)
    
    return Response({"detail": "Not authorized"}, status=403)


@api_view(['GET'])
def get_guard_entrances(request):

    if request.user.role == 'guard':
        
        entrances = request.user.entrances.all()  # Access buildings via the relationship
        print(f"{entrances=}")
        serializer = EntranceSerializer(entrances, many=True)
        return Response(serializer.data)
    
    return Response({"detail": "Not authorized"}, status=403)

@api_view(['GET'])
def get_inhabitant_apartment(request):

    if request.user.role == 'inhabitant':  # Ensure user is a manager
        apartments = request.user.apartments.all()  # Access buildings via the relationship
        print(f"{apartments=}")
        serializer = ApartmentSerializer(apartments, many=True)
        return Response(serializer.data)
    
    return Response({"detail": "Not authorized"}, status=403)



