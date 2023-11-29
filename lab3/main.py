from method_newton import method_newton
from method_of_cutting import method_of_cutting
from simplified_method_newton import simplified_method_newton

if __name__ == "__main__":
    print(
        "Метод Ньютона: ", method_newton(x0=(1, 1), e=0.01), "\n",
        "Спрощений метод Ньютона: ", simplified_method_newton(x0=(1, 1), e=0.01), "\n",
        "Метод січних: ", method_of_cutting(x0=(1, 1), e=0.01), "\n",
        sep=""
    )