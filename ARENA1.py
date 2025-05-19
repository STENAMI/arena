import random


class Gladiator:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense


gladiator1 = Gladiator("щавэль", 100, 20, 10)
gladiator2 = Gladiator("ракушкэ", 100, 15, 15)

print(f"На арене сражаются самые КРУТЫЕ: {gladiator1.name} и {gladiator2.name}!")

while gladiator1.health > 0 and gladiator2.health > 0:
    attacker, defender = (gladiator1, gladiator2) if random.random() < 0.5 else (gladiator2, gladiator1)

    # Случайное событие: 5% шанс на поддержку толпы
    if random.random() < 0.05:
        print("ВСЕ В ШОКЕ ОТ ТАКОГО БОЯ И ПОДДЕРЖИВАЮТ ИХ!!!")
        attacker.attack += 5  # Увеличиваем атаку атакующего на 5

    damage = max(0, attacker.attack - defender.defense)
    defender.health -= damage

    print(f"{attacker.name} жестко кусает {defender.name} и наносит {damage} урона! Осталось здоровья: {defender.health}")

    if damage == 0:
        print(f"{attacker.name} жестко кусает {defender.name}, но урон оказался нулевым.")

winner = gladiator1 if gladiator1.health > 0 else gladiator2
print(f"Победитель: {winner.name}! Поздравляем! Теперь противник плакэ плакэ.")

