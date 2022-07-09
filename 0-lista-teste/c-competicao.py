# x = (a + b + |a - b|) / 2

def highestScore(a, b):
    result = (a + b + abs(a - b)) / 2
    return result


a = int(input())
l = int(input())
p = int(input())
h = int(input())


