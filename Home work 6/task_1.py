# 1- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


from typing import List

def find_second_index(list_strings:List[str], search_word:str) -> int:
    count = 0
    for k, item in enumerate(list_strings):
        if item == search_word:
            count += 1
        if count ==2:
            return k
    return -1

print(find_second_index(["qwe", "asd", "zxc", "qwe", "ertqwe"], "qwe"))
print(find_second_index(["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], "йцу"))

