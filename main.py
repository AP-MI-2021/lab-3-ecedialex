from typing import List
def show_menu():
    print('1. Citire lista')
    print('2. Afisare cea mai lunga subsecventa cu toate numerele pare. (ex.10)')
    print('3. Afisare cea mai lunga subsecventa cu numere ce au aceelasi numar de divizori. (ex.12)')
    print('4. Afisare cea mai lunga subsecventa cu numere formate din cifre prime. (ex.13)')
    print('x. Exit.')
def read_list() -> List[int]:
    lst = []
    lst_str = input('Dati numerele separate prin spatiu:')
    lst_str_split = lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst

def get_longest_all_even(lst: List[int]) -> List[int]:
    '''
    Determina cea mai lunga subsecventa in care toate elementele cifre pare.
    :param lst: lista in care se cauta subsecventa
    :return: subsecventa gasita
    '''

    n = len(lst)
    result = []
    for st in range(n):
        for dr in range(st, n):
            all_even = True
            for num in lst[st:dr+1]:
                if num % 2 != 0:
                    all_even = False
                    break
            if all_even:
                if dr - st + 1 > len(result):
                    result = lst[st:dr+1]
    return result

def test_get_longest_all_even():
    assert get_longest_all_even([1, 2, 3, 4, 5]) == [2]
    assert get_longest_all_even([1,2,3,4,6,8,6]) == [4,6,8,6]
    assert get_longest_all_even([1, 3 ,5 ,7]) == []
    assert get_longest_all_even([1,2,3,4,10,20,30,40,5]) == [4,10,20,30,40]

def div_count(n):
    """
    Returneaza numarul de divizori ai unui numar citit
    :param n: numar citit
    :return: numarul de divizori ai lui n
    """
    d=0
    for i in range (1,(int)(n**0.5)+1):
        if n%i ==0:
            if n/i == i:
                d=d+1
            else:
                d=d+2
    return d

def get_longest_same_div_count(lst: List[int]) -> List[int]:
    """
    Determina cea mai lunga subsecventa in care toate elementele au aceelasi numar de divizori
    :param lst:
    :return:
    """
    n=len(lst)
    result=[]
    for st in range(n):
        for dr in range(st,n):
            d=div_count(lst[st])
            for num in lst[st:dr+1]:
                if div_count(num) != d:
                    d=-1
                    break

            if(d!=-1):
                if dr - st +1 > len(result):
                    result = lst[st:dr+1]
    return result
def test_get_longest_same_div_count():
    assert get_longest_same_div_count([2, 2, 2, 2]) == [2, 2, 2, 2]
    assert get_longest_same_div_count([0]) == [0]
    assert get_longest_same_div_count([1, 4, 9 ,3 ,5 ,7 ,9, 11]) == [3, 5, 7]

def prime_digit(n):
    if n==2:
        return True
    if n==3:
        return True
    if n==5:
        return True
    if n==7:
        return True
    return False

def all_digits_prime(n):
    """
    Determina data toate cifrele unui numar sunt prime
    :param n: numar intreg
    :return: True daca n este format doar din cifre prime
             False daca n nu este format doar din cifre prime
    """
    while n!=0:
        if prime_digit(n%10) != True:
            return False
        n=n//10
    return True

def test_all_digits_prime():
    assert all_digits_prime(2) == True
    assert all_digits_prime(23575) == True
    assert all_digits_prime(32) == True
    assert all_digits_prime(1) == False

def get_longest_prime_digits(lst: List[int]) -> List[int]:
    """
    Determina cea mai mare subsecventa in care toate elementele sunt formate din cifre prime
    :param lst: lista in care se cauta subsecventa
    :return: subsecventa gasita
    """
    n=len(lst)
    result=[]
    for st in range(n):
        for dr in range (st,n):
            all_prime=True
            for num in lst[st:dr+1]:
                if all_digits_prime(num) != True:
                    all_prime=False
                    break
            if all_prime == True:
                if dr-st +1 > len(result):
                    result=lst[st:dr+1]
    return result
def test_get_longest_prime_digits():
    assert get_longest_prime_digits([1,2,3,6,7,23,32,55,7252]) == [7, 23, 32, 55, 7252]
    assert get_longest_prime_digits([2,3,5,7]) == [2,3,5,7]
    assert get_longest_prime_digits([45,54]) == []
    assert get_longest_prime_digits([41,44,45,47]) == []
def main():
    lst = []
    while True:
        show_menu()
        opt = input('Optiunea: ')
        if opt == '1':
            lst = read_list()
        elif opt == '2':
            print('Cea mai lunga subsecventa cu toate numerele pare este:',get_longest_all_even(lst))
        elif opt == '3':
            print('Cea mai lunga subsecventa cu numerele ce au același număr de divizori. :',get_longest_same_div_count(lst))
        elif opt == '4':
            print('Cea mai lunga subsecventa cu numerele ce sunt formate din cifre prime. :',get_longest_prime_digits(lst))
        elif opt == 'x.':
            break
        else:
            print('Optiune invalida.')


if __name__ == '__main__':
    test_get_longest_all_even()
    test_get_longest_same_div_count()
    test_all_digits_prime()
    test_get_longest_prime_digits()
    main()