import random
import requests
import discord
from discord.ext import commands

TOKEN = "OTQ3ODYwMTQ0MDQ4NDUxNTg0.YhzZjA.hrPTf2pRhPCu25Ken667_BxY7ps"
weapon1 = 0
weapon2 = 0
gold = 0
health = 0
rooms = 0
character = False
enemy_melee = 0
enemy_middle = 0
enemy_ranged = 0
enemy_melee_hp = 0
enemy_middle_hp = 0
enemy_ranged_hp = 0
player_dice1 = 0
player_dice2 = 0
player_dice3 = 0
enemy_dice1 = 0
enemy_dice2 = 0
enemy_dice3 = 0
combat_room = False
treasure_room = False
healing_room = False
shop_room = False
choosing_a_room = False
roomchoise1 = 0
roomchoise2 = 0
shopchoise1 = 0
shopchoise2 = 0
shopprise1 = 0
shopprise2 = 0
treasure_item = 0
shop_pending_item = 0
floortype = 0
status_weak = False
status_slime = False
status_block = False
item_ace = False
item_smallrock = False
item_healingplant = False
item_amulet = False
item_bluedice = False
item_goldendice = False
item_reddice = False
item_cuteblob = False
item_dicebag = False
weapon1_active = False
weapon2_active = False
dicelist = ['<:dice_1:967497465135763507>', '<:dice_2:967497505313026108>', '<:dice_3:967497533125455962>',
            '<:dice_4:967497552280821800>', '<:dice_5:967497573990551572>', '<:dice_6:967497592286089236>']
enemydicelist = ['<:enemydice_1:967499080819425350>', '<:enemydice_2:967499100213870704>',
                 '<:enemydice_3:967499125698474064>', '<:enemydice_4:967499145764044830>',
                 '<:enemydice_5:967499164948787301>', '<:enemydice_6:967499032710746183>']
itemlist = ['<:amulet:967851614075510814>', '<:blue_dice:967856678802423848>', '<:cute_blob:967861424246362213>',
            '<:dice_bag:967848354992246875>', '<:golden_dice:967860186616307853>', '<:red_dice:967860087475560508>']
floorlist = ['<:floor_plate:967527135176720464>', '<:floor_fire:967532159546060950>',
             '<:floor_curse:967529863206551583>', '<:floor_slime:967528449763868732>']
weaponlist = ['<:arbalet:967483215013105764>', '<:kinjal:967479576366305351>', '<:sword:967485121479462932>',
              '<:shid:967486984845156452>', '<:hoook:967494061860720690>', '<:staff:967490897832992798>']
cursedweaponlist = ['<:cursed_axe:967508608139002026>', '<:cursed_staff:967505361705787433>',
                    '<:cursed_eye:967511665090383903>']
dashes = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']


class MainBot(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.character = character
        self.weapon1 = weapon1
        self.weapon2 = weapon2
        self.gold = gold
        self.health = health
        self.rooms = rooms
        self.enemy_melee = enemy_melee
        self.enemy_middle = enemy_middle
        self.enemy_ranged = enemy_ranged
        self.enemy_melee_hp = enemy_melee_hp
        self.enemy_middle_hp = enemy_middle_hp
        self.enemy_ranged_hp = enemy_ranged_hp
        self.player_dice1 = player_dice1
        self.player_dice2 = player_dice2
        self.player_dice3 = player_dice3
        self.enemy_dice1 = enemy_dice1
        self.enemy_dice2 = enemy_dice2
        self.enemy_dice3 = enemy_dice3
        self.combat_room = combat_room
        self.treasure_room = treasure_room
        self.healing_room = healing_room
        self.shop_room = shop_room
        self.choosing_a_room = choosing_a_room
        self.roomchoise1 = roomchoise1
        self.roomchoise2 = roomchoise2
        self.shopchoise1 = shopchoise1
        self.shopchoise2 = shopchoise2
        self.shopprise1 = shopprise1
        self.shopprise2 = shopprise2
        self.treasure_item = treasure_item
        self.shop_pending_item = shop_pending_item
        self.floortype = floortype
        self.item_ace = item_ace
        self.item_smallrock = item_smallrock
        self.item_healingplant = item_healingplant
        self.item_amulet = item_amulet
        self.item_bluedice = item_bluedice
        self.item_goldendice = item_goldendice
        self.item_reddice = item_reddice
        self.item_cuteblob = item_cuteblob
        self.item_dicebag = item_dicebag
        self.dicelist = dicelist
        self.enemydicelist = enemydicelist
        self.itemlist = itemlist
        self.floorlist = floorlist
        self.weaponlist = weaponlist
        self.cursedweaponlist = cursedweaponlist
        self.status_weak = status_weak
        self.status_slime = status_slime
        self.status_block = status_block
        self.weapon1_active = weapon1_active
        self.weapon2_active = weapon2_active

    @commands.command(name='info')
    async def info(self, ctx):
        await ctx.send("Добро пожаловать в **Dicemoji!** Здесь вы и ваши враги будут бросать **кубы**, чтобы совершать "
                       "различные действия. Вам потребуется пройти 15 случайных **комнат** и после сразиться с "
                       "**боссом**. Находите могущественные **артефакты**, надёжное ||(или не очень)|| **оружие** и "
                       "то, без чего ни один искатель приключений не обойдётся - **золото**! Список команд:\n\n"
                       "`*startgame` - начать новую игру\n\n`*savegame` - сохранить игру\n\n`*loadgame` - "
                       "загрузить сохранённую игру\n\n`*char [1 или 2]` - выбор персонажа в начале игры\n\n"
                       "`*room [1 или 2]` - выбор следующей комнаты\n\n`*buy [1, 2 или nothing]` - купить в "
                       "магазине первое или второе оружие соответственно, или ничего не покупать\n\n`*pick [1 или 2]` "
                       "- выбрать, вместо какого оружия взять купленное вами в магазине\n\n`*sacrifice [10,"
                       " 20, 30 или nothing]` - пожертвовать соответствующее количество золота в комнате исцеления\n\n"
                       "\n\n`*attack [1 или 2] [melee, middle, ranged]` - атаковать оружием врага в указанной "
                       "вами позиции\n\n`*rollroom` - перейти к следующей комнате\n\n`*rollfight` - бросить куб в бою"
                       "\n\n`*info_loot` - узнать информацию о всём оружии и предметах в игре\n\n`*info_floor` - узнать"
                       " информацию о всех типах пола в игре")

    @commands.command(name='info_loot')
    async def info_loot(self, ctx):
        await ctx.send(f'Архив лута в **Dicemoji:**\n\n**Обычное оружие:**\n\n{self.weaponlist[0]} - активируется на '
                       f'{self.dicelist[3]}{self.dicelist[4]}{self.dicelist[5]}, среднее и дальнее, наносит 3 урона\n'
                       f'\n{self.weaponlist[1]} - активируется на {self.dicelist[1]}{self.dicelist[2]}, ближнее и '
                       f'среднее, наносит 2 урона\n\n{self.weaponlist[2]} - активируется на {self.dicelist[3]}'
                       f'{self.dicelist[4]}{self.dicelist[5]}, ближнее, наносит 5 урона\n\n{self.weaponlist[3]} - '
                       f'активируется на {self.dicelist[0]}{self.dicelist[1]}, накладывает на персонажа '
                       f'<:token_block:967533280457015345>, который предотвращает следующий полученный урон\n\n'
                       f'{self.weaponlist[4]} - активируется на {self.dicelist[0]}{self.dicelist[1]}{self.dicelist[2]},'
                       f'среднее и дальнее, наносит 1 урон и притягивает врага на одну позицию вперёд\n\n'
                       f'{self.weaponlist[5]} - активируется на {self.dicelist[4]}{self.dicelist[5]}, лечит персонажа '
                       f'на 3 здоровья\n\n**Проклятое оружие:**\n\n{self.cursedweaponlist[0]} - активируется на '
                       f'{self.dicelist[2]}{self.dicelist[3]}, ближнее, наносит 6 урона и отбрасывает врага на одну '
                       f'позицию назад\n\n{self.cursedweaponlist[1]} - активируется на {self.dicelist[0]}'
                       f'{self.dicelist[2]}{self.dicelist[5]}, наносит всем врагам 1 урон, лечит персонажа на 2\n\n'
                       f'{self.cursedweaponlist[2]} - активируется на {self.dicelist[0]}{self.dicelist[1]}'
                       f'{self.dicelist[2]}{self.dicelist[3]}{self.dicelist[4]}{self.dicelist[5]}, ближнее и среднее, '
                       f'наносит 1 урон, если два ваших куба, брошенных при атаке, совпали, то мгновенно убивает врага,'
                       f' которого атакует')
        await ctx.send(f'**Предметы:**\n\n<:ace:967842334333100092> - когда вы выбрасываете '
                       f'{self.dicelist[0]} в бою, все враги получают 1 урон\n\n<:small_rock:967843198716244100> - '
                       f'когда вы выбрасываете {self.dicelist[0]} в бою, вы бросаете ещё один, третий куб\n\n'
                       f'<:healing_plant:967846012590903327> - восстановите 2 здоровья в конце каждого боя\n\n'
                       f'<:blue_dice:967856678802423848> - если при выборе комнаты вам не выпало {self.dicelist[4]} или'
                       f' {self.dicelist[5]}, то бросок будет сделан ещё один раз\n\n<:red_dice:967860087475560508> - '
                       f'когда враг выбрасывает {self.enemydicelist[0]}, он получает 1 урон\n\n<:golden_dice:9678601866'
                       f'16307853> - при входе в магазин бросается куб. Если выпадает {self.dicelist[4]} или '
                       f'{self.dicelist[5]}, вы получаете 30 золота\n\n<:amulet:967851614075510814> - на вас не '
                       f'действуют эффекты пола (на врагов они продолжают действовать)\n\n<:cute_blob:96786142424636221'
                       f'3> - перед боем с финальным боссом полностью восстановите здоровье и повысьте его до 30\n\n'
                       f'<:dice_bag:967848354992246875> - на вас не действуют эффекты <:token_slime:967539012514512927>'
                       f' и <:token_weak:967537998839291964>')

    @commands.command(name='info_floor')
    async def info_floor(self, ctx):
        await ctx.send(f'Пол подземелий с врагами в **Dicemoji** бывает разным. Всего если четыре типа:\n\n'
                       f'{self.floorlist[0]} - нет эффекта, встречается чаще всего\n\n{self.floorlist[1]} - в конце '
                       f'каждого хода враги и персонаж бросают куб и на {self.dicelist[0]}{self.dicelist[1]}'
                       f'{self.dicelist[2]} получают 1 урон\n\n{self.floorlist[2]} - когда враг или персонаж '
                       f'выбрасывает {self.dicelist[0]}, он получает 1 урон\n\n{self.floorlist[3]} - в конце каждого '
                       f'хода игрок получает эффект <:token_slime:967539012514512927>')

    @commands.command(name='startgame')
    async def startgame(self, ctx):
        self.weapon1 = 0
        self.weapon2 = 0
        self.gold = 0
        self.health = 0
        self.rooms = 0
        self.character = False
        self.enemy_melee = 0
        self.enemy_middle = 0
        self.enemy_ranged = 0
        self.player_dice1 = 0
        self.player_dice2 = 0
        self.player_dice3 = 0
        self.enemy_dice1 = 0
        self.enemy_dice2 = 0
        self.enemy_dice3 = 0
        self.combat_room = False
        self.treasure_room = False
        self.healing_room = False
        self.shop_room = False
        self.choosing_a_room = False
        self.roomchoise1 = 0
        self.roomchoise2 = 0
        self.shopchoise1 = 0
        self.shopchoise2 = 0
        self.shop_pending_item = 0
        self.floortype = 0
        self.item_ace = False
        self.item_smallrock = False
        self.item_healingplant = False
        self.item_amulet = False
        self.item_bluedice = False
        self.item_goldendice = False
        self.item_reddice = False
        self.item_cuteblob = False
        self.status_weak = False
        self.status_slime = False
        self.status_block = False
        self.weapon1_active = False
        self.weapon2_active = False
        self.itemlist = ['<:amulet:967851614075510814>', '<:blue_dice:967856678802423848>',
                         '<:cute_blob:967861424246362213>', '<:dice_bag:967848354992246875>',
                         '<:golden_dice:967860186616307853>', '<:red_dice:967860087475560508>']
        await ctx.send("Мы начинаем новое приключение!")
        await ctx.send("Выберите персонажа с помощью команды `*char 1` или `*char 2`\n\n<:plant_knight:9675172509847511"
                       "14> **Растительный рыцарь:**\n\n27 здоровья\n\nСтартовое оружие:\n<:sword:967485121479462932> -"
                       " активируется на <:dice_4:967497552280821800><:dice_5:967497573990551572><:dice_6:9674975922860"
                       "89236>, ближнее, наносит 5 урона\n<:shid"
                       ":967486984845156452> - активируется на <:dice_1:967497465135763507><:dice_2:967497505313026108>"
                       ", накладывает на персонажа <:token_block:967533280457015345>, который предотвращает следующий "
                       "полученный урон\n\n"
                       "Стартовый предмет:\n<:healing_plant:967846012590903327> - восстановите 2 здоровья в конце каждо"
                       "го боя\n\n***ИЛИ***\n\n<:desert_wanderer:967522631190462474> **Покоритель пустынь:**\n\n22 здор"
                       "овья\n\nСтартовое оружие:\n<:arbalet:967483215013105764> - активируется на <:dice_4:96749755228"
                       "0821800><:dice_5:967497573990551572><:dice_6:967497592286089236>, среднее и дальнее, наносит 3"
                       " урона\n<:kinjal:967479576366305351> - активируется на <:dice_2:967497505313026108><:dice_3:967"
                       "497533125455962>, ближнее и среднее, наносит 2 урона\n\nСтартовые предметы:\n<:ace:96784233433"
                       "3100092> - когда вы выбрасываете <:dice_1:967497465135763507> в бою, все враги получают 1 "
                       "урон\n<:small_rock:967843198716244100> - когда вы выбрасываете <:dice_1:967497465135763507> в "
                       "бою, вы бросаете ещё один, третий куб")

    @commands.command(name='char')
    async def char(self, ctx, character_number):
        if self.character is False:
            if character_number == '1':
                self.character = '<:plant_knight:967517250984751114>'
                self.item_healingplant = True
                self.weapon1 = self.weaponlist[2]
                self.weapon2 = self.weaponlist[3]
                self.health = 27
            if character_number == '2':
                self.character = '<:desert_wanderer:967522631190462474>'
                self.item_ace = True
                self.item_smallrock = True
                self.weapon1 = self.weaponlist[0]
                self.weapon2 = self.weaponlist[1]
                self.health = 22
            self.gold = 20
            await ctx.send(f'Вы выбрали {self.character}! Используйте `*rollroom`, чтобы перейти в первую комнату')
            self.choosing_a_room = True
        else:
            await ctx.send("Вы уже выбрали персонажа! Чтобы выбрать его заново, вам нужно начать новую игру с помощью "
                           "команды `*startgame`")

    @commands.command(name='rollroom')
    async def rollroom(self, ctx):
        self.rooms += 1
        enemymeleelist = ['<:skeleton_fractured:967468877669867520>',
                          '<:skeleton_fighter:967462011011231824>', '<:slime_green:967544763135975585>',
                          '<:slime_red:967544830995603467>', '<:slime_skeleton:967542688469614703>']
        enemymidllelist = ['<:skeleton_fighter:967462011011231824>', '<:slime_red:967544830995603467>',
                           '<:slime_purple:967544881222402048>', '<:skeleton_warrior:967467049775403028>',
                           '<:slime_skeleton:967542688469614703>']
        enemyrangedlist = ['<:skeleton_warrior:967467049775403028>', '<:skeleton_caster:967463541101695086>',
                           '<:slime_queen:967547687614423103>', '<:slime_skeleton:967542688469614703>']
        if self.choosing_a_room is True:
            if self.rooms < 16:
                roll = random.randint(1, 6)
                await ctx.send(f'Подземелье выбросило {self.dicelist[roll-1]} При выпадении {self.dicelist[4]} или '
                               f'{self.dicelist[5]} вы получаете выбор из комнаты с врагами и случайной другой комнаты.'
                               f' Иначе на вас просто нападают.')
                if self.item_bluedice is True and roll < 5:
                    roll = random.randint(1, 6)
                    await ctx.send(f'<:blue_dice:967856678802423848> перебрасывает значение... Выпадает '
                                   f'{self.dicelist[roll-1]}')
                if roll > 4:
                    roll2 = random.randint(1, 3)
                    if roll2 == 1:
                        self.roomchoise2 = 'магазин'
                    if roll2 == 2:
                        self.roomchoise2 = 'сокровищницу'
                    if roll2 == 3:
                        self.roomchoise2 = 'комнату исцеления'
                    await ctx.send(f'Хаос на мгновение прекращается. Вы можете окунуться в него опять, попытаясь '
                                   f'заработать **золото** в бою. Или лучше выбрать кое-что более необычное -'
                                   f' {self.roomchoise2}! Используйте команду `*room [1 или 2]`')
                if roll < 5:
                    await ctx.send("Это опасно... С другой стороны, такие комнаты - хороший способ заработать, ведь "
                                   "местные монстры зачастую охраняют **золото**. Приготовьтесь к бою!")
                    self.choosing_a_room = False
                    self.combat_room = True
                    roll = random.randint(1, 20)
                    if roll == 1 or roll == 2 or roll == 3 or roll == 4 or roll == 5 or roll == 6:
                        self.enemy_melee = enemymeleelist[0]
                        self.enemy_melee_hp = 2
                    if roll == 7 or roll == 8 or roll == 9 or roll == 10 or roll == 11 or roll == 12:
                        self.enemy_melee = enemymeleelist[2]
                        self.enemy_melee_hp = 4
                    if roll == 13 or roll == 14 or roll == 15:
                        self.enemy_melee = enemymeleelist[1]
                        self.enemy_melee_hp = 2
                    if roll == 16 or roll == 17 or roll == 18:
                        self.enemy_melee = enemymeleelist[3]
                        self.enemy_melee_hp = 2
                    if roll == 19 or roll == 20:
                        self.enemy_melee = enemymeleelist[4]
                        self.enemy_melee_hp = 4
                    roll = random.randint(1, 20)
                    if roll == 1 or roll == 2 or roll == 3 or roll == 4 or roll == 5 or roll == 6 or roll == 7:
                        self.enemy_middle = 0
                        self.enemy_ranged = 0
                        self.enemy_middle_hp = 0
                        self.enemy_ranged_hp = 0
                    else:
                        if roll == 8 or roll == 9 or roll == 10:
                            self.enemy_middle = enemymidllelist[0]
                            self.enemy_middle_hp = 4
                        if roll == 11 or roll == 12 or roll == 13:
                            self.enemy_middle = enemymidllelist[1]
                            self.enemy_middle_hp = 2
                        if roll == 14 or roll == 15 or roll == 16:
                            self.enemy_middle = enemymidllelist[2]
                            self.enemy_middle_hp = 3
                        if roll == 17 or roll == 18 or roll == 19:
                            self.enemy_middle = enemymidllelist[3]
                            self.enemy_middle_hp = 6
                        if roll == 20:
                            self.enemy_middle = enemymidllelist[4]
                            self.enemy_middle_hp = 4
                        roll = random.randint(1, 20)
                        if roll == 1 or roll == 2 or roll == 3 or roll == 4 or roll == 5 or roll == 6 or roll == 7:
                            self.enemy_ranged = 0
                            self.enemy_ranged_hp = 0
                        else:
                            if roll == 8 or roll == 9 or roll == 10 or roll == 11:
                                self.enemy_ranged = enemyrangedlist[0]
                                self.enemy_ranged_hp = 6
                            if roll == 12 or roll == 13 or roll == 14 or roll == 15:
                                self.enemy_ranged = enemyrangedlist[1]
                                self.enemy_ranged_hp = 4
                            if roll == 16 or roll == 17 or roll == 18:
                                self.enemy_ranged = enemyrangedlist[2]
                                self.enemy_ranged_hp = 4
                            if roll == 19 or roll == 20:
                                self.enemy_ranged = enemyrangedlist[3]
                                self.enemy_ranged_hp = 4
                    if self.enemy_middle == 0:
                        await ctx.send(f'{self.character}        {self.enemy_melee}')
                    elif self.enemy_ranged == 0:
                        await ctx.send(f'{self.character}        {self.enemy_melee}  {self.enemy_middle}')
                    else:
                        await ctx.send(f'{self.character}        {self.enemy_melee}  {self.enemy_middle}  '
                                       f'{self.enemy_ranged}')
                    roll2 = random.randint(1, 10)
                    if roll2 == 8:
                        self.floortype = self.floorlist[1]
                    elif roll2 == 9:
                        self.floortype = self.floorlist[2]
                    elif roll2 == 10:
                        self.floortype = self.floorlist[3]
                    else:
                        self.floortype = self.floorlist[0]
                    await ctx.send(5 * self.floortype)
                    await ctx.send('Бросайте кубы с помощью `*rollfight`, атакуйте с помощью `*attack [название оружия]'
                                   ' [melee, middle или ranged]`. Удачи (здесь она пригодится)!')
            if self.rooms == 16:
                ctx.send("Дальше уже не выйдет выбрать свой путь. Все они вели сюда. Пришло время узнать, победите ли "
                         "вы или нет!")
                self.choosing_a_room = False
                self.combat_room = True
                self.rooms += 1
                self.enemy_melee = self.enemy_middle = self.enemy_ranged = '<:deadeye:967549879503188008>'
                self.enemy_melee_hp = self.enemy_middle_hp = self.enemy_ranged_hp = 7
                await ctx.send(f'{self.character}        {self.enemy_melee}  {self.enemy_middle}  '
                               f'{self.enemy_ranged}')
                roll2 = random.randint(1, 10)
                if roll2 == 8:
                    self.floortype = self.floorlist[1]
                elif roll2 == 9:
                    self.floortype = self.floorlist[2]
                elif roll2 == 10:
                    self.floortype = self.floorlist[3]
                else:
                    self.floortype = self.floorlist[0]
                await ctx.send(5 * self.floortype)
                await ctx.send('Это финальный бой! Как и всегда, бросайте кубы с помощью `*rollfight`, атакуйте с '
                               'помощью `*attack [название оружия] [melee, middle или ranged]`. Удачи (сейчас она '
                               'нужна, как никогда)!')
                if self.item_cuteblob is True:
                    self.health = 30
                    await ctx.send('<:cute_blob:967861424246362213> повышает ваше здоровье до 30 перед финальным боем!')
        else:
            await ctx.send("Сейчас вы не можете выбрать комнату! Скорее всего, вы не закончили бой или взаимодействие "
                           "в текущей комнате.")

    @commands.command(name='room')
    async def room(self, ctx, room_number):
        if self.choosing_a_room is True:
            if room_number == '1':
                enemymeleelist = ['<:skeleton_fractured:967468877669867520>',
                                  '<:skeleton_fighter:967462011011231824>', '<:slime_green:967544763135975585>',
                                  '<:slime_red:967544830995603467>', '<:slime_skeleton:967542688469614703>']
                enemymidllelist = ['<:skeleton_fighter:967462011011231824>', '<:slime_red:967544830995603467>',
                                   '<:slime_purple:967544881222402048>', '<:skeleton_warrior:967467049775403028>',
                                   '<:slime_skeleton:967542688469614703>']
                enemyrangedlist = ['<:skeleton_warrior:967467049775403028>', '<:skeleton_caster:967463541101695086>',
                                   '<:slime_queen:967547687614423103>', '<:slime_skeleton:967542688469614703>']
                await ctx.send("Это опасно... С другой стороны, такие комнаты - хороший способ заработать, ведь "
                               "местные монстры зачастую охраняют **золото**. Приготовьтесь к бою!")
                self.choosing_a_room = False
                self.combat_room = True
                roll = random.randint(1, 20)
                if roll == 1 or roll == 2 or roll == 3 or roll == 4 or roll == 5 or roll == 6:
                    self.enemy_melee = enemymeleelist[0]
                    self.enemy_melee_hp = 2
                if roll == 7 or roll == 8 or roll == 9 or roll == 10 or roll == 11 or roll == 12:
                    self.enemy_melee = enemymeleelist[2]
                    self.enemy_melee_hp = 4
                if roll == 13 or roll == 14 or roll == 15:
                    self.enemy_melee = enemymeleelist[1]
                    self.enemy_melee_hp = 2
                if roll == 16 or roll == 17 or roll == 18:
                    self.enemy_melee = enemymeleelist[3]
                    self.enemy_melee_hp = 2
                if roll == 19 or roll == 20:
                    self.enemy_melee = enemymeleelist[4]
                    self.enemy_melee_hp = 4
                roll = random.randint(1, 20)
                if roll == 1 or roll == 2 or roll == 3 or roll == 4 or roll == 5 or roll == 6 or roll == 7:
                    self.enemy_middle = 0
                    self.enemy_ranged = 0
                    self.enemy_middle_hp = 0
                    self.enemy_ranged_hp = 0
                else:
                    if roll == 8 or roll == 9 or roll == 10:
                        self.enemy_middle = enemymidllelist[0]
                        self.enemy_middle_hp = 4
                    if roll == 11 or roll == 12 or roll == 13:
                        self.enemy_middle = enemymidllelist[1]
                        self.enemy_middle_hp = 2
                    if roll == 14 or roll == 15 or roll == 16:
                        self.enemy_middle = enemymidllelist[2]
                        self.enemy_middle_hp = 3
                    if roll == 17 or roll == 18 or roll == 19:
                        self.enemy_middle = enemymidllelist[3]
                        self.enemy_middle_hp = 6
                    if roll == 20:
                        self.enemy_middle = enemymidllelist[4]
                        self.enemy_middle_hp = 4
                    roll = random.randint(1, 20)
                    if roll == 1 or roll == 2 or roll == 3 or roll == 4 or roll == 5 or roll == 6 or roll == 7:
                        self.enemy_ranged = 0
                        self.enemy_ranged_hp = 0
                    else:
                        if roll == 8 or roll == 9 or roll == 10 or roll == 11:
                            self.enemy_ranged = enemyrangedlist[0]
                            self.enemy_ranged_hp = 6
                        if roll == 12 or roll == 13 or roll == 14 or roll == 15:
                            self.enemy_ranged = enemyrangedlist[1]
                            self.enemy_ranged_hp = 4
                        if roll == 16 or roll == 17 or roll == 18:
                            self.enemy_ranged = enemyrangedlist[2]
                            self.enemy_ranged_hp = 4
                        if roll == 19 or roll == 20:
                            self.enemy_ranged = enemyrangedlist[3]
                            self.enemy_ranged_hp = 4
                if self.enemy_middle == 0:
                    await ctx.send(f'{self.character}        {self.enemy_melee}')
                elif self.enemy_ranged == 0:
                    await ctx.send(f'{self.character}        {self.enemy_melee}  {self.enemy_middle}')
                else:
                    await ctx.send(f'{self.character}        {self.enemy_melee}  {self.enemy_middle}  '
                                   f'{self.enemy_ranged}')
                roll2 = random.randint(1, 10)
                if roll2 == 8:
                    self.floortype = self.floorlist[1]
                elif roll2 == 9:
                    self.floortype = self.floorlist[2]
                elif roll2 == 10:
                    self.floortype = self.floorlist[3]
                else:
                    self.floortype = self.floorlist[0]
                await ctx.send(5 * self.floortype)
                await ctx.send('Бросайте кубы с помощью `*rollfight`, атакуйте с помощью `*attack [название оружия]'
                               ' [melee, middle или ranged]`. Удачи (здесь она пригодится)!')
            if room_number == '2':
                if self.roomchoise2 == 'магазин':
                    self.choosing_a_room = False
                    self.shop_room = True
                    roll = random.randint(1, 6)
                    if roll == 6:
                        self.shopchoise2 = random.choice(self.cursedweaponlist)
                        self.shopprise2 = random.randint(90, 120)
                    else:
                        self.shopchoise2 = random.choice(self.weaponlist)
                        self.shopprise2 = random.randint(50, 80)
                    roll = random.randint(1, 6)
                    if roll == 6:
                        self.shopchoise1 = random.choice(self.cursedweaponlist)
                        self.shopprise1 = random.randint(90, 120)
                    else:
                        self.shopchoise1 = random.choice(self.weaponlist)
                        self.shopprise1 = random.randint(50, 80)
                    if self.item_goldendice is True:
                        roll = random.randint(1, 6)
                        await ctx.send('Пришло время бросить <:golden_dice:967860186616307853>...')
                        if roll == 5 or roll == 6:
                            await ctx.send(f'Выпадает {self.dicelist[roll-1]} Повезло! Вы получаете 30 '
                                           f'<:gold:967840035653189733>')
                            self.gold += 30
                        else:
                            await ctx.send(f'Выпадает {self.dicelist[roll - 1]} Повезёт в следующий раз...')
                    await ctx.send(f'Добро пожаловать! В магазине продаётся:\n\n{self.shopchoise1} за '
                                   f'{self.shopprise1} <:gold:967840035653189733> ***ИЛИ*** {self.shopchoise2} за '
                                   f'{self.shopprise2} <:gold:967840035653189733>\n\nУ вас {self.gold} <:gold:967840035'
                                   f'653189733>')
                    await ctx.send('С помощью команды `*buy [1, 2 или nothing]` вы можете купить оружие '
                                   'на выбор, или пропустить магазин. Кто знает, когда ещё вам могут понадобиться'
                                   ' деньги?')
                if self.roomchoise2 == 'сокровищницу':
                    if not self.itemlist == []:
                        self.treasure_item = random.choice(self.itemlist)
                        if self.treasure_item == '<:amulet:967851614075510814>':
                            self.item_amulet = True
                        if self.treasure_item == '<:blue_dice:967856678802423848>':
                            self.item_bluedice = True
                        if self.treasure_item == '<:cute_blob:967861424246362213>':
                            self.item_cuteblob = True
                        if self.treasure_item == '<:dice_bag:967848354992246875>':
                            self.item_dicebag = True
                        if self.treasure_item == '<:golden_dice:967860186616307853>':
                            self.item_goldendice = True
                        if self.treasure_item == '<:red_dice:967860087475560508>':
                            self.item_reddice = True
                        await ctx.send(f'В сокровищнице вы находите мощный предмет: {self.treasure_item} Используйте'
                                       f'`*rollroom`, чтобы продвинуться дальше.')
                        self.itemlist.remove(self.treasure_item)
                    else:
                        self.gold += 20
                        await ctx.send(f'В сокровищнице вы находите 20 <:gold:967840035653189733> Используйте'
                                       f'`*rollroom`, чтобы продвинуться дальше.')
                if self.roomchoise2 == 'комнату исцеления':
                    self.choosing_a_room = False
                    self.healing_room = True
                    await ctx.send('В комнате исцеления вы можете использовать команду `*sacrifice [10, 20, 30 '
                                   'или nothing]`, чтобы пожертвовать определённое число золота и полечиться или '
                                   'пропустить комнату соответственно:\n\n10 <:gold:967840035653189733> - 5 здоровья\n'
                                   '\n20 <:gold:967840035653189733> - 15 здоровья\n\n30 <:gold:967840035653189733> - '
                                   'полное лечение')
        else:
            await ctx.send("Сейчас вы не можете выбрать комнату! Скорее всего, вы не закончили бой или взаимодействие "
                           "в текущей комнате.")

    @commands.command(name='buy')
    async def buy(self, ctx, tovar_choise):
        if self.shop_room is True:
            if tovar_choise == '1':
                if self.shopprise1 <= self.gold:
                    self.gold = self.gold - self.shopprise1
                    self.shop_pending_item = self.shopchoise1
                    await ctx.send(f'Вы купили {self.shop_pending_item} за {self.shopprise1} <:gold:967840035653189733>'
                                   f'У вас осталось {self.gold} <:gold:967840035653189733> Используйте команду '
                                   f'`*pick [1, 2]`, чтобы выбрать, вместо какого оружия вы хотите взять это.')
                else:
                    await ctx.send('У вас не хватает золота!')
            if tovar_choise == '2':
                if self.shopprise2 <= self.gold:
                    self.gold = self.gold - self.shopprise2
                    self.shop_pending_item = self.shopchoise2
                    await ctx.send(f'Вы купили {self.shop_pending_item} за {self.shopprise2} <:gold:967840035653189733>'
                                   f'У вас осталось {self.gold} <:gold:967840035653189733> Используйте команду '
                                   f'`*pick [1, 2]`, чтобы выбрать, вместо какого оружия вы хотите взять это.')
                else:
                    await ctx.send('У вас не хватает золота!')
            if tovar_choise == 'nothing':
                await ctx.send('Вы решили ничего не покупать. Используйте команду `*rollroom`, чтобы перейти в '
                               'следующую комнату')
                self.shop_room = False
                self.choosing_a_room = True
        else:
            await ctx.send('Сейчас вы находитесь не в магазине.')

    @commands.command(name='pick')
    async def pick(self, ctx, picked):
        if self.shop_room is True:
            if not self.shop_pending_item == 0:
                if picked == 1:
                    await ctx.send(f'Вы меняете своё первое оружие {self.weapon1} на {self.shop_pending_item} '
                                   f'Используйте команду `*rollroom`, чтобы перейти в следующую комнату')
                    self.weapon1 = self.shop_pending_item
                    self.shop_pending_item = 0
                    self.shop_room = False
                    self.choosing_a_room = True
                if picked == 2:
                    await ctx.send(f'Вы меняете своё второе оружие {self.weapon2} на {self.shop_pending_item} '
                                   f'Используйте команду `*rollroom`, чтобы перейти в следующую комнату')
                    self.weapon2 = self.shop_pending_item
                    self.shop_pending_item = 0
                    self.shop_room = False
                    self.choosing_a_room = True
            else:
                await ctx.send('Пока вы ничего нового не покупали.')
        else:
            await ctx.send('Сейчас вы находитесь не в магазине.')

    @commands.command(name='sacrifice')
    async def sacrifice(self, ctx, sacred_gold):
        if self.healing_room is True:
            if sacred_gold == '10':
                if self.gold >= 10:
                    self.gold -= 10
                    self.health += 5
                    if self.character == '<:plant_knight:967517250984751114>' and self.health > 27:
                        self.health = 27
                    if self.character == '<:desert_wanderer:967522631190462474>' and self.health > 22:
                        self.health = 22
                    await ctx.send(f"Вы потратили 10 <:gold:967840035653189733> и восстановили 5 здоровья. Теперь у вас"
                                   f" {self.gold} золота и {self.health} здоровья. Используйте `*rollroom`, чтобы "
                                   f"перейти в следующую комнату")
                    self.healing_room = False
                    self.choosing_a_room = True
                else:
                    await ctx.send('У вас не хватает золота!')
            if sacred_gold == '20':
                if self.gold >= 20:
                    self.gold -= 20
                    self.health += 15
                    if self.character == '<:plant_knight:967517250984751114>' and self.health > 27:
                        self.health = 27
                    if self.character == '<:desert_wanderer:967522631190462474>' and self.health > 22:
                        self.health = 22
                    await ctx.send(f"Вы потратили 20 <:gold:967840035653189733> и восстановили 15 здоровья. Теперь у "
                                   f"вас {self.gold} золота и {self.health} здоровья. Используйте `*rollroom`, чтобы "
                                   f"перейти в следующую комнату")
                    self.healing_room = False
                    self.choosing_a_room = True
                else:
                    await ctx.send('У вас не хватает золота!')
            if sacred_gold == '30':
                if self.gold >= 30:
                    self.gold -= 30
                    if self.character == '<:plant_knight:967517250984751114>' and self.health < 27:
                        self.health = 27
                    if self.character == '<:desert_wanderer:967522631190462474>' and self.health < 22:
                        self.health = 22
                    await ctx.send(f"Вы потратили 30 <:gold:967840035653189733> и полностью восстановили здоровье. "
                                   f"Теперь у вас {self.gold} золота и {self.health} здоровья. Используйте `*rollroom`,"
                                   f" чтобы перейти в следующую комнату")
                    self.healing_room = False
                    self.choosing_a_room = True
                else:
                    await ctx.send('У вас не хватает золота!')
            if sacred_gold == 'nothing':
                await ctx.send('Вы решили ничего не покупать. Используйте команду `*rollroom`, чтобы перейти в '
                               'следующую комнату')
                self.healing_room = False
                self.choosing_a_room = True
        else:
            await ctx.send('Сейчас вы не в комнате исцеления.')

    @commands.command(name='rollfight')
    async def rollfight(self, ctx):
        if self.combat_room is True:
            self.player_dice1 = random.randint(1, 6)
            self.player_dice2 = random.randint(1, 6)
            await ctx.send(f'Вам выпадает {self.dicelist[self.player_dice1-1]}{self.dicelist[self.player_dice2-1]}')
            if self.status_slime is True and (self.player_dice1 == 6 or self.player_dice2 == 6):
                await ctx.send(f'На вас наложен эффект <:token_slime:967539012514512927>! Если выпадает хотя бы один '
                               f'{dicelist[5]}, то кубы перебрасываются один раз, а <:token_slime:967539012514512927>'
                               f'пропадает.')
                self.status_slime = False
                self.player_dice1 = random.randint(1, 6)
                self.player_dice2 = random.randint(1, 6)
                await ctx.send(f'Вам выпадает {self.dicelist[self.player_dice1 - 1]}'
                               f'{self.dicelist[self.player_dice2 - 1]}')
            if self.item_ace is True and (self.player_dice1 == 1 or self.player_dice2 == 1):
                self.player_dice3 = random.randint(1, 6)
                await ctx.send(f'Вам выпала единица, а значит <:ace:967842334333100092> добавляет вам третий '
                               f'куб! Выпадает {self.dicelist[self.player_dice3 - 1]}')
            if self.floortype == '<:floor_curse:967529863206551583>' and (self.player_dice3 == 1 or
                                                                          self.player_dice2 == 1 or
                                                                          self.player_dice3 == 1):
                await ctx.send(f'Вам выпала единица, {self.floorlist[2]} наносит вам 1 урон. У вас остаётся '
                               f'{self.health} здоровья')
                self.health -= 1
                if self.health == 0:
                    await ctx.send('***ЭТО КОНЕЦ***\n\nИспользуйте команду `*startgme`, чтобы начать новую игру')
                    self.choosing_a_room = False
                    self.combat_room = False
            if self.item_ace is True and (self.player_dice1 == 1 or self.player_dice2 == 1):
                await ctx.send(f'Вам выпала единица, <:small_rock:967843198716244100> наносит всем врагам 1 урон!')
                if not self.enemy_melee == 0:
                    self.enemy_melee_hp -= 1
                    if self.enemy_melee_hp == 0:
                        self.enemy_melee = self.enemy_middle
                        self.enemy_ranged = self.enemy_middle
                        self.enemy_melee_hp = self.enemy_middle_hp
                        self.enemy_middle_hp = self.enemy_ranged_hp
                        self.enemy_ranged_hp = 0
                        self.enemy_ranged = 0
                if not self.enemy_middle == 0:
                    self.enemy_middle_hp -= 1
                    if self.enemy_middle_hp == 0:
                        self.enemy_middle = self.enemy_ranged
                        self.enemy_ranged = 0
                        self.enemy_middle_hp = self.enemy_ranged_hp
                        self.enemy_ranged_hp = 0
                if not self.enemy_ranged == 0:
                    self.enemy_ranged_hp -= 1
                    if self.enemy_ranged_hp == 0:
                        self.enemy_ranged = 0
                if self.enemy_melee == 0 and self.enemy_middle == 0 and self.enemy_ranged == 0:
                    if self.rooms < 16:
                        roll2 = random.randint(20, 50)
                        self.gold = self.gold + roll2
                        await ctx.send(f'Победа! Вы получаете {roll2} золота. У вас {self.health} здоровья и '
                                       f'{self.gold} золота')
                        if self.item_healingplant is True:
                            self.health += 2
                            if self.character == '<:plant_knight:967517250984751114>' and self.health > 27:
                                self.health = 27
                            await ctx.send(f'<:healing_plant:967846012590903327> восстановил вам два здоровья. У вас '
                                           f'{self.health} здоровья')
                        self.combat_room = False
                        self.choosing_a_room = True
                    else:
                        await ctx.send(f'Вы прошли игру! Поздравляем! Ваша награда: случайный котик!')
                        response = requests.get('https://api.thecatapi.com/v1/images/search')
                        data = response.json()
                        await ctx.send(data[0]['url'])
                        await ctx.send('Используйте команду `*startgame`, чтобы начать новую игру')
                        self.combat_room = False
                        self.choosing_a_room = False
            if self.player_dice1 == 1 or self.player_dice2 == 1 or self.player_dice3 == 1:
                if self.weapon1 == self.weaponlist[3] or self.weapon1 == self.weaponlist[4] or \
                        self.weapon1 == self.cursedweaponlist[1] or self.weapon1 == self.cursedweaponlist[2]:
                    self.weapon1_active = True
                    await ctx.send(f'Ваше первое оружие - {self.weapon1} - активируется!')
            elif self.player_dice1 == 2 or self.player_dice2 == 2 or self.player_dice3 == 2:
                if self.weapon1 == self.weaponlist[1] or self.weapon1 == self.weaponlist[4] or \
                        self.weapon1 == self.cursedweaponlist[2]:
                    self.weapon1_active = True
                    await ctx.send(f'Ваше первое оружие - {self.weapon1} - активируется!')
            elif self.player_dice1 == 3 or self.player_dice2 == 3 or self.player_dice3 == 3:
                if self.weapon1 == self.weaponlist[1] or self.weapon1 == self.weaponlist[4] or \
                        self.weapon1 == self.cursedweaponlist[1] or self.weapon1 == self.cursedweaponlist[2] or \
                        self.weapon1 == self.cursedweaponlist[0]:
                    self.weapon1_active = True
                    await ctx.send(f'Ваше первое оружие - {self.weapon1} - активируется!')
            elif self.player_dice1 == 4 or self.player_dice2 == 4 or self.player_dice3 == 4:
                if self.weapon1 == self.weaponlist[0] or self.weapon1 == self.weaponlist[2] or \
                        self.weapon1 == self.cursedweaponlist[2] or self.weapon1 == self.cursedweaponlist[0]:
                    self.weapon1_active = True
                    await ctx.send(f'Ваше первое оружие - {self.weapon1} - активируется!')
            elif self.player_dice1 == 5 or self.player_dice2 == 5 or self.player_dice3 == 5:
                if self.weapon1 == self.weaponlist[0] or self.weapon1 == self.weaponlist[2] or \
                        self.weapon1 == self.weaponlist[5] or self.weapon1 == self.cursedweaponlist[2]:
                    self.weapon1_active = True
                    await ctx.send(f'Ваше первое оружие - {self.weapon1} - активируется!')
            elif self.player_dice1 == 6 or self.player_dice2 == 6 or self.player_dice3 == 6:
                if self.weapon1 == self.weaponlist[0] or self.weapon1 == self.weaponlist[2] or \
                        self.weapon1 == self.weaponlist[5] or self.weapon1 == self.cursedweaponlist[2] or self.weapon1\
                        == self.cursedweaponlist[1]:
                    self.weapon1_active = True
                    await ctx.send(f'Ваше первое оружие - {self.weapon1} - активируется!')
            if self.player_dice1 == 1 or self.player_dice2 == 1 or self.player_dice3 == 1:
                if self.weapon2 == self.weaponlist[3] or self.weapon2 == self.weaponlist[4] or \
                        self.weapon2 == self.cursedweaponlist[1] or self.weapon2 == self.cursedweaponlist[2]:
                    self.weapon2_active = True
                    await ctx.send(f'Ваше второе оружие - {self.weapon2} - активируется!')
            elif self.player_dice1 == 2 or self.player_dice2 == 2 or self.player_dice3 == 2:
                if self.weapon2 == self.weaponlist[1] or self.weapon2 == self.weaponlist[4] or \
                        self.weapon2 == self.cursedweaponlist[2]:
                    self.weapon2_active = True
                    await ctx.send(f'Ваше второе оружие - {self.weapon2} - активируется!')
            elif self.player_dice1 == 3 or self.player_dice2 == 3 or self.player_dice3 == 3:
                if self.weapon2 == self.weaponlist[1] or self.weapon2 == self.weaponlist[4] or \
                        self.weapon2 == self.cursedweaponlist[1] or self.weapon2 == self.cursedweaponlist[2] or \
                        self.weapon2 == self.cursedweaponlist[0]:
                    self.weapon2_active = True
                    await ctx.send(f'Ваше второе оружие - {self.weapon2} - активируется!')
            elif self.player_dice1 == 4 or self.player_dice2 == 4 or self.player_dice3 == 4:
                if self.weapon2 == self.weaponlist[0] or self.weapon2 == self.weaponlist[2] or \
                        self.weapon2 == self.cursedweaponlist[2] or self.weapon2 == self.cursedweaponlist[0]:
                    self.weapon2_active = True
                    await ctx.send(f'Ваше второе оружие - {self.weapon2} - активируется!')
            elif self.player_dice1 == 5 or self.player_dice2 == 5 or self.player_dice3 == 5:
                if self.weapon2 == self.weaponlist[0] or self.weapon2 == self.weaponlist[2] or \
                        self.weapon2 == self.weaponlist[5] or self.weapon2 == self.cursedweaponlist[2]:
                    self.weapon2_active = True
                    await ctx.send(f'Ваше второе оружие - {self.weapon2} - активируется!')
            elif self.player_dice1 == 6 or self.player_dice2 == 6 or self.player_dice3 == 6:
                if self.weapon2 == self.weaponlist[0] or self.weapon2 == self.weaponlist[2] or \
                        self.weapon2 == self.weaponlist[5] or self.weapon2 == self.cursedweaponlist[2] or self.weapon2\
                        == self.cursedweaponlist[1]:
                    self.weapon2_active = True
                    await ctx.send(f'Ваше второе оружие - {self.weapon2} - активируется!')
            if self.weapon1_active is True and self.weapon1 == self.weaponlist[5]:
                self.weapon1_active = False
                self.health += 3
                if self.character == '<:plant_knight:967517250984751114>' and self.health > 27:
                    self.health = 27
                if self.character == '<:desert_wanderer:967522631190462474>' and self.health > 22:
                    self.health = 22
                await ctx.send(f'{self.weaponlist[5]} лечит вам 3 здоровья. Теперь у вас {self.health} здоровья.')
            if self.weapon2_active is True and self.weapon2 == self.weaponlist[5]:
                self.weapon2_active = False
                self.health += 3
                if self.character == '<:plant_knight:967517250984751114>' and self.health > 27:
                    self.health = 27
                if self.character == '<:desert_wanderer:967522631190462474>' and self.health > 22:
                    self.health = 22
                await ctx.send(f'{self.weaponlist[5]} лечит вам 3 здоровья. Теперь у вас {self.health} здоровья.')
            if self.weapon1_active is True and self.weapon1 == self.weaponlist[3]:
                self.weapon1_active = False
                self.status_block = True
                await ctx.send(f'{self.weaponlist[3]} накладывает на вас <:token_block:967533280457015345>')
            if self.weapon2_active is True and self.weapon2 == self.weaponlist[3]:
                self.weapon2_active = False
                self.status_block = True
                await ctx.send(f'{self.weaponlist[3]} накладывает на вас <:token_block:967533280457015345>')
            await ctx.send('Используйте команду `*attack [1 или 2] [melee, middle, ranged]`, чтобы атаковать '
                           'врага в указанной вами позиции')
        else:
            await ctx.send('Сейчас вы не находитесь в бою')

    @commands.command(name='attack')
    async def attack(self, ctx, attacking_weapon, enemyposition):
        if self.combat_room is True:
            if attacking_weapon == '1':
                if self.weapon1_active is True:
                    if self.weapon1 == '<:arbalet:967483215013105764>':
                        if enemyposition == 'melee':
                            await ctx.send('Арбалет не может атаковать ближнюю позицию')
                        if enemyposition == 'middle' and not self.enemy_middle == 0:
                            self.enemy_middle_hp -= 3
                            self.weapon1_active = False
                            await ctx.send(f'Вы наносите {self.enemy_middle} 3 урона')
                        if enemyposition == 'ranged' and not self.enemy_ranged == 0:
                            self.enemy_ranged_hp -= 3
                            self.weapon1_active = False
                            await ctx.send(f'Вы наносите {self.enemy_ranged} 3 урона')
                    if self.weapon1 == '<:kinjal:967479576366305351>':
                        if enemyposition == 'melee':
                            await ctx.send(f'Вы наносите {self.enemy_melee} 2 урона')
                            self.enemy_melee_hp -= 2
                            self.weapon1_active = False
                        if enemyposition == 'middle' and not self.enemy_middle == 0:
                            self.enemy_middle_hp -= 2
                            self.weapon1_active = False
                            await ctx.send(f'Вы наносите {self.enemy_middle} 2 урона')
                        if enemyposition == 'ranged' and not self.enemy_ranged == 0:
                            await ctx.send(f'Кинжал не может атаковать дальнюю позицию')
                    if self.weapon1 == '<:sword:967485121479462932>':
                        if enemyposition == 'melee':
                            await ctx.send(f'Вы наносите {self.enemy_melee} 5 урона')
                            self.enemy_melee_hp -= 5
                            self.weapon1_active = False
                        if enemyposition == 'middle':
                            await ctx.send('Меч не может атаковать дальнюю позицию')
                        if enemyposition == 'ranged':
                            await ctx.send('Меч не может атаковать дальнюю позицию')


bot = commands.Bot(command_prefix='*')
bot.add_cog(MainBot(bot))
bot.run(TOKEN)