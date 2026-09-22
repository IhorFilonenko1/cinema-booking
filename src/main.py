"""Точка входу застосунку Cinema Booking."""

import movies


def print_menu():
    print("\n=== Cinema Booking ===")
    print("1] Список фільмів")
    print("2] Додати фільм")
    print("3] Інформація про фільм")
    print("0] Вихід")


def show_movies():
    for m in movies.list_movies():
        print(
            f'{m["id"]}. {m["title"]} ({m["year"]}, {m["genre"]}) '
            f'— {m["duration"]} хв, місць: {m["seats"]}, ціна: {m["price"]:.2f}'
        )


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


def main():
    while True:
        print_menu()
        choice = input("Оберіть опцію: ").strip()
        if choice == "1":
            show_movies()
        elif choice == "2":
            add_movie_prompt()
        elif choice == "3":
            movie_info_prompt()
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Невідома опція.")


if __name__ == "__main__":
    main()
