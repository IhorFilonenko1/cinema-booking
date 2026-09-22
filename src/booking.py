"""Бронювання квитків."""

import movies

bookings = []

_next_booking_id = 1


def choose_movie(movie_id):
    """Вибір фільму для бронювання."""
    return movies.get_movie(movie_id)


def book_tickets(movie_id, tickets, discount_percent=0):
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
        "total": calculate_discount(movie["price"] * tickets, discount_percent),
    }
    _next_booking_id += 1
    bookings.append(booking)
    return booking


def get_bookings():
    """Повертає список усіх бронювань."""
    return bookings


def cancel_booking(booking_id):
    """Скасовує бронювання та повертає місця у фільм."""
    for booking in bookings:
        if booking["id"] == booking_id:
            movie = movies.get_movie(booking["movie_id"])
            if movie is not None:
                movie["seats"] += booking["tickets"]
            bookings.remove(booking)
            return booking
    return None


def get_statistics():
    """Загальна статистика кінотеатру."""
    return {
        "movies": len(movies.list_movies()),
        "booked_tickets": sum(b["tickets"] for b in bookings),
        "free_seats": sum(m["seats"] for m in movies.list_movies()),
    }


def calculate_discount(total_price, percent):
    """Розраховує суму з урахуванням знижки у відсотках."""
    if percent <= 0:
        return round(total_price, 2)
    if percent > 100:
        percent = 100
    return round(total_price * (100 - percent) / 100, 2)
