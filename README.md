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

## Git

У репозиторії продемонстровано повний цикл роботи з гілками:
створення гілки → розробка → commit → push → merge → конфлікт →
вирішення конфлікту → rebase → cherry-pick → stash → видалення гілок.

### Гілки

| Гілка | Призначення |
|---|---|
| `main` | Основна гілка проєкту |
| `feature/movies` | Каталог фільмів: список, додавання, перегляд інформації (видалена після merge) |
| `feature/booking` | Бронювання: вибір фільму, кількості квитків, перегляд бронювань |
| `feature/cancel-booking` | Скасування бронювання з поверненням місць |
| `feature/search` | Пошук фільмів за назвою (паралельно з `feature/favorites` від одного коміту) |
| `feature/favorites` | Список обраних фільмів (паралельно з `feature/search` від одного коміту) |
| `feature/menu` | Перший варіант головного меню |
| `feature/menu-update` | Другий варіант головного меню |
| `feature/statistics` | Статистика: кількість фільмів, заброньованих квитків і вільних місць |
| `feature/discount` | Розрахунок знижки на квитки |
| `feature/ratings` | Оцінки фільмів (розробка з використанням stash) |
| `feature/test` | Модульні тести для бронювання |

### Merge-конфлікт

Конфлікт виник у `src/main.py` під час merge `feature/menu-update` у `main`
після того, як `feature/menu` вже була змерджена. Обидві гілки змінили один
і той самий фрагмент — тіло `print_menu()` та нумерацію пунктів у dispatch-циклі.

Вирішення: конфліктуючий код переглянуто за маркерами `<<<<<<<`, `=======`,
`>>>>>>>`, меню вручну об'єднано в повний варіант з усіма функціями
(перегляд, додавання, інформація, пошук, обране, бронювання, скасування,
вихід), нумерацію dispatch приведено у відповідність. Після `git add`
merge завершено комітом, роботу програми перевірено.

### Rebase

Гілку `feature/statistics` створено від `main`, у ній зроблено два коміти.
Після цього в `main` додано коміт з тестами (`Add unit tests for movie catalog`).
На `feature/statistics` виконано `git rebase main` — обидва коміти
відтворено поверх останнього коміту `main`, після чого гілку змерджено
fast-forward. Лінійність історії перевірено через
`git log --oneline --graph --all`.

### Cherry-pick

У гілці `feature/discount` створено коміт `Add ticket discount` з функцією
`calculate_discount()` у `src/booking.py`. Замість merge коміт перенесено
в `main` командою `git cherry-pick <hash>` — у `main` з'явився новий коміт
із тією самою зміною.

### Stash

Під час роботи над `feature/ratings` зміни в `src/movies.py` (функції
оцінок) тимчасово сховано через `git stash` без коміту. У `main` виконано
іншу роботу (коміт `Apply discount percent during booking`), після чого
зміни відновлено через `git stash pop` і фічу завершено.

### Видалення гілок

Після merge локальну гілку `feature/movies` видалено (`git branch -d`),
віддалену — `git push origin --delete feature/movies`. Локальну копію
`feature/test` відтворено з віддаленої через
`git switch -c feature/test origin/feature/test`.
