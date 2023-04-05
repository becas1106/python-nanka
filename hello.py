# print
print('hoge')

hoge = 1 + 2

print(hoge)

print('hoge','huga','piyo', sep='\n')


# for
arr = {1, 3, 5}
j = 0

for i in arr:
    j += i

print(j)


for i in range(1, 10, 2):
    print(i)


# if
# inp = int(input())
inp = 3

if (inp % 2) == 1:
    type = ('kisu','')
elif inp > 9:
    type = ('gusu','big')
else:
    type = ('gusu','small')

print('{}は{}です。{}'.format(inp, type[0], type[1]))


# iroiro
n = 1_000_000
print(n * 3)

import collections_test
print(collections_test.__name__)






from pathlib import Path
import os
# このファイルを格納しているフォルダから引数に渡した先に移動したときの絶対パス
print(os.path.abspath("../"))

# このファイルの絶対パス
print(Path(__file__).resolve())

# パスの結合
print(os.path.join(Path(__file__).resolve().parent, 'project', 'templates'))