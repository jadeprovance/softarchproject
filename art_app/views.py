
from django.shortcuts import render, get_object_or_404
from .models import ArtPiece, Comment, Favorite
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required

def home(request):
    # Your view logic here
    context = {'message': 'Welcome to the art app!'}
    return render(request, 'home.html', context)

def art_detail(request, art_id):
    art_piece = get_object_or_404(ArtPiece, pk=art_id)
    comments = Comment.objects.filter(art_piece=art_piece)
    
    context = {
        'art_piece': art_piece,
        'comments': comments,
    }
    return render(request, 'art_detail.html', context)

@login_required
def add_to_favorites(request, art_id):
    art_piece = get_object_or_404(ArtPiece, pk=art_id)

    if not Favorite.objects.filter(user=request.user, art_piece=art_piece).exists():
        Favorite.objects.create(user=request.user, art_piece=art_piece)
        return HttpResponse("Art added to favorites")
    else:
        return HttpResponse("Art is already in favorites")

@login_required
def remove_from_favorites(request, art_id):
    art_piece = get_object_or_404(ArtPiece, pk=art_id)
    favorite = Favorite.objects.filter(user=request.user, art_piece=art_piece).first()

    if favorite:
        favorite.delete()
        return HttpResponse("Art removed from favorites")
    else:
        return HttpResponse("Art is not in favorites")

@login_required
def add_comment(request, art_id):
    art_piece = get_object_or_404(ArtPiece, pk=art_id)

    if request.method == 'POST':
        text = request.POST.get('text', '')
        Comment.objects.create(user=request.user, art_piece=art_piece, text=text)
        return HttpResponse("Comment added")
    else:
        return HttpResponse("Invalid request")

def get_comments(request, art_id):
    art_piece = get_object_or_404(ArtPiece, pk=art_id)
    comments = Comment.objects.filter(art_piece=art_piece)

    comment_list = []
    for comment in comments:
        comment_list.append(f"{comment.user.username}: {comment.text}")

    return HttpResponse("\n".join(comment_list))

@login_required
def profile(request):
    
    user = request.user
    favorites = Favorite.objects.filter(user=user)

    
    context = {
        'user': user,
        'favorites': favorites,
    }

    
    return render(request, 'profile.html', context)