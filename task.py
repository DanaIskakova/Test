import random

#1. Функция проверки простоты: is_prime(x: int) -> bool
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#2. Функция генерации списка простых чисел: primes(count: int) -> List[int]
def primes(count: int) -> list[int]:
    """Генерация списка простых чисел"""
    primes_list = []
    num = 2
    while len(primes_list) < count:
        if is_prime(num):
            primes_list.append(num)
        num += 1
        
    random.seed(100)
    random.shuffle(primes_list)
    
    return primes_list

#3. Функция расчёта контрольной суммы: checksum(x: List[int]) -> int
def checksum(x: list[int]) -> int:
    res = 0
    for elem in x:
        res += elem
        res *=113
        res %=10000007
    return res    

#4. Функция, которая выполняет все требуемые действия и возвращает контрольную сумму результата pipeline() -> int
def pipeline() -> int:
    # Генерация списка из 1000 первых простых чисел
    primes_list_1000 = primes(1000)
    return checksum(primes_list_1000)
    
def main():
    print(pipeline())

if __name__ =='__main__':
    exit(main())   