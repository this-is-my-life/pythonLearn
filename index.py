import datetime

def cacu():
  return thisyear - birthyear

name = input('이름을 입력하세요> ')
thisyear = datetime.datetime.now().year
birthyear = int(input('생년을 입력하세요> '))

print(name + '님 안녕하세요!')
print('당신의 나이는 만 ' + str(cacu()) + '세입니다')
print('당신의 나이는 ' + str(cacu() + 1) + '세입니다')
