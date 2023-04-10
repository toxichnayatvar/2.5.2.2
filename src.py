import turtle

x = int(input('Введите размер стороны:'))

turtle.shape("turtle")
turtle.fillcolor('#32CD32')

for i in range(5):
    turtle.forward(x)
    turtle.right(36)
    turtle.forward(x)
    turtle.left(108)

turtle.done()