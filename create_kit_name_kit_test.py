import sender_stand_request
import data


# функция меняет значение в параметре name из тела kit_body вкладка data
def get_kit_body(name):
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_body = data.kit_body.copy()
    # изменение значения в name
    current_body["name"] = name
    # возвращается новый словарь с нужным значением name
    return current_body


# Функция для позитивной проверки по вводимым символам
# Проверка успешного создания набора с измененным именем под авторизованным пользователем code = 201
def positive_assert(name):
    # в переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body(name)
    # в переменную kit_response сохраняется результат запроса на создание набора под авторизованным пользователем
    kit_response = sender_stand_request.post_new_client_kit(kit_body) #get_new_user_token())
    # Проверить код ответа
    assert kit_response.status_code == 201
    # Проверить, что имя в ответе совпадает с именем в запросе
    assert kit_response.json()["name"] == kit_body["name"]


# Функция для негативной проверки по вводимым символам
# Ошибка. Набор не создан под авторизованным пользователем code = 400 при введеных/не введенных символах
def negative_assert(kit_body):
    # в переменную kit_response сохраняется результат запроса на создание набора под авторизованным пользователем
    kit_response = sender_stand_request.post_new_client_kit(kit_body) #get_new_user_token())
    # Проверить код ответа
    assert kit_response.status_code == 400
    # Проверка, что в теле ответа "code" равен 400
    assert kit_response.json()["code"] == 400


# Тест 1. Допустимое количество символов (1)

def test1_name_created_kit_1_letter_get_success_response():
    positive_assert("а")

# Тест 2. Допустимое количество символов (511)

def test2_name_created_kit_511_letter_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Тест 3. Количество символов меньше допустимого (0) (выдаст ошибку)

def test3_name_created_kit_empty_get_error_response():
    kit_body = get_kit_body("")
    negative_assert(kit_body)

# Тест 4. Количество символов больше допустимого (512)

def test4_name_created_kit_512_letter_get_error_response():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert(kit_body)

# Тест 5. Разрешены английские буквы

def test5_name_created_kit_from_english_letter_get_success_response():
    positive_assert("QWErty")

# Тест 6. Разрешены русские буквы

def test6_name_created_kit_from_russian_letter_get_success_response():
    positive_assert("Мария")

# Тест 7. Разрешены спецсимволы

def test7_name_created_kit_from_special_simbol_get_success_response():
    positive_assert("\"№%@\",")

# Тест 8. Разрешены пробелы

def test8_name_created_kit_with_space_get_success_response():
    positive_assert("Человек и Ко")

# Тест 9. Разрешены цифры

def test9_name_created_kit_with_numbers_get_success_response():
    positive_assert("123")

# Тест 10. Ошибка. Параметр не передан в запросе

def test10_client_kit_with_no_name_get_error_response():
    # Копируется словарь с телом запроса из файла data в переменную user_body
    kit_body = data.kit_body.copy()
    # Удаление параметра name из запроса
    kit_body.pop("name")
    # Проверка полученного ответа
    negative_assert(kit_body)

# Тест 11. Ошибка. Передан другой тип параметра

def test11_create_client_kit_name_number_type_get_error_response():
    kit_body = get_kit_body(123)
    negative_assert(kit_body)
