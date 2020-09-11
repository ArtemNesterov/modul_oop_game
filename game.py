from exceptions import GameOver, EnemyDown
import model
from settings import WELCOME_STRING, START_STRING, START_EXIT_KEY_WORDS, GOODBYE_STRING, WRONG_SELECT, LIVES, V_SCORE, \
    ENEMY_DOWN_STRING, LIVES_STRING


def input_player_name(string=WELCOME_STRING):
    return input(string)


def input_start(string=START_STRING):
    i = ''
    while i.upper() not in [x.upper() for x in START_EXIT_KEY_WORDS.values()]:
        i = input(string).strip()
    if i == START_EXIT_KEY_WORDS['exit']:
        print(GOODBYE_STRING)
        exit()


def select_player_attack(string="введи 1 длявыбора волшебника, 2 для воина, 3 для разбойника"):
    while True:
        i = input(string)
        if i.isdigit():
            i = int(i)
        if i in [1, 2, 3]:
            return i
        print(WRONG_SELECT)


def play():
    """
    - Ввод имени игрока
    - Создание объекта player
    - level = 1
    - Создание объекта enemy
    - в бесконечном цикле вызывает методы attack и defense объекта player
    - при возникновении исключения EnemyDown повышает уровень игры, создает новый объект Enemy с
    новым уровнем, добавляет игроку +5 очков."""

    level = 1
    player = model.Player(input_player_name(), LIVES)
    player.input_start()
    enemy = model.Enemy(level)
    while True:
        try:
            player.attack(enemy)
            player.defence(enemy)
        except EnemyDown:
            level += 1
            enemy = model.Enemy(level)
            player.score += V_SCORE
            print(ENEMY_DOWN_STRING, player.score)
            print(LIVES_STRING, player.lives)

            continue
        except GameOver:  # запись очков игрока
            with open("scores.txt", "a") as f:
                f.writelines("{}:  {}".format(player.name, player.score))


if __name__ == '__main__':
    try:
        play()
    except GameOver:
        # выводит
        # сообщение
        # об
        # ошибке, записывает
        # результат
        # в
        # таблицу
        # рекордов.
        pass

    except KeyboardInterrupt:
        pass

    finally:
        print("Good bye!")
