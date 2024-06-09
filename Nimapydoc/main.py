import time
from typing import Callable, Any
import six


class MyDecorator:
    def __init__(self) -> None:
        pass

    @staticmethod
    def timer(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            t1 = time.time()
            result = func(*args, **kwargs)
            t2 = time.time() - t1

            if func.__name__ == "main":
                print(f"Total time of program: {t2:.3f}sec")
            else:
                print(f"Time of {func.__name__} function: {t2:.3f}")

            return result

        wrapper.__name__ = func.__name__  # not sure about here
        return wrapper

    @staticmethod
    def retry(retries: int | float = 3, delay: int | float = 1) -> Callable:

        if retries <= 0 or delay <= 0:
            raise ValueError(
                "Retries must be greater than 0 and delay must be positive."
            )

        def decorator(func: Callable) -> Callable:
            def wrapper(*args, **kwargs) -> Any:

                for i in range(retries):

                    try:
                        print(f"Running {func.__name__} function!")
                        return func(*args, **kwargs)
                    except Exception as e:
                        if i == retries - 1:
                            print(f"Error:{repr(e)}.")
                            print(
                                f"{func.__name__} function failed after {retries} retries."
                            )
                            break
                        else:
                            print(f"Error: {repr(e)} -> Retrying...")
                            time.sleep(delay)

            wrapper.__name__ = func.__name__  # not sure about here
            return wrapper

        return decorator
    
    @staticmethod
    def repeat(repeats: int = 2, delay: int | float = 0) -> Callable:

        if not isinstance(repeats, int) or repeats <= 0 or delay < 0:
            raise ValueError("Repeats must be a positive integer and delay non-negative.")

        def decorator(func: Callable) -> Callable:
            def wrapper(*args, **kwargs) -> Any:
                result = None
                for i in range(repeats):
                    result = func(*args, **kwargs)
                    if delay > 0:
                        time.sleep(delay)
                return result

            wrapper.__name__ = func.__name__
            return wrapper

        return decorator


"""
        ||> This section is for testing purposes.
        ||> It will not be included in your main file.
        ||> However, if you uncomment it and run this file, they will be executed!
        ||> So, watch out and code wisely!

        >===>>=================<<==<
        |      Let's dive in!      |
        >===>>================<<===<
"""

# @MyDecorator.retry()
# def problem():
#     time.sleep(1)
#     raise Exception("connecting...")

# @MyDecorator.retry()
# @MyDecorator.timer
# @MyDecorator.repeat(delay=0,repeats=5)
# def no_problem():
#     for i in range(100000):
#         ...
#     print("h")
#     return 5

# @MyDecorator.retry()
# @MyDecorator.timer
# def main():
#     problem()
#     a=no_problem()
#     print(a)

# if __name__ == "__main__":
#     main()
