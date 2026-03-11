def function_name(search:str, status:bool, *args:tuple, **kwargs:dict):
    result: list = []
    result_2: str = ""
    """
        Обрабатывает аргументы в зависимости от параметров search и status.

        Параметры:
            search (str): Строковый аргумент сравниваемый  "args" или "kwargs".
            status (bool): Логический аргумент влияющий на обработку args.
            *args (tuple): Произвольное количество позиционных аргументов.
            **kwargs (dict): Произвольное количество именованных аргументов.

        Возвращает:
                - Если search="args" и status=True: список целых чисел из args
                - Если search="args" и status=False: строка из всех args
                - Если search="kwargs": строка с информацией о ключах и значениях kwargs

        Исключения:
            ValueError: Если search не равен "args" или "kwargs"
            """
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