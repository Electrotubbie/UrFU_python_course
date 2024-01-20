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

def del_signs(text: str) -> str:
    unsigned = str() # обозначение переменной текста без знаков препинания
    for literal in text: # перебор символов в тексте
        if literal.isalpha():
            unsigned += literal
        else: # если символ не буква, то
            if unsigned[-1] == ' ':
                continue # продолжаем перебор символов без замены на пробел
            else:
                unsigned += ' ' # замена знака на пробел
    return unsigned.strip()

def cut_in_parts(text: str, separator: str) -> (list, int):
    cut_text = text.split(separator)
    return cut_text, len(cut_text)

def count_word(text: str) -> dict:
    text_list = cut_in_parts(del_signs(text.lower()), ' ')[0] # удаление пробелов и создание списка из слов в тексте
    word_stat = dict()
    for word in set(text_list):
        word_stat[word] = text_list.count(word) # генерация словаря с счётчиками слов
    return dict(sorted(word_stat.items()))

# print(del_signs(st))
# print(cut_in_parts(st, ' '))
# print(*count_word(st).items(),sep='\n')
