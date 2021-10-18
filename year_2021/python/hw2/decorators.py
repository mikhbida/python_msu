

def call_controller(n_calls: int, time_interval: int):
    import time
    """
    Напишите функцию декоратор, которая ограничивает количество вызовов функции.
    ```
    n_calls: количество возможнх вызовов
    time_interval: время в секундах
    ```
    ```
    @firewall(10, 20):
    def foo():
      pass
    ```
    """
    count = [0]

    def _inner_decorator(fn):
        def _inner_function(*args, **kwargs):
            print(f'Sleeping for <{time_interval}> seconds')
            time.sleep(time_interval)
            print('I am trying to run')
            if count[0] < n_calls:
                count[0] += 1
                print(f'Attempt <{count[0]}>')
                return fn(*args, **kwargs)
            else:
                print(f'Limit exceeded after <{count[0]}> attempts')
                return 

        return _inner_function

    return _inner_decorator
