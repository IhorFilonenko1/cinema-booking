"""Каталог фільмів кінотеатру."""

movies = [
    {
        "id": 1,
        "title": "Dune: Part Two",
        "genre": "Sci-Fi",
        "year": 2024,
        "duration": 166,
        "seats": 60,
        "price": 150.0,
    },
    {
        "id": 2,
        "title": "Oppenheimer",
        "genre": "Drama",
        "year": 2023,
        "duration": 180,
        "seats": 45,
        "price": 140.0,
    },
    {
        "id": 3,
        "title": "Inside Out 2",
        "genre": "Animation",
        "year": 2024,
        "duration": 96,
        "seats": 80,
        "price": 100.0,
    },
]

_next_id = 4


def list_movies():
    """Повертає список усіх фільмів."""
    return movies


def get_movie(movie_id):
    """Повертає фільм за id або None."""
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    return None


def add_movie(title, genre, year, duration, seats, price):
    """Додає новий фільм до каталогу та повертає його."""
    global _next_id
    movie = {
        "id": _next_id,
        "title": title,
        "genre": genre,
        "year": year,
        "duration": duration,
        "seats": seats,
        "price": price,
    }
    _next_id += 1
    movies.append(movie)
    return movie


def search_movies(query):
    """Шукає фільми за частиною назви (без урахування регістру)."""
    query = query.lower()
    return [m for m in movies if query in m["title"].lower()]
