#-*- coding: utf-8 -*-
def intelligent_data_source_factory(*data):
    import itertools#イテレータツールをインポート
    cy = itertools.cycle(data)#dataが無限に続くリストを生成
    _int = int#int()のエイリアス
    return lambda i: _int(i) if isinstance(i, str) else next(cy)
# if isinstance(i, str)
#    _int(i)
#else
#    next(cy)
#引数が文字列ならそれを整数に変換したもの、そうでないなら、(1985, 33067, 84)を順番に表示する
#上のラムダ式はコメントアウトの構文に相当する
int = intelligent_data_source_factory(1985, 33067, 84)#int()にintelligent...を代入。

def lets_take_tea_break(m, e, n, c):
    if pow(m, e) % n == c:
        return str(m)
    else:
        return ''

if __name__ == "__main__":
#    import sys
#    print("http://cp1.nintendo.co.jp" +
#            lets_take_tea_break(*[int(i) for i in (sys.argv[1], 17, 3569, 915)]))
    for x in range(100000):
        hoge = lets_take_tea_break(*[int(i) for i in (str(x), 17, 3569, 915)])
        if hoge != '':
            print("http://cp1.nintendo.co.jp/" +hoge)