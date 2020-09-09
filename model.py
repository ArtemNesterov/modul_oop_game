class Player:
    def __init__(self, name, lives, score, allowed_attacks):
        self.name = name
        self.lives = lives
        self.score = score
        self.allowed_attacks = allowed_attacks

    @staticmethod
    def fight(attack, defense):
        # статический
        # fight(attack, defense) - возвращает
        # результат
        # раунда - 0
        # если
        # ничья, -1
        # если
        # атака
        # неуспешна, 1
        # если
        # атака
        # успешна.
        pass

    def decrease_lives(self):
        # то
        # же, что
        # и
        # Enemy.decrease_lives(), вызывает
        # исключение
        # GameOver
        pass

    def attack(self, enemy_obj):
        # получает
        # ввод
        # от
        # пользователя(1, 2, 3), выбирает
        # атаку
        # противника
        # из
        # объекта
        # enemy_obj;
        # вызывает
        # метод
        # fight();
        # Если
        # результат
        # боя
        # 0 - вывести
        # "It's a draw!",
        # если
        # 1 = "You attacked successfully!"
        # и
        # уменьшает
        # количество
        # жизней
        # противника
        # на
        # 1, если - 1 = "You missed!"
        pass

    def defence(self, enemy_obj):
        # то
        # же
        # самое, что
        # и
        # метод
        # attack(), только
        # в
        # метод
        # fight
        # первым
        # передается
        # атака
        # противника, и
        # при
        # удачной
        # атаке
        # противника
        # вызывается
        # метод
        # decrease_lives
        # игрока.

        pass


class Enemy:
    def __init__(self, level, lives):
        self.level = level
        self.lives = lives

    @staticmethod
    def fight(attack, defense):
        # возвращает
        # результат
        # раунда - 0
        # если
        # ничья, -1
        # если
        # атака
        # неуспешна, 1
        # если
        # атака
        # успешна.
        pass

    def decrease_lives(self):
        # уменьшает
        # количество
        # жизней.Когда
        # жизней
        # становится
        # 0
        # вызывает
        # исключение
        # EnemyDown.

        pass
