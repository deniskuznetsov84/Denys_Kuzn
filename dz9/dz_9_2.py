#2 Напишіть клас TextProcessor для обробки текстових даних. Клас повинен мати публічний
# метод get_clean_string, який видалить всі знаки пунктуації з рядка, який передається йому аргументом,
# та приватним методом is_punktuation, який безпосередньо перевіряє символ на рівність зі знаками пунктуації
# та повертає True/False, який, в свою чергу, є приватним або захищеним атрибутом.
# Потім напишіть клас TextLoader, який має приватний атрибут text_processor, який є об'єктом класу TextProcessor.
# Клас TextLoader повинен мати приватний атрибут clean_string і публічний метод set_clean_text, який буде викликати
# метод класу TextProcessor через свій атрибут text_processor і записувати значення в clean_string. Створіть
# додатковий property для clean_string, який буде виводити повідомлення в консоль про те, що виводиться вже
# очищений текст.
# Напишіть клас DataInterface, в якому буде захищений атрибут, що є екземпляром класу TextLoader, а також публічний
# метод process_texts, який буде приймати список рядків, опрацьовувати їх у циклі і виводити значення в консоль.

class TextProcessor:
    def __init__(self):
        self._punctuation_marks = '_-\.,!?;:*/()'

    def __is_punktuation(self, marks):
        if marks in self._punctuation_marks:
            return True
        return False

    def get_clean_string(self, text):
        clean_text = ""
        for i in text:
            if self.__is_punktuation(i):
                continue
            clean_text += i
        return clean_text

class TextLoader:
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = None

    def set_clean_text(self, text):
        self.__clean_string = self.__text_processor.get_clean_string(text)

    @property
    def clean_string(self):
        print(f'Clean string is: {self.__clean_string}')
        return self.__clean_string

class DataInterface:
    def __init__(self):
        self.__text_loader = TextLoader()

    def process_texts(self, texts):
        clean_texts = []
        for i in texts:
            self.__text_loader.set_clean_text(i)
            clean = self.__text_loader.clean_string
            clean_texts.append(clean)
        return clean_texts

a = DataInterface()
t = ['True/False, який, в свою чергу, є', 'метод set_clean_text, який', 'метод process_texts, який']
a.process_texts(t)