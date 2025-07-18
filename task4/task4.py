import sys

def min_moves_to_equal(nums):
    """
    Находит минимальное количество ходов для приведения 
    всех элементов к одному числу
    """
    if not nums:
        return 0
    
    nums.sort()
    n = len(nums)
    
    if n % 2 == 1:
        median = nums[n // 2]
    else:
        median = nums[n // 2 - 1]
    
    moves = 0
    for num in nums:
        moves += abs(num - median)
    
    return moves

def read_numbers_from_file(filename):
    """Читает числа из файла"""
    numbers = []
    with open(filename, 'r') as f:
        for line in f:
            numbers.append(int(line.strip()))
    return numbers

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python task4.py <numbers_file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    numbers = read_numbers_from_file(filename)
    
    result = min_moves_to_equal(numbers)
    
    print(result)