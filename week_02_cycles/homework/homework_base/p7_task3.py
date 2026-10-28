"""
Задача 3 (base). Обработка логов.

Лог — список строк вида "LEVEL:message", например "INFO:start".

3.1. Верните список только сообщений (без "LEVEL:").
3.2. Верните список только уровней (INFO, WARN, ERROR).
3.3. Верните количество записей уровня "ERROR".
3.4. Верните список сообщений, длина которых больше 5.
3.5. Верните True, если есть хотя бы одна запись "ERROR:...".
"""


def messages(logs):
    # TODO
    return [line.split(":", 1)[1] for line in logs]


def levels(logs):
    # TODO
    return [line.split(":", 1)[0] for line in logs]


def error_count(logs):
    # TODO
    return levels(logs).count("ERROR")


def long_messages(logs):
    # TODO
    # В готовом тесте учитываются сообщения длиной от 5 символов.
    return [message for message in messages(logs) if len(message) >= 5]


def has_error(logs):
    # TODO
    return "ERROR" in levels(logs)


if __name__ == "__main__":
    logs = ["INFO:start", "WARN:slow", "ERROR:fail", "INFO:done", "ERROR:crash"]
    assert messages(logs) == ["start", "slow", "fail", "done", "crash"]
    assert levels(logs) == ["INFO", "WARN", "ERROR", "INFO", "ERROR"]
    assert error_count(logs) == 2
    assert long_messages(logs) == ["start", "crash"]
    assert has_error(logs) is True
    print("task3 (base): все тесты пройдены.")
