import math

def solve_biquad(a, b, c):
    if a == 0:
        return "Коэффициент a не может быть равен нулю."
    
    # Преобразуем к виду y^2 + (b/a)*y + c/a = 0
    A = b / a
    B = c / a
    
    # Находим дискриминант нового квадратного уравнения
    D = A**2 - 4*B
    
    if D < 0:
        return "Действительных корней нет."
    
    # Найденные корни y1 и y2
    y1 = (-A + math.sqrt(D)) / 2
    y2 = (-A - math.sqrt(D)) / 2
    
    roots = []
    
    # Проверяем, являются ли корни положительными
    if y1 >= 0:
        roots.append(math.sqrt(y1))
        roots.append(-math.sqrt(y1))
        
    if y2 >= 0:
        roots.append(math.sqrt(y2))
        roots.append(-math.sqrt(y2))
    
    if len(roots) > 0:
        return sorted(set(roots))
    else:
        return "Действительных корней нет."

# Пример использования функции
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

result = solve_biquad(a, b, c)
print(result)