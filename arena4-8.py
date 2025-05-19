#"Арена гладиаторов"

# Список гладиаторов
gladiators = []

def add_gladiator(name, strength, agility):
    """LJОБАВЛЕНИЕ нового гладиатора в арсенал"""
    gladiator = {
        'name': name,
        'strength': strength,
        'agility': agility
    }
    gladiators.append(gladiator)
    print(f"Гладиатор {name} добавлен.")

def list_gladiators():
    """вывод имеющихся гладиаторов"""
    if not gladiators:
        print("Нет ни одного гладиатора!!!.")
    else:
        for index, g in enumerate(gladiators, start=1):
            print(f"{index}. {g['name']} (Сила: {g['strength']}, Ловкость: {g['agility']})")

def fight(glad1_name, glad2_name):
    """бой между двумя гладиаторами"""
    glad1 = next((g for g in gladiators if g['name'] == glad1_name), None)
    glad2 = next((g for g in gladiators if g['name'] == glad2_name), None)

    if not glad1 or not glad2:
        print("Один или оба гладиатора не найдены.")
        return

    # Простая логика боя: сравниваем силу и ловкость
    score1 = glad1['strength'] + glad1['agility']
    score2 = glad2['strength'] + glad2['agility']

    print(f"Бой: {glad1['name']} vs {glad2['name']}")
    if score1 > score2:
        print(f"Победитель: {glad1['name']}!")
    elif score2 > score1:
        print(f"Победитель: {glad2['name']}!")
    else:
        print("Ничья!")

# Пример использования
add_gladiator("Femboy", 8, 7)
add_gladiator("Furry", 6, 9)
list_gladiators()
fight("Femboy", "Furry")