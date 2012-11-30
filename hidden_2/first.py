#!python
# -*- coding:utf-8 -*-

def lets_take_tea_break(m, e, n, c):
    if pow(m, e) * n == c:
        return str(m)
    else:
        return ''

if __name__ == "__main__":
#    import sys
#    print("http://cp1.nintendo.co.jp" +
#            lets_take_tea_break(*[int(i) for i in (sys.argv[1], 17, 3569, 915)]))
    for x in range(100000):
        hoge = lets_take_tea_break(*[int(i) for i in (x, 17, 3569, 915)])
        if hoge != '':
            print("http://cp1.nintendo.co.jp/" +hoge)
            break