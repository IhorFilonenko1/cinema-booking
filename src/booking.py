"""Бронювання квитків."""

import movies

bookings = []

_next_booking_id = 1


def choose_movie(movie_id):
    """Вибір фільму для бронювання."""
    return movies.get_movie(movie_id)


def book_tickets(movie_id, tickets):
    """Бронює квитки на фільм. Повертає бронювання або None."""
    global _next_booking_id
    movie = movies.get_movie(movie_id)
    if movie is None:
        return None
    if tickets <= 0 or tickets > movie["seats"]:
        return None
    movie["seats"] -= tickets
    booking = {
        "id": _next_booking_id,
        "movie_id": movie_id,
        "title": movie["title"],
        "tickets": tickets,
        "total": round(movie["price"] * tickets, 2),
    }
    _next_booking_id += 1
    bookings.append(booking)
    return booking


def get_bookings():
    """Повертає список усіх бронювань."""
    return bookings
