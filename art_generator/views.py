
import requests
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from art_app.models import ArtPiece

@login_required
def generate_art(request):
    api_key = "abb53b86-ab26-41ee-bb5c-32bac71dcf53"
    base_url = "https://api.harvardartmuseums.org/object"

    params = {
        "apikey": api_key,
        "size": 5,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        art_pieces = []

        for result in data.get("records", []):
            art_piece = ArtPiece(
                title=result.get("title", "Untitled"),
                image_url=result.get("primaryimageurl", ""),
                description=result.get("description", ""),
                artist=result.get("people", [{"name": "Unknown"}])[0]["name"],
                date=result.get("dated", ""),
            )
            art_pieces.append({'id': None, **art_piece.__dict__})

        context = {'art_pieces': art_pieces}
        return JsonResponse(context)
    else:
        context = {'error_message': 'Unable to fetch art pieces'}
        return JsonResponse(context, status=500)

