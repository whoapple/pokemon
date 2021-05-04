import random
import time
import csv
import pygame


class Pokemon:
    def __init__(self, id, name, type_1, type_2, total, hp, atk, _def, sp_atk, sp_def, speed, *_):
        self.name = name
        self.atk = int(atk)
        self._def = int(_def)
        self.max_hp = int(hp)
        self.hp = int(hp)
        self.speed = int(speed)
        self.sp_atk = sp_atk
        self.id = int(id)
        self.type_1 = type_1
        self.type_2 = type_2
        self.total = int(total)
        self.sp_def = sp_def


    def __repr__(self):
        return f"Покемон: {self.name}\nАтака: {self.atk}\nЗащита: {self._def}\nЗдоровье: {self.hp}/{self.max_hp}\nСкорость: {self.speed}\nID: {self.id}\nТип 1: {self.type_1}\nТип 2: {self.type_2}\n"


    def attack(self, opponent):
        better_print(f'\n{self.name} атакует {opponent.name}')
        opponent.hp -= int((self.atk/opponent._def)*(self.total/50)*random.uniform(1.5, 3.0))
        self.show_stats(opponent)


    def show_stats(self, target):
        better_print(f"HP: {target.hp} ({int(100/target.max_hp*target.hp)}%)")


class Player:
    def __init__(self):
        self.inventory = {'малое зелье здоровья':0, "покебол":0, 'зелье здоровья':0, 'большое зелье здоровья':0, 'зелье силы':0}
        self.pokemon_list = []
        self.current_pokemon = ''
        self.money = 0


def fight():
    enemy_pok = ''
    player_pok = player.current_pokemon

    while enemy_pok == '':
        better_print("Начинай сначала")
        with open('pokemon.csv') as file:
            csv_reader = csv.reader(file)

            opponent_id = str(random.randint(1, 721))
            for line in csv_reader:
                if line[0] == opponent_id:
                    if int(line[4])/player.current_pokemon.total <= 1:
                        enemy_pok = Pokemon(*line)
                        print("Вражеский", enemy_pok)
                    break
                else:
                    print(line[0])
                    print('Не тот')
    print("Ваш", player_pok)
    better_print(f'на вас напал {enemy_pok.name}')

    while player_pok.hp > 0 and enemy_pok.hp > 0:
        try:
            better_print('что вы хотите сделать?\n1 - атаковать\n2 - бежать\n3 - поймать покемона\n4 - замена покемона')
            choice = int(input())
            if choice == 1:
                player_pok.attack(enemy_pok)
            if choice == 2:
                better_print('вы успешно убежали')
                break
            if choice == 3:
                if 100/enemy_pok.max_hp*enemy_pok.hp >= 50:
                    better_print('слишком много хп')
                if 20 < 100/enemy_pok.max_hp*enemy_pok.hp < 50:
                    chance = random.randint(1, 2)
                    better_print('1...')
                    time.sleep(1)
                    better_print('2...')
                    time.sleep(1)
                    better_print('3...')
                    time.sleep(1)
                    if chance == 1:
                        better_print('поимка не удалась')
                    if chance == 2:
                        better_print('поимка удалась')
                        time.sleep(1)
                        better_print(f'покемон {enemy_pok.name} добавлен в ваш покедекс')
                        player.pokemon_list.append(enemy_pok)
                        break
                if 100/enemy_pok.max_hp*enemy_pok.hp <= 20:
                    chance = random.randint(1, 10)
                    better_print('1...')
                    time.sleep(1)
                    better_print('2...')
                    time.sleep(1)
                    better_print('3...')
                    time.sleep(1)
                    if chance == 10:
                        better_print('поимка не удалась')
                    else:
                        better_print('поимка удалась')
                        time.sleep(1)
                        better_print(f'покемон {enemy_pok.name} добавлен в ваш покедекс')
                        player.pokemon_list.append(enemy_pok)
                        break
            if choice == 4:
                better_print('выбери замену покемону:')
                for i, pokemon in enumerate(player.pokemon_list):
                    better_print(f'{i} - {pokemon.name}')
                choice = int(input())
                player_pok = player.pokemon_list[choice]
        except ValueError:
            better_print('введено неверное значение')
            continue
        enemy_pok.attack(player_pok)


def better_print(word):
    for i in word:
        print(i, end='', flush='True')
        time.sleep(0.03)
    print()


def heal():
    for pokemon in player.pokemon_list:
        pokemon.hp = pokemon.max_hp
    pygame.mixer.Sound('heal.m4a').play()
    better_print('все ваши покемоны были вылечены')


def shop():
    while True:
        better_print('добро пожаловать в магазин')
        better_print(f'в вашем кошельке {player.money} монет')
        better_print('что вы хотите сделать?\n0 - выйти из магазина\n1 - купить покебол\n2 - купить малое зелье здоровья\n3 - купить зелье здоровья\n4 - купить большое зелье здоровья\n5 - купить зелье силы')
        choice = int(input())
        if choice == 0:
            break
        if choice == 1:
            better_print('сколько товаров вы хотите купить?')
            quantity = int(input())
            player.inventory['покебол'] += quantity
        if choice == 2:
            better_print('сколько товаров вы хотите купить?')
            quantity = int(input())
            player.inventory['малое зелье здоровья'] += quantity
        if choice == 3:
            better_print('сколько товаров вы хотите купить?')
            quantity = int(input())
            player.inventory['зелье здоровья'] += quantity
        if choice == 4:
            better_print('сколько товаров вы хотите купить?')
            quantity = int(input())
            player.inventory['большое зелье здоровья'] += quantity
        if choice == 5:
            better_print('сколько товаров вы хотите купить?')
            quantity = int(input())
            player.inventory['зелье силы'] += quantity
        better_print('хотите продолжить покупки?\n1 - да\n2 - нет')
        choice = int(input())
        if choice == 1:
            continue
        if choice == 2:
            break
    better_print('приходите ещё!')


pygame.mixer.init()
# sound = pygame.mixer.Sound('heal.mp3')
# sound.play()

player = Player()

better_print('Добро пожаловать в консольных покемонов!\nВыберите своего первого покемона:\n1 - Charmander\n2 - Bulbasaur\n3 - Squirtle')
first_pokemon = int(input())
if first_pokemon == 1:
    player.pokemon_list.append(Pokemon(4,'Charmander', 'Fire', '', 309, 39, 52, 43, 60, 50, 65, 1, False))
if first_pokemon == 2:
    player.pokemon_list.append(Pokemon(1,'Bulbasaur','Grass','Poison',318,45,49,49,65,65,45,1,False))
if first_pokemon == 3:
    player.pokemon_list.append(Pokemon(7,'Squirtle','Water','',314,44,48,65,50,64,43,1,False))

player.current_pokemon = player.pokemon_list[0]
better_print('Поздравляем, вы получили своего первого покемона!')

while True:
    better_print('что вы хотите сделать?\n1 - пойти в бой\n2 - пойти в медпункт\n3 - пойти в магазин\n4 - выйти и сохраниться')
    choice = int(input())
    if choice == 1:
        fight()
    if choice == 2:
        heal()
    if choice == 3:
        shop()
    if choice == 4:
        pass
