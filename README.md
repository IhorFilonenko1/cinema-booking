# Cinema Booking

Консольний застосунок на Python для кінотеатру: каталог фільмів, бронювання та скасування квитків, пошук, обране, статистика та знижки.

## Структура

```
cinema-booking/
├── src/
│   ├── main.py      # точка входу, головне меню
│   ├── movies.py    # каталог фільмів, пошук, обране, оцінки
│   └── booking.py   # бронювання, скасування, знижки, статистика
├── tests/
├── .gitignore
└── README.md
```

## Запуск

```bash
python src/main.py
```

## Тести

```bash
python -m unittest discover tests
```
