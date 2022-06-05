from datetime import date
from django.shortcuts import render

data = {
    "movies": [
        {
            "title": "film adi 1",
            "description": "film açiklama 1",
            "imageUrl": "m1.jpg",
            "coverImage":"cover1.jpg",
            "slug": "film-adi-1",
            "language": "english",
            "date": date(2021,10,10)
        },
        {
            "title": "film adi 2",
            "description": "film açiklama 2",
            "imageUrl": "m2.jpg",
            "coverImage":"cover2.jpg",
            "slug": "film-adi-2",
            "language": "english",
            "date": date(2021,5,10)
        },
        {
            "title": "film adi 3",
            "description": "film açiklama 3",
            "imageUrl": "m3.jpg",
            "coverImage":"cover3.jpg",
            "slug": "film-adi-3",
            "language": "english",
            "date": date(2021,10,5)
        },
        {
            "title": "film adi 4",
            "description": "film açiklama 4",
            "imageUrl": "m4.jpg",
            "coverImage":"cover1.jpg",
            "slug": "film-adi-4",
            "language": "english",
            "date": date(2020,10,5)
        },
        {
            "title": "film adi 3",
            "description": "film açiklama 3",
            "imageUrl": "m3.jpg",
            "slug": "film-adi-3",
            "language": "english",
            "date": date(2021,10,5)
        },
        {
            "title": "film ad, 4",
            "description": "film açiklama 4",
            "imageUrl": "m4.jpg",
            "slug": "film-adi-4",
            "language": "english",
            "date": date(2020,10,5)
        }
    ],
    "sliders": []
}


# Create your views here.

def index(request):
    movies = data["movies"][-4:]
    return render(request, 'index.html', {
        "movies": movies
    })

def movies(request):
    movies = data["movies"]
    return render(request, 'movies.html', {
        "movies": movies
    })

def movie_details(request, slug):
    movies = data["movies"]
    selectedMovie = None

    for movie in movies:
        if movie[slug] == slug:
           selectedMovie = movie

    return render(request, 'movie-details.html', {
        "movie": selectedMovie
})