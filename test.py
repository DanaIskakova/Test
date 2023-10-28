from task import is_prime
from task import primes
from task import checksum
from task import pipeline

def test_is_prime():
    assert is_prime(0) == False
    assert is_prime(1) == True
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(7) == True
    assert is_prime(12) == False 
    
def test_primes():
    result = primes(10)
    assert len(result) == 10
    
    result = primes(1)
    assert len(result) == 1
    
def test_checksum():
    result = checksum([1, 2, 6, 24])
    assert result == 6012369

    result = checksum([])
    assert result == 0
    
def test_pipeline():
    result = pipeline()
    assert result == 7785816     
           
test_is_prime()
test_primes() 
test_checksum() 
test_pipeline()         