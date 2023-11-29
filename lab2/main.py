from method_newton import method_newton
from simplified_method_newton import simplified_method_newton
from method_of_cutting import method_of_cutting

if __name__ == "__main__":
    result = method_of_cutting(x0=0, x1=2, e=0.1)
    print(f"Метод січних: x~{result[0]} {'(правильно)' if result[1] else '(не правильно)' }")
    result = simplified_method_newton(x=1, e=0.1)
    print(f"Спрощений метод Ньютона: x~{result[0]} {'(правильно)' if result[1] else '(не правильно)' }")
    result = method_newton(x=1, e=0.01)
    print(f"Метод Ньютона: x~{result[0]} {'(правильно)' if result[1] else '(не правильно)' }")
    