#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number >= 0:
        number = number
    elif number < 0:
        number = (-1)*number
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    List=[]
    for letter in prefixes:
        List.append(letter+suffixe)
    return List


def prime_integer_summation() -> int:
    sum = 2
    prime_numbers_used=1
    number = 2
    while prime_numbers_used < 100:
        number += 1
        for index in range(2, number):
            if number%index!=0:
                if(number==index+1):
                    sum += number
                    prime_numbers_used += 1
                continue
            else:
                break
    return sum


def factorial(number: int) -> int:
    result = 1
    for index in range(1, number+1):
        result *= index
    return result


def use_continue() -> None:
    for index in range (1,11):
        if index == 5:
            continue
        else:
            print (index)
    return index


def verify_ages(groups: List[List[int]]) -> List[bool]:
    boolean_list = []
    index_integer = 0
    for index_list in groups:
        if len(index_list) > 10 or len(index_list) <= 3:
            boolean_list.append(False)

        if len(boolean_list)==index_integer:
            for element in index_list:
                if element == 25:
                    boolean_list.append(True)
                    break

        if len(boolean_list)==index_integer:
            for element in index_list:
                if element < 18:
                    boolean_list.append(False)
                    break
        
        if len(boolean_list)==index_integer:
            exactement_50_ans = False
            plus_que_70_ans = False
            for element in index_list:
                if element > 70:
                    plus_que_70_ans = True
                if element == 50:
                    exactement_50_ans = True
            if plus_que_70_ans is True and exactement_50_ans is True:
                boolean_list.append(False)
                index_integer += 1
            else:
                boolean_list.append(True)

        index_integer += 1
        
    return boolean_list


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
