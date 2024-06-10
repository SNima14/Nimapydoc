import time
from typing import Callable, Any


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
    
    @staticmethod
    def createFuncVersion(first_var: int = 1, second_var: int = 1, third_var: int = 1) -> Callable:
        def decorator(func: Callable) -> Callable:
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            wrapper.version = YourPersonalVersion(first_var, second_var, third_var)
            wrapper.__name__ = func.__name__
            return wrapper

        return decorator
    

class YourPersonalVersion:
    def __init__(self, first: int = 1, second: int = 1, third: int = 1) -> None:
        if not isinstance(first, int) or not isinstance(second, int) or not isinstance(third, int):
            raise TypeError("You can only enter integers!")

        if first <= 0 or second <= 0 or third <= 0:
            raise ValueError("Invalid number or numbers entered!")

        self.first = first
        self.second = second
        self.third = third

    def __str__(self) -> str:
        return f"{self.first}.{self.second}.{self.third}"

    def __repr__(self) -> str:
        return f"version of {self}: {self.first}.{self.second}.{self.third}"

    def __int__(self) -> int:
        try:
            return int(f"{self.first}{self.second}{self.third}")
        except Exception as e:
            print(f"Can't convert {self} to int: {e}")
            return None

    def __gt__(self, other) -> bool:
        if not isinstance(other, YourPersonalVersion):
            raise ValueError("You can only compare two versions with each other!")

        if self.first != other.first:
            return self.first > other.first
        elif self.second != other.second:
            return self.second > other.second
        else:
            return self.third > other.third

    def __lt__(self, other) -> bool:
        if not isinstance(other, YourPersonalVersion):
            raise ValueError("You can only compare two versions with each other!")

        if self.first != other.first:
            return self.first < other.first
        elif self.second != other.second:
            return self.second < other.second
        else:
            return self.third < other.third

    def __eq__(self, other) -> bool:
        if not isinstance(other, YourPersonalVersion):
            raise ValueError("You can only compare two versions with each other!")

        return self.first == other.first and self.second == other.second and self.third == other.third



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
# @MyDecorator.createFuncVersion()
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
#     print(repr(no_problem.version) +"  " +str(a) )

# if __name__ == "__main__":
#     main()
