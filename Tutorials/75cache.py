import functools
import time
from functools import lru_cache

@lru_cache(maxsize=3)  # no.s of last calls saved in memory (includes function calls)

def f1():
    # ASSUME SOME HEAVY WORK TAKING 3 SECONDS!
    time.sleep(3)

    print("Text Files")

if __name__ == "__main__":

    f1()
    print('Calling Again!')

    # using lru cache  f1() will not be executed again ;  but result of previous call will be shown
    f1()
    print('Done')