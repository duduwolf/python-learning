def a(a,b):
    print (int((a+b)*(b-a+1)/2))

# def b(a,b):
#     c = a
#     for looper in range(a,b+1):
#         c = c+1
#         d = a+c
#         print（str(d)）

# a(1,2)
# b(1,2)

def jisuan(min, max):
    count = 0
    for i in range(min, max+1):
        count = count + i
    return count

print(jisuan(2, 3))
print(a(2, 3))