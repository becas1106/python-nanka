

def main():
    hoge_tu = ('hoge','huga')
    hoge_tu = forceAppend(hoge_tu, 'piyo')
    print(hoge_tu[::2])

    # setに順番がないのは分かるけど直後にprintするだけでも割と順番変わる
    # メモリでの位置次第？
    se = set(hoge_tu)
    se2 = {'piyo', 'hunya'}
    print('se:{}'.format(se))
    print('se2:{}'.format(se2))

    print('se and se2:{}'.format(se & se2))
    



# tupleの作りをガン無視しちゃお

# クラスに関数作っちゃうのはimmutableオブジェクトだから出来ない
# def forceAppend(self, tgt):
#     tuplist = list(self)
#     tuplist.append(tgt)
#     self = tuplist
# tuple.forceAppend = forceAppend

# 新しいtuple作って返すくらいならいけるか
def forceAppend(tup:tuple, tgt) -> tuple:
    tuplist = list(tup)
    tuplist.append(tgt)
    return tuplist


if __name__ == '__main__':
    main()
    