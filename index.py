def cacu():
  n = int(input('숫자를 입력하세요> '))
  if n > 0:
    print(str(n) + '는 양수입니다')
  elif n < 0:
    print(str(n) + '는 음수입니다')
  else:
    print(str(n) + '은 0입니다')

while True:
  cacu()