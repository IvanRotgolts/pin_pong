import arcade

class Game(arcade.Window):
    def __init__(self, width, height, title) : 
        #функция super вызывает конструктор класса родителя и передает ему аргументы(значения)
        super().__init__(width, height, title) 

        #Создаем объект шарик
        self.ball = Ball(300, 300, 3)

    def on_draw(self):
        #делает отрисовку
        self.background_color = (0, 128, 128)
        self.clear()

        self.ball.draw()
    
    def update(self, delta_time: float):
        #обновляет положение
        self.ball.update()

class Ball(arcade.Sprite):
    #Описываю шарик
    def __init__(self, x, y, speed):
        super().__init__(filename = "C:\\MyPrograms\\arcade\\pin_pong\\ball.png", scale = 0.2)
        #устанавливаем атрибутам положение и скорость
        self.center_x = x
        self.center_y = y
        self.change_x = speed

    def update(self):
        #обновление положения и логика
        self.center_x += self.change_x

        if self.right > 600:
            self.change_x *= -1
        
        if self.left < 0:
            self.change_x *= -1


    





















#coздаем окно
window = Game(600, 600, 'Пинг-Понг')
#запускаем игровой движок 
arcade.run()