# def solution(price):
#     answer = price
#     if price >= 500000:
#         answer = price * 0.8  # 20% 할인
#     elif price >= 300000:
#         answer = price * 0.9  # 10% 할인
#     elif price >= 100000:
#         answer = price * 0.95  # 5% 할인
#     return int(answer) 

# def solution(price):
#     if price >= 500000:
#         return int(price * 0.8)  # 20% 할인
#     elif price >= 300000:
#         return int(price * 0.9)  # 10% 할인
#     elif price >= 100000:
#         return int(price * 0.95)  # 5% 할인
#     else:
#         return price  # 할인 없음

# def solution(price):
#     if price >= 500000:
#         return price - (price * 0.2)
#     elif price >= 300000:
#         return price - (price * 0.1)
#     elif price >= 100000:
#         return price - (price * 0.05)
#     else:
#         return price

def solution(price):
    if price>=500000:
        price = price *0.8
    elif price>=300000:
        price = price *0.9
    elif price>=100000:
        price = price * 0.95
    return int(price)

