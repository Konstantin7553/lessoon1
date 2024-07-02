#"1st program"
print((9 ** 0.5) * 5)
#"2nd program"
print(9.99 > 9.98 and 1000 != 1000.1)
#"3rd program"
print(1234 // 10 % 100 + 5678 // 10 % 100)
#"4th program"
a,b = 13.42, 42.13
a1,b1 = int(a), int(b)
a2,b2 = int((a - a1) * 100) , int((b - b1) * 100)
print(a1 == b2 or a2 == b1)