import arcade
from constants import *

class Game(arcade.Window):
    """главный игровой класс
    здесь мы объединяем все части нашей игры"""
    def __init__(self, width, height, title) : 
        #функция super вызывает конструктор класса родителя и передает ему аргументы(значения)
        super().__init__(width, height, title) 
        self.score = 0 
        self.game_status = True
        #Создаем объект шарик
        self.ball = Ball(300, 300, 3, 2)

        self.bar = Bar(300, 50, 3)

    def on_draw(self):
        #делает отрисовку
        self.background_color = (0, 128, 128)
        self.clear()

        #отрисовываем надпись для счета
        arcade.draw_text(
            f"счет: {self.score}",
            10,
            10,
            (139, 0, 0),
            25
            )
        self.ball.draw()
        self.bar.draw()
        if not self.game_status:
            pass
        #отрисовать сообщение о проигрыше
        #отрисовать сообщение о выигрые (100 очков)
    
    def update(self, delta_time: float):
        if self.game_status:
            #обновляет положение
            self.ball.update()

            self.bar.update()
        
            if self.ball.bottom <= 0:
                self.game_status = False
            #проверняем на столкновение ракетку и мяч
            collision = arcade.check_for_collision(self.ball, self.bar)
            if collision:
                self.ball.bottom = self.bar.top + 5
                self.ball.rise_speed(0.5)
                self.ball.change_y = -self.ball.change_y
                self.score += 1

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.bar.change_x = -BAR_SPEED_X
            
        if symbol == arcade.key.RIGHT:
            self.bar.change_x = BAR_SPEED_X

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.bar.change_x = 0

        if symbol == arcade.key.RIGHT:
            self.bar.change_x = 0


class Ball(arcade.Sprite):
    #Описываю шарик
    def __init__(self, x, y, speed_x, speed_y):
        super().__init__(filename = BASE_PATH + "\\ball.png", scale = 0.15)
        #устанавливаем атрибутам положение и скорость
        self.center_x = x
        self.center_y = y

        #задаем скорость
        self.change_x = speed_x
        self.change_y = speed_y

    def update(self):
        #обновление положения и логика
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1
        
        if self.left < 0:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1

    def rise_speed(self, offset):
        self.change_x += offset
        self.change_y += offset
            
class Bar(arcade.Sprite):
    """описывает объект ракетки"""
    def __init__(self, x, y, speed):
        super().__init__(filename = BASE_PATH + "\\bar.png", scale = 0.1)
        self.center_x = x
        self.center_y = y
        self.change_x = speed

    def update(self):
        self.center_x += self.change_x

        if self.left <= 0:
            self.change_x *= -1

        if self.right >= 600:
            self.change_x *= -1
        
    





















#coздаем окно
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
#запускаем игровой движок 
arcade.run()