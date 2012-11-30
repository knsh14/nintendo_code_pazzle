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
#
#上のラムダ式はコメントアウトの構文に相当する
int = intelligent_data_source_factory(1985, 33067, 84)#int()にintelligent...を代入。
