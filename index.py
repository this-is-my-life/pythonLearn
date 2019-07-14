def cacu():
  n = int(input('숫자를 입력하세요> '))
  if n % 2 == 0:
    print(str(n) + '는 짝수입니다')
  else n % 2 == 1:
    print(str(n) + '는 홀수입니다')

while True:
  cacu()