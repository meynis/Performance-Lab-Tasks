import sys

def circular_array_path(n, m):
    """
    Находит путь в круговом массиве
    n - размер массива (1 до n)
    m - длина интервала
    """
    path = []
    current = 0
    
    while True:
        path.append(current + 1)
        current = (current + m) % n
        
        if current == 0:
            break
    
    return path

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python task1.py <n> <m>")
        sys.exit(1)
    
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    
    result = circular_array_path(n, m)
    print(''.join(map(str, result)))