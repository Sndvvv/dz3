from typing import Any, Union, List, Tuple, Dict


def function_name(
        search: str,
        status: bool,
        *args: Any,
        **kwargs: Any
) -> Union[List[int], str]:
    """
    Обрабатывает аргументы в зависимости от параметров search и status.

    Параметры:
        search (str): Режим поиска. Может быть "args" или "kwargs".
        status (bool): Флаг, влияющий на обработку args.
        *args (Any): Произвольное количество позиционных аргументов.
        **kwargs (Any): Произвольное количество именованных аргументов.

    Возвращает:
        Union[List[int], str]:
            - Если search="args" и status=True: список целых чисел из args
            - Если search="args" и status=False: строка из всех args
            - Если search="kwargs": строка с информацией о ключах и значениях kwargs

    Исключения:
        ValueError: Если search не равен "args" или "kwargs"

    Примеры:
        >>> function_name("args", True, 1, 2, "a", 3.5)
        [1, 2, 3]

        >>> function_name("args", False, 1, 2, "a", 3.5)
        '12a3.5'

        >>> function_name("kwargs", True, name="John", age=30)
        'Key: name, Value: John; Key: age, Value: 30; '
    """
    # Аннотации для внутренних переменных
    result: List[int] = []
    result_2: str = ""

    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f"{i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += ("Key: {}, Value: {}; ".format(k, v))
        return result_2
    else:
        raise ValueError("Error for search")