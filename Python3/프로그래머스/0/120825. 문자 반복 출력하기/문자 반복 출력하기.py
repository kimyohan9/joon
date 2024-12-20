def solution(my_string,n):
    return ''.join([char * n for char in my_string])

# def solution(my_string,n):
#     result = ""
#     for char in my_string:
#         result += char * 3
#     return result