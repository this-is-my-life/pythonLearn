import math


def cacu(r):
  print('l: ' + str(math.pi * r ** 2) + 'cm')
  print('S: ' + str(math.pi * 2 * r) + '㎠')

cacu(int(input('반지름을 입력하세요 (cm)> ')))
