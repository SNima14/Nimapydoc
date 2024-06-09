"""
        |>||=====================||<|
        |                           |
        |     ___      ___  ___     |
        |    /  /|    /  /||\  \    |
        |   /  / /   /  // \ \  \   |
        |  /  / /   /  //   \ \  \  |
        | |\  \/   /  //     \/  /| |
        | \ \  \  /_ //      /  //  |
        |  \ \__\|__|/      /_ //   |
        |   \|__|          |__|/    |
        |                           |
        |>||=====================||<|

    <-- >>================<>================<< -->
    <-- || ███╗   ██╗██╗███╗   ███╗ █████╗  || -->
    <-- || ████╗  ██║██║████╗ ████║██╔══██╗ || -->
    <-- || ██╔██╗ ██║██║██╔████╔██║███████║ || -->
    <-- || ██║╚██╗██║██║██║╚██╔╝██║██╔══██║ || -->
    <-- || ██║ ╚████║██║██║ ╚═╝ ██║██║  ██║ || --> 
    <-- || ╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ || -->
    <-- >>================<>================<< -->
    

        Coding is not just a profession;
        it's a passion and a way of life!

         ||===========================||
          |  Written by:              |
          |  ~~>  NIMA HOMAM !        |
         ||===========================||
          | Version: 1.1.1            |
          | Date:6/9/2024             |             
         ||===========================||
"""

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
# def no_problem():
#     for i in range(100000):
#         ...
#     return None

# @MyDecorator.retry()
# @MyDecorator.timer
# def main():
#     problem()
#     no_problem()

# if __name__ == "__main__":
#     main()
