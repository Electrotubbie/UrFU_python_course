# Задание 2
## Коллекции

Воспользуйтесь кодом:

```python
st = "Я помню чудное мгновенье:\n\
Передо мной явилась ты,\n\
Как мимолетное виденье,\n\
Как гений чистой красоты.\n\
\n\
В томленьях грусти безнадежной,\n\
В тревогах шумной суеты,\n\
Звучал мне долго голос нежный\n\
И снились милые черты.\n\
\n\
Шли годы. Бурь порыв мятежный\n\
Рассеял прежние мечты,\n\
И я забыл твой голос нежный,\n\
Твои небесные черты.\n\
\n\
В глуши, во мраке заточенья\n\
Тянулись тихо дни мои\n\
Без божества, без вдохновенья,\n\
Без слез, без жизни, без любви.\n\
\n\
Душе настало пробужденье:\n\
И вот опять явилась ты,\n\
Как мимолетное виденье,\n\
Как гений чистой красоты.\n\
\n\
И сердце бьется в упоенье,\n\
И для него воскресли вновь\n\
И божество, и вдохновенье,\n\
И жизнь, и слезы, и любовь."

print(st)
```

1. Необходимо написать функцию, которая получает строку, заменяет в 
ней
    - все знаки препинания и переходы строк на « », 
    - устраняет множественные пробелы, и возвращает эту строку.

2. Необходимо написать функцию, которая получает строку, разрезает её по переданному разделителю, возвращает список из подстрок – «слов», и количество подстрок.

3. Написать код, который использует описанные выше функции для создания упорядоченного по алфавиту словаря с частотой использованных слов. Словарь должен быть регистронезависимым («Без» и «без» - это одно слово)