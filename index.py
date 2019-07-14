from turtle import *
import random

texts = ['JS', 'C', 'C#', 'C++', 'JAVA', 'HTML', 'CSS', 'py', '한스']
colors = ['yellow', 'blue', 'green', 'purple', 'red', 'orange', 'skyblue', 'gold', 'brown']
lon = 8

tracer(0)


def go(x, y):
  pu()
  goto(x, y)
  pd()

def dice():
  clear()

  lang = random.randint(0, lon)

  go(180 , 70)
  color(colors[lang])

  begin_fill()
  for i in range(6):
    circle(20, 220)
    rt(160)
  end_fill()
  go(-450, 0)
  write('세상에서 가장 완벽한 언어는', font=("D2Coding", 30))
  color('white')

  go(110, 50)
  write(texts[lang], font=("D2Coding", 30))

onkey(dice, '')
listen()

input()