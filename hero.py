#Створення классу Герой
class Hero:
    # Конструктор классу
    def __init__(self, name, weapon, health, power, range_attack):
        self.name = name
        self.weapon = weapon
        self.health = health
        self.power = power
        self.range_attack = range_attack
        self.money = 100

    # Метод для виводу повної інформації про героя
    def hero_info(self):
        print(f'{self.name} має зброю {self.weapon}, його рівень здоров\'я: {self.health}. Сила удару: {self.power},'
              f' максимальна дистанція удару: {self.range_attack} метр(и)!')

    # Метод для перевірки рівня здоров'я героя
    def health_info(self):
        if self.health < 0:
            self.health = 0
        print(f'У {self.name} лишилося {self.health} хп!')

    # Метод для удару по іншому герою
    def strike(self, enemy):
        chance_crit = randint(1, 5)
        if chance_crit == 3:
            enemy.health -= 5
            print(f'{self.name} наніс {5} критичного урона герою {enemy.name}!')
        attack = randint(self.power - 10, self.power + 10)
        print(f'Осліпляючий блиск меча! {self.name} наніс {attack} урона герою {enemy.name}!')
        enemy.health -= attack

    def check_money(self):
        print(f'У {self.name} лишилося {self.money} монет!')


class Barbarian(Hero):
    def __init__(self, name, weapon, health, power, range_attack):
        super().__init__(name, weapon, health, power, range_attack)
        self.rage = 0

    def strike(self, enemy):
        self.rage += 1
        chance_crit = randint(1, 5)
        if chance_crit == 3:
            enemy.health -= 5
            print(f'{self.name} наніс {5} критичного урона герою {enemy.name}!')
        attack = randint(self.power - 10, self.power + 10)
        print(f'На всю арену пролунав тріск! {self.name} наніс {attack} урона герою {enemy.name}!')
        enemy.health -= attack
        if self.rage == 3:
            self.rage = 0
            attack_rage = randint(self.power - 15, self.power)
            print(f'{self.name} розізлився і наніс {attack} додаткового урона герою {enemy.name}!')
            enemy.health -= attack_rage


class Magic(Hero):
    def __init__(self, name, weapon, health, power, range_attack):
        super().__init__(name, weapon, health, power, range_attack)
        self.level_mana = 0

    def strike(self, enemy):
        chance_crit = randint(1, 5)
        if chance_crit == 3:
            enemy.health -= 5
            print(f'{self.name} наніс {5} критичного урона герою {enemy.name}!')
        attack = randint(self.power - 10, self.power + 10)
        print(f'В повітрі пронеслась магічна струя! {self.name} наніс {attack} урона герою {enemy.name}!')
        enemy.health -= attack


# Функція для створення битви
def fight(hero1, hero2):
    choice_strike = randint(1, 2)
    while hero1.health > 0 or hero2.health > 0:
        if choice_strike == 1:
            hero1.strike(hero2)
            hero2.health_info()
            if hero2.health == 0:
                break

            hero2.strike(hero1)
            hero1.health_info()
            if hero1.health == 0:
                break

        elif choice_strike == 2:
            hero2.strike(hero1)
            hero1.health_info()
            if hero1.health == 0:
                break

            hero1.strike(hero2)
            hero2.health_info()
            if hero2.health == 0:
                break

    if hero1.health > hero2.health:
        print(f'Переміг {hero1.name}!')
    else:
        print(f'Переміг {hero2.name}!')


