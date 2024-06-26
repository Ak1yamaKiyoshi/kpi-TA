 
```
Завдання:

Допоможіть армаді з найменшими втратами перемогти піратів. Армада має кораблі з
різною кількістю моряків. Адміральський корвет має середню кількість моряків в
порівнянні з іншими. Перемогти піратське судно може лише корабель з неменшим
числом моряків, але зайві задіяні люди не допустимі. Кількість піратів на судні
задається з клавіатури. Сигнал для атаки подає адміральський корвет, йому необхідно
обрати відповідний корабель. За допомогою прапорців кожен з кораблів може
зв’язатися лише з двома кораблями та отримати дані про кількість матросів. Команда
атаки передається ланцюжком між кораблями. Якщо кількість матросів не відповідає
кількості піратів з’являється новий корабель з відповідною кількістю і сигнал на атаку
повторюється. Для обох випадків показати шлях проходження сигналу.
```

- Піратське судно - Шукане число.
- Адміральский корвет - Скоріше за все корінь дерева з середнім значенням. 
- Армада - Вузли дерева. 
- Прапорці - Це зв'язок між кораблями, тобто дерево може бути лише бінарним

- Алгоритм додавання нового корабля див у прикладі 3.
- ! Там помилка у розрахунках, але сенс той же

## Приклад 1 
- Адміральский корвет - [15]
- Піратське судно - [18]

```
Армада:
        [25]
    [20]<
        [17]
[15]<
        [13]
    [10]<
        [7]
```
- Шлях:
- 15 10 | 25 > 18

## Приклад 2
- Адміральский корвет - [15]
- Піратське судно - [39]

```
Армада:
        [25]
    [20]<
        [17]
[15]<
        [13]
    [10]<
        [7] 
```
- Шлях:
- 15 10 13 | 38 (сумма) - Недостатня кількість. 
- 15 20 17 | 52 (сумма) - Достатня кількість.

## Приклад 3 
- Адміральский корвет - [15]
- Піратське судно - [71]

```
Армада:
        [25]
    [20]<
        [17]
[15]<
        [13]
    [10]<
        [7] 
```
- Шлях:
- 15 20 25 | 70 - Недостатня кількість 
- Обходимо всі шляхи та записуємо їй суми:
- маленькі пропущено . . . 32, 38, 52, 70
- Листкові вузли: 7 13 17 25 

- 71 - 32 = 39 додаємо до дерева, максимальний шлях після цього: 99
- 71 - 38 = 33 додаємо до дерева, максимальний шлях після цього: 93
- 71 - 52 = 19 додаємо до дерева, максимальний шлях після цього: 71
- 71 - 70 = 1  додаємо до дерева, максимальний шлях після цього: 60

- Рахуємо найменшу помилку, і додаємо відповідний корабель до армади. 
- 71 == 71, тобто у дерево додаємо 19.
```
        [25]<
    [20]<
            [19]<
        [17]<
[15]<
        [13]<
    [10]<
        [7]<
```