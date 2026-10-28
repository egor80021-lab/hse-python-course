# task5.py — Домашняя работа 6, базовый уровень.
# Задача 5. Мини-парсер данных (строки + regex).


# ============================================================
# Задача 5. Мини-парсер данных (строки + regex)
# ============================================================
# На вход приходит строка с парами "ключ=значение", разделёнными ';'.
# Например: "name=Ira;age=20;city=Moscow".
#
# Подзадачи:
#   5.1. Вернуть список ключей.
#   5.2. Вернуть список значений.
#   5.3. Вернуть True, если все значения непустые.
#   5.4. Вернуть True, если строка содержит хотя бы одну цифру.
#   5.5. Вернуть True, если все ключи состоят только из латинских букв.

import re


def hw_5_1_keys(data: str) -> list[str]:
    """Вернуть список ключей."""
    # TODO: реализовать
    keys = []
    for pair in data.split(";"):
        key = pair.split("=", 1)[0]
        keys.append(key)
    return keys


def hw_5_2_values(data: str) -> list[str]:
    """Вернуть список значений."""
    # TODO: реализовать
    values = []
    for pair in data.split(";"):
        value = pair.split("=", 1)[1]
        values.append(value)
    return values


def hw_5_3_all_nonempty(data: str) -> bool:
    """Вернуть True, если все значения непустые."""
    # TODO: реализовать
    for value in hw_5_2_values(data):
        if value == "":
            return False
    return True


def hw_5_4_has_digit(data: str) -> bool:
    """Вернуть True, если в строке есть хотя бы одна цифра."""
    # TODO: реализовать
    return re.search(r"\d", data) is not None


def hw_5_5_keys_latin(data: str) -> bool:
    """Вернуть True, если все ключи — только латинские буквы."""
    # TODO: реализовать
    for key in hw_5_1_keys(data):
        if re.fullmatch(r"[A-Za-z]+", key) is None:
            return False
    return True


# ============================================================
# Assert-тесты
# ============================================================

if __name__ == "__main__":
    data = "name=Ira;age=20;city=Moscow"
    assert hw_5_1_keys(data) == ["name", "age", "city"]
    assert hw_5_2_values(data) == ["Ira", "20", "Moscow"]
    assert hw_5_3_all_nonempty(data) is True
    assert hw_5_3_all_nonempty("name=;age=20") is False
    assert hw_5_4_has_digit(data) is True
    assert hw_5_4_has_digit("name=Ira;city=Moscow") is False
    assert hw_5_5_keys_latin(data) is True
    assert hw_5_5_keys_latin("имя=Ira") is False

    print("task5: все assert-тесты пройдены.")
