def pprint(matrix: list[list[float]]) -> None:
    for line in matrix:
        line = [str(round(num, 1)) for num in line]
        print("|", " | ".join(line), "|")
    print()


def determinant(matrix: list[list[float]]) -> float:
    n = len(matrix)
    det = 1
    v = matrix.copy()

    for k in range(0, n):
        print(f"Крок: {k + 1}")

        max = abs(v[k][k])
        w = k
        for l in range(k + 1, n):
            if max < v[k][l]:
                max = v[k][l]
                w = l
        for d in range(n):
            v[d][k], v[d][w] = v[d][w], v[d][k]

        det = det * ((-1) ** (w + k)) * v[k][k]

        for i in range(k + 1, n):
            factor = v[i][k] / v[k][k]
            for j in range(k, n):
                v[i][j] -= factor * v[k][j]
        pprint(v)

    return round(det, 3)


def get_matrix(k: int) -> list[list[float]]:
    s = 0.02 * k
    return [
        [8.30, 2.62 + s, 4.10, 1.90],
        [3.92, 8.45, 7.78 - s, 2.46],
        [3.77, 7.21 + s, 8.04, 2.28],
        [2.21, 3.65 - s, 1.69, 6.69],
    ]


matrix = get_matrix(7)
print("Вхідна матриця:")
pprint(matrix)

det = determinant(matrix)
print(f"Визначник матриці: {det}")
