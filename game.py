import exceptions

if __name__ == '__main__':
    try:
        pass

    except exceptions.GameOver:
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


        # - Содержит блок на проверку имени модуля (main)
        #     - внутри if блок try/except.
        #     - try запускает функцию play()
        #     - except обрабатывает два исключения:
        #         GameOver - выводит сообщение об ошибке, записывает результат в таблицу рекордов.
        #         KeyboardInterrupt - pass
        #     - finally печатает "Good bye!"


def play():
    name = input()



        # - Ввод имени игрока
        #     - Создание объекта player
        #     - level = 1
        #     - Создание объекта enemy
        #     - в бесконечном цикле вызывает методы attack и defense объекта player
        #     - при возникновении исключения EnemyDown повышает уровень игры, создает новый объект Enemy с
        #     новым уровнем, добавляет игроку +5 очков.
    pass
