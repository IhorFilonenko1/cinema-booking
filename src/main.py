"""Точка входу застосунку Cinema Booking."""

import booking
import movies


def print_menu():
    print("\n=== Cinema Booking ===")
    print("1] Список фільмів")
    print("8] Обрані фільми")
    print("2] Додати фільм")
    print("3] Інформація про фільм")
    print("4] Забронювати квиток")
    print("5] Мої бронювання")
    print("6] Скасувати бронювання")
    print("7] Пошук фільмів")
    print("0] Вихід")


def show_movies():
    for m in movies.list_movies():
        print(
            f'{m["id"]}. {m["title"]} ({m["year"]}, {m["genre"]}) '
            f'— {m["duration"]} хв, місць: {m["seats"]}, ціна: {m["price"]:.2f}'
        )


def favorites_prompt():
    for m in movies.list_favorites():
        print(f'{m["id"]}. {m["title"]} ({m["year"]})')
    movie_id = input("ID фільму, щоб додати в обране (Enter — пропустити): ").strip()
    if movie_id:
        movie = movies.add_to_favorites(int(movie_id))
        if movie is None:
            print("Фільм не знайдено або вже в обраному.")
        else:
            print(f'"{movie["title"]}" додано в обране.')


def add_movie_prompt():
    title = input("Назва: ").strip()
    genre = input("Жанр: ").strip()
    year = int(input("Рік: "))
    duration = int(input("Тривалість (хв): "))
    seats = int(input("Кількість місць: "))
    price = float(input("Ціна квитка: "))
    movie = movies.add_movie(title, genre, year, duration, seats, price)
    print(f'Додано фільм "{movie["title"]}" з id {movie["id"]}')


def movie_info_prompt():
    movie_id = int(input("ID фільму: "))
    movie = movies.get_movie(movie_id)
    if movie is None:
        print("Фільм не знайдено.")
        return
    print(
        f'{movie["title"]} ({movie["year"]})\n'
        f'Жанр: {movie["genre"]}\n'
        f'Тривалість: {movie["duration"]} хв\n'
        f'Вільних місць: {movie["seats"]}\n'
        f'Ціна квитка: {movie["price"]:.2f}'
    )


def book_tickets_prompt():
    show_movies()
    movie_id = int(input("ID фільму: "))
    movie = booking.choose_movie(movie_id)
    if movie is None:
        print("Фільм не знайдено.")
        return
    tickets = int(input("Кількість квитків: "))
    result = booking.book_tickets(movie_id, tickets)
    if result is None:
        print("Не вдалося забронювати: недостатньо вільних місць.")
        return
    print(
        f'Заброньовано {result["tickets"]} квитк(ів) на "{result["title"]}". '
        f'Сума: {result["total"]:.2f}. № бронювання: {result["id"]}'
    )


def show_bookings():
    for b in booking.get_bookings():
        print(
            f'№{b["id"]}: {b["title"]} — {b["tickets"]} квитк(ів), '
            f'сума {b["total"]:.2f}'
        )


def cancel_booking_prompt():
    show_bookings()
    booking_id = int(input("№ бронювання: "))
    cancelled = booking.cancel_booking(booking_id)
    if cancelled is None:
        print("Бронювання не знайдено.")
        return
    print(f'Скасовано бронювання №{cancelled["id"]} ({cancelled["title"]}).')


def search_prompt():
    query = input("Назва або частина назви: ").strip()
    results = movies.search_movies(query)
    if not results:
        print("Нічого не знайдено.")
        return
    for m in results:
        print(f'{m["id"]}. {m["title"]} ({m["year"]}) — місць: {m["seats"]}')


def main():
    while True:
        print_menu()
        choice = input("Оберіть опцію: ").strip()
        if choice == "1":
            show_movies()
        elif choice == "8":
            favorites_prompt()
        elif choice == "2":
            add_movie_prompt()
        elif choice == "3":
            movie_info_prompt()
        elif choice == "4":
            book_tickets_prompt()
        elif choice == "5":
            show_bookings()
        elif choice == "6":
            cancel_booking_prompt()
        elif choice == "7":
            search_prompt()
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Невідома опція.")


if __name__ == "__main__":
    main()
