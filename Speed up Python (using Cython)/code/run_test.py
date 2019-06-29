import sys
import timeit
import pyximport

pyximport.install(build_dir="./build")


def test(n: int):
    py_time = timeit.timeit(
        f"fibonacci_series({n})", setup="from pure_python import fibonacci_series", number=1000)
    cy_time = timeit.timeit(
        f"fibonacci_series({n})", setup="from cython_implementation import fibonacci_series", number=1000)
    return py_time, cy_time


def main():
    try:
        arg = sys.argv[1]
        py_time, cy_time = test(int(arg))
        print(f"Python test took {py_time} secs")
        print(f"Cython test took {cy_time} secs")
        print(f"Cython speed up over Python : {py_time/cy_time} times")
    except IndexError:
        print("please pass int argument")


if __name__ == "__main__":
    main()
