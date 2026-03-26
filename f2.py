import f1
import numpy as np

criteria = input("Введите критерии через запятую:\n").split(",")
criteria = [c.strip() for c in criteria]

alternatives = input("\nВведите альтернативы через запятую:\n").split(",")
alternatives = [a.strip() for a in alternatives]


# МАТРИЦА КРИТЕРИЕВ

print("\n=== Сравнение критериев ===")
criteria_matrix = f1.input_matrix(criteria)
criteria_weights = f1.priority_vector(criteria_matrix)


# МАТРИЦЫ АЛЬТЕРНАТИВ

alt_weights = []

for crit in criteria:
    print(f"\n=== Сравнение альтернатив по критерию: {crit} ===")
    matrix = f1.input_matrix(alternatives)
    weights = f1.priority_vector(matrix)
    alt_weights.append(weights)

alt_weights = np.array(alt_weights).T


# ИТОГ

final_scores = alt_weights.dot(criteria_weights)

# ВЫВОД

print("\nВеса критериев:")
for c, w in zip(criteria, criteria_weights):
    print(f"{c}: {w:.3f}")

print("\nИтоговые оценки альтернатив:")
for alt, score in zip(alternatives, final_scores):
    print(f"{alt}: {score:.3f}")

best = alternatives[np.argmax(final_scores)]
print(f"\nЛучший выбор: {best}")