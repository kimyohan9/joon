def solution(money):
    price = 5500
    cups = money // price
    change = money % price
    return [cups,change]