# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы 
# фамилии тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Энакин Скайуокер 5
# Фредди Меркури 3
# Александр Пушкин 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3
# Александр Пушкин 4

def get_list_data(filename: str) -> list[str]:
    """
    функция список из строк файла
    arg - имя файла
    return - список из строк файла

    """
    with open(filename, encoding='utf-8') as file:
        return file.read().split('\n')
    
def elements_to_caps(lst: list, element) -> list[str]:
    """
    функция переводит в верхний регистр строку при условии наличия в строке заданного значения
    arg - список list, trigger_str - значение, из-за которого будет переводиться текст в верх.рег.
    return - список с измененными на верхний регистр строк, если условие trigger_str 
    выполнилось  
    
    """
    for i in range(len(lst)):
        if element in list[i]:
            lst[i] = lst[i].upper()
    return lst

lst = get_list_data(r"C:\Users\Марина\OneDrive\Рабочий стол\курсы\1. Тестирование_GB\1. введение в phyton\home work\Home work 4\students_marks.txt")
print(elements_to_caps(lst, '5'))


