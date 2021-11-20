import keep_alive
import discord
import asyncio
import time
from traceback import format_list, extract_tb


from datetime import datetime
import json
import random
import re
import sys
import os
from discord.ext import commands

TOKEN = 'OTExMDAwMjU0MzgyNDg5NjQx.YZbBGg.i31vNlSp1HBE-t48bm0VG4yk9VA'

bot = commands.Bot(command_prefix='!')  # инициализируем бота с префиксом '!'

@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def rules(message):  # создаем асинхронную фунцию бота
    await message.channel.send(
        '1. Задача спецназа отбивать атаки мурлока \n'
        '2. Задача химика давать бафф спецназу и разрабатывать лекарство против болезни \n'
        '3. Задача мурлока атаковать аванпосты и в конечном итоге главый город, также мурлок может заражать других участников \n'
    )


# ----------------------------------- MURLOCK ------------------------------------------------------
@bot.command(pass_context=True)
async def murlock(messageM):
    await messageM.channel.send(
        '--База мурлока-- \n'
        '1. Царь Мурлок может проводить улучшение для мурлоков: урон, защита, здоровье \n'
        '2. Царь Мурлок может нанимать спец.отряд: подрывник, снайпер, огнеметчик \n'
        '3. Царь Мурлок может создавать ловушки для спецназа во время вылазки \n'
        '4. Нанять обычных мурлоков, в день можно нанимать 100 мурлоков, лимит неограничен \n'
        '5. Узнать свою мощь (характеристики и количество солдат) \n'
        'Выбери цифру, что ты хочешь сделать (пример !1, !2, !3, !4, !5) \n')


# -----------------------------------------------------------------------------------------
attack_murlock = -4
protection_murlock = 2
health_murlock = 10
murloc_army = 250
bomber_counter = 2
sniper_counter = 1
flamethrower_counter = 0
fake_counter = True
field_counter = False

# ----- 1 -----
@bot.command(pass_context=True)
async def one(message_one):  # ВЫБРАНА ЦИФРА 1
    await message_one.channel.send(
        'Что вы хотите улучшить? \n' 
        'Пример: !damage, !protection, !health \n')


@bot.command(pass_context=True)
async def damage(message_damage):  # УЛУЧШЕНИЕ УРОНА
    global attack_murlock
    attack_murlock += 1
    await message_damage.channel.send('Урон усилен на 1 единицу')


@bot.command(pass_context=True)
async def protection(message_protection):  # УЛУЧШЕНИЕ ЗАЩИТЫ
    global protection_murlock
    protection_murlock += 1
    await message_protection.channel.send('Защита усилена на 1 единицу')


@bot.command(pass_context=True)
async def health(message_health):  # УЛУЧШЕНИЕ ЗДОРОВЬЯ
    global health_murlock
    health_murlock += 10
    await message_health.channel.send('Здоровье увеличено на 10 единиц')


# -----------------------------------------------------------------------------------------
# ----- 2 -----
@bot.command(pass_context=True)
async def two(message_two):  # ВЫБРАНА ЦИФРА 2
    await message_two.channel.send('Кого вы хотите нанять? (пример !подрывник)'
                                   )


@bot.command(pass_context=True)
async def bomber(message_bomber):  # НАЕМ ПОДРЫВНИКА
    global bomber_counter
    if bomber_counter == 0 or 1:
        bomber_counter += 1
        await message_bomber.channel.send('Подрывник нанят')
    else:
        await message_bomber.channel.send('Превышен лимит подрывников')


@bot.command(pass_context=True)
async def sniper(message_sniper):  # НАЕМ СНАЙПЕРА
    global sniper_counter
    if sniper_counter == 0:
        sniper_counter += 1
        await message_sniper.channel.send('Снайпер нанят')
    else:
        await message_sniper.channel.send('Превышен лимит снайперов')


@bot.command(pass_context=True)
async def flamethrower(message_flamethrower):  # НАЕМ ОГНЕМЕТЧИКА
    global flamethrower_counter
    if flamethrower_counter == 0 or 1:
        flamethrower_counter += 1
        await message_flamethrower.channel.send('Огнеметчик нанят')
    else:
        await message_flamethrower.channel.send('Превышен лимит огнеметчиков')


# -----------------------------------------------------------------------------------------
# ----- 3 -----
@bot.command(pass_context=True)
async def three(message_three):
    await message_three.channel.send(
        'Какую ловушку вы хотите создать? \n'
        '1. Защитное поле, в течение 6-и часов спецназ не может начать вылазку \n'
        '2. Фальшивый мурлок, при успешной вылазке, прогресс вакцины падает на 1% (лучше всего использовать на последней минуте вылазки) \n'
        'Пример выбора: !field - защитное поле, !fake - фальшивый мурлок \n')


@bot.command(pass_context=True)
async def field(message_field):
    global field_counter
    field_counter = True
    await message_field.channel.send('Защитное поле - активно')


@bot.command(pass_context=True)
async def fake(message_fake):
    global fake_counter
    fake_counter = True
    await message_fake.channel.send('Фальшивый мурлок - активно')


# -----------------------------------------------------------------------------------------
# ----- 4 -----
@bot.command(pass_context=True)
async def four(message_four):
    await message_four.channel.send('Можно нанять 25 мурлоков')


@bot.command(pass_context=True)
async def army(message_army):
    global murloc_army
    murloc_army += 25
    await message_army.channel.send('Мурлоки наняты')


# -----------------------------------------------------------------------------------------
# ----- 5 -----
@bot.command(pass_context=True)
async def five(message_five):
    await message_five.channel.send('Урон мурлоков: {} \n'
                                    'Защита мурлоков: {} \n'
                                    'Здоровье мурлоков: {} \n'
                                    'Мурлоки: {} \n'
                                    'Подрывники: {} \n'
                                    'Снайперы: {} \n'
                                    'Огнеметчики: {} \n'
                                    'Защитное поле: {} \n'
                                    'Фальшивый мурлок: {} \n'.format(attack_murlock, protection_murlock, health_murlock, murloc_army, bomber_counter, sniper_counter, flamethrower_counter, field_counter, fake_counter))

# ==================================== КОМАНДЫ ДРУГИЕ ========================================
@bot.command(pass_context=True)
async def save(message_save):
    num = random.randint(0,100)
    if num < 70:
      await message_save.channel.send('К сожалению вам не удалось сбежать, выпало число: {}'.format(num))
    if num >= 70:
      await message_save.channel.send('Вам удалось сбежать из лап кровожадного мурлока! Выпало число: {}'.format(num))
# ------------------------------------------------- 

# ========================================= СПЕЦНАЗ =========================================================
@bot.command(pass_context=True)
async def spetsnaz(messageS):
    await messageS.channel.send('Управление солдатами и своими характеристиками \n'
                                '1. Выбрать автомат \n'
                                '2. Прокачать солдат \n'
                                '3. Обучить спец.войска \n'
                                '4. Собрать армию \n'
                                '5. Вывести стату армии \n'
                                'Как выбрать? Пример: !getauto, !twoS, !threeS, !arm, !stat \n')
# ----------------------------------------------------------------------------------------------------------
updd_solder = 5.5
updef_solder= 0.5
uphp_solder = 5
solder_army = 15
stormtrooper_counter = 0
gunner_counter = 0
tank_counter = 1
@bot.command(pass_context=True)
async def getauto(message_getauto):         # ВЫБОР АВТОМАТА
    await message_getauto.channel.send('1. ╾━╤デ╦︻ - М4А1 (Хороший урон и скорость стрельбы по мурлокам) \n'
                                       '2. ︻╦̵̵͇══╤─ - РПД (Много патронов, сдерживает большие атаки мурлоков) \n'
                                       '3. ︻╦╤─ - MP7 (Высокая скорость стрельбы по мурлокам) \n'
                                       '4. ︻デ┳═ー - ВСС (Лучший друг спецназа на вылазке) \n'
                                       '5. ⌐╦╦═─ - Berreta (Очень высокий урон по мурлокам, но мало патронов) \n'
                                       '6. ︻◦◤══一 - XM7 (Убойная сила на близкой дистанции) \n'
                                       'Пример: !m4a1, !rpd, !mp7, !vss, !berreta, !xm7 \n')

@bot.command(pass_context=True)     # m4a1
async def m4a1(message_m4a1):
    await message_m4a1.channel.send('Вы выбрали М4А1')

@bot.command(pass_context=True)         # rpd
async def rpd(message_rpd):
    await message_rpd.channel.send('Вы выбрали РПД')

@bot.command(pass_context=True)         # mp7
async def mp7(message_mp7):
    await message_mp7.channel.send('Вы выбрали МP7')

@bot.command(pass_context=True)         # vss
async def vss(message_vss):
    await message_vss.channel.send('Вы выбрали ВСС')

@bot.command(pass_context=True)         # berreta
async def berreta(message_berreta):
    await message_berreta.channel.send('Вы выбрали Berreta')

@bot.command(pass_context=True)         # xm7
async def xm7(message_xm7):
    await message_xm7.channel.send('Вы выбрали XM7')
#--------------------------------------------------------------------------------------
@bot.command(pass_context=True)
async def twoS(message_twoS):           # ВЫБРАНА ЦИФРА 2
    await message_twoS.channel.send('1. Прокачать урон солдат \n'
                                    '2. Прокачать защиту солдат \n'
                                    '3. Увеличить здоровье солдат \n'
                                    'Пример !updd, !updef, !uphp \n')

@bot.command(pass_context=True)
async def updd(message_updd):
    global updd_solder
    updd_solder += 1
    await message_updd.channel.send('Атака усилена на 0.5 единиц')

@bot.command(pass_context=True)
async def updef(message_updef):
    global updef_solder
    updef_solder += 1
    await message_updef.channel.send('Защита усилена на 0.5 единиц')

@bot.command(pass_context=True)
async def uphp(message_uphp):
    global uphp_solder
    uphp_solder += 1
    await message_uphp.channel.send('Здоровье увеличено на 5 единиц')
#--------------------------------------------------------------------------------------
@bot.command(pass_context=True)
async def threeS(message_threeS):         # ВЫБРАНА ЦИФРА 3
    await message_threeS.channel.send('Кого вы хотите нанять? \n'
                                      '1. Штурмовик \n'
                                      '2. Пулеметчик \n'
                                      '3. Танк \n'
                                      'Пример: !stormtrooper, !gunner, !tank \n')

@bot.command(pass_context=True)
async def stormtrooper(message_stormtrooper):         # НАЕМ ШТУРМОВИКА
    global stormtrooper_counter
    if stormtrooper_counter <= 10:
        stormtrooper_counter += 1
        await message_stormtrooper.channel.send('Штурмовик нанят')
    else:
        await message_stormtrooper.channel.send('Превышен лимит штурмовиков')
        
@bot.command(pass_context=True)
async def gunner(message_gunner):         # НАЕМ ПУЛЕМЕТЧИКА
    global gunner_counter
    if gunner_counter <= 5:
        gunner_counter += 1
        await message_gunner.channel.send('Пулеметчик нанят')
    else:
        await message_gunner.channel.send('Превышен лимит пулеметчиков')
        
@bot.command(pass_context=True)
async def tank(message_tank):         # НАЕМ ТАНКА
    global tank_counter
    if tank_counter <= 2:
        tank_counter += 1
        await message_tank.channel.send('Танк нанят')
    else:
        await message_tank.channel.send('Превышен лимит танков')
        
@bot.command(pass_context=True)
async def arm(message_arm):
    global solder_army
    solder_army += 15
    await message_arm.channel.send('Солдаты наняты +15')
    
@bot.command(pass_context=True)
async def stat(message_stat):
    await message_stat.channel.send('Урон солдат: {} \n'
                                    'Защита солдат: {} \n'
                                    'Здоровье солдат: {} \n'
                                    'Солдаты: {} \n'
                                    'Штурмовики: {} \n'
                                    'Пулеметчики: {} \n'
                                    'Танки: {} \n'.format(updd_solder,updef_solder,uphp_solder,solder_army,
                                              stormtrooper_counter,gunner_counter,tank_counter))

# ============================================ ХИМИКИ ==================================================
@bot.command(pass_context=True)
async def chemist(message_chemist):
    await message_chemist.channel.send('Управление наукой \n'
                                       '1. Дать постоянный бафф союзным солдатам, вероятность 50% \n'
                                       '2. Провести опыты на мурлоке, вероятность 20% \n'
                                       '3. Анализ клеток, вероятность 10% - успешно, 20% - отрицательные баффы солдатам \n'
                                       '10% - положительные баффы солдатам, 60% - не успешно \n'
                                       '4. Прогресс вакцины \n'
                                       'Пример: !buff, !exp, !analysis, !lab \n')
# ---------------------------------------------------------------------------------------------------------
@bot.command(pass_context=True)
async def buff(message_buff):
    await message_buff.channel.send('Какой бафф хотите дать? \n'
                                    '1. Бафф к урону \n'
                                    '2. Бафф к защите \n'
                                    '3. Бафф к здоровью \n'
                                    'Пример: !buffdd, !buffdef, !buffhp \n')

@bot.command(pass_context=True)
async def buffdd(message_buffdd):
    global updd_solder
    num_dd = random.randint(0, 100)
    if num_dd >= 50:
        updd_solder += 5
        await message_buffdd.channel.send('Солдаты получили +5 к урону')
    elif num_dd < 50:
        updd_solder -= 5
        await message_buffdd.channel.send('Бафф прошел неудачно, солдаты получили -5 к урону')

@bot.command(pass_context=True)
async def buffdef(message_buffdef):
    global updef_solder
    num_def = random.randint(0, 100)
    if num_def >= 50:
        updef_solder += 5
        await message_buffdef.channel.send('Солдаты получили +5 к защите')
    elif num_def < 50:
        updef_solder -= 5
        await message_buffdef.channel.send('Бафф прошел неудачно, солдаты получили -5 к защите')

@bot.command(pass_context=True)
async def buffhp(message_buffhp):
    global uphp_solder
    num_hp = random.randint(0, 100)
    if num_hp >= 50:
        uphp_solder += 5
        await message_buffhp.channel.send('Солдаты получили +10 к здоровью')
    elif num_hp < 50:
        uphp_solder -= 5
        await message_buffhp.channel.send('Бафф прошел неудачно, солдаты получили -10 к здоровью')
# ---------------------------------------------------------------------------------------------------------
@bot.command(pass_context=True)
async def exp(message_exp):
    num_exp = random.randint(0, 100)
    if num_exp >= 80:
        r_buff = random.randint(1,3)
        if r_buff == 1:
            global attack_murlock
            attack_murlock -= 5
            await message_exp.channel.send('Опыты прошли успешно, мурлок получил -5 к урону')
        elif r_buff == 2:
            global protection_murlock
            protection_murlock -= 5
            await message_exp.channel.send('Опыты прошли успешно, мурлок получил -5 к защите')
        elif r_buff == 3:
            global health_murlock
            health_murlock -= 10
            await message_exp.channel.send('Опыты прошли успешно, мурлок получил -10 к здоровью')
    elif num_exp < 80:
        await message_exp.channel.send('Опыты прошли не успешно')
# ---------------------------------------------------------------------------------------------------------
vaccine = 0         # Прогресс к вакцине
@bot.command(pass_context=True)
async def analysis(message_analysis):
    global updd_solder
    global updef_solder
    global uphp_solder
    num_analysis = random.randint(0, 100)
    if 0 < num_analysis <= 10:
        global vaccine
        vaccine += 1
        await message_analysis.channel.send('Анализ клеток прошел успешно, прогресс к вакцине +1')
    elif 11 < num_analysis <= 20:
        r_buff = random.randint(1,3)
        if r_buff == 1:
            updd_solder += 5
            await message_analysis.channel.send('Опыты прошли успешно, солдаты получили +5 к урону')
        elif r_buff == 2:
            updef_solder += 5
            await message_analysis.channel.send('Опыты прошли успешно, солдаты получили +5 к защите')
        elif r_buff == 3:
            uphp_solder += 5
            await message_analysis.channel.send('Опыты прошли успешно, солдаты получили +10 к здоровью')
    elif 21 < num_analysis <= 40:
        r_buff = random.randint(1,3)
        if r_buff == 1:
            updd_solder -= 5
            await message_analysis.channel.send('Опыты прошли не успешно, солдаты получили -5 к урону')
        elif r_buff == 2:
            updef_solder -= 5
            await message_analysis.channel.send('Опыты прошли не успешно, солдаты получили -5 к защите')
        elif r_buff == 3:
            uphp_solder -= 10
            await message_analysis.channel.send('Опыты прошли не успешно, солдаты получили -10 к здоровью')
    elif 41 < num_analysis <= 100:
        await message_analysis.channel.send('Анализ клеток прошел не успешно')

@bot.command(pass_context=True)
async def lab(message_lab):
    await message_lab.channel.send('Прогресс вакцины: {} \n'.format(vaccine))

# ============================================ РЕЖИМ СРАЖЕНИЯ ==============================================
@bot.command(pass_context=True)
async def fight(message_fight):
    global murloc_army      # Армия мурлока
    global bomber_counter       # Подрывники мурлока
    global flamethrower_counter     # Огнеметчики мурлока
    global sniper_counter       # Снайперы мурлока
    global solder_army      # Армия людей
    global stormtrooper_counter     # Штурмовики людей
    global gunner_counter       # Пулеметчики людей
    global tank_counter     # Танки людей
    global updd_solder      # Атака людей
    global updef_solder     # Защита людей
    global uphp_solder      # Здоровье людей
    global attack_murlock       # Атака мурлоков
    global protection_murlock       # Защита мурлоков
    global health_murlock       # Здоровье мурлоков
    r_fight = random.randint(0,100)
    figthS_counter = 0
    figthM_counter = 0
    for i in range(3):
        await message_fight.channel.send('Мурлок начинает атаку!!! ВСЕ НА ЗАЩИТУ СРОЧНО!!!')
        time.sleep(3)
    if murloc_army >= solder_army or murloc_army < solder_army:
        time.sleep(5)
        if murloc_army >= solder_army:
            await message_fight.channel.send('Солдаты сражаются не на жизнь, а на смерть! \n'
                                            'Но численное преимущество за мурлоками! \n')
        elif murloc_army < solder_army:
            await message_fight.channel.send('Солдаты сражаются не на жизнь, а на смерть! \n'
                                             'Численное преимущество за солдатами! \n')
        time.sleep(10)
        await message_fight.channel.send('СОЛДАТЫ НАЧИНАЮТ СДАВАТЬ ПОЗИЦИИ, МУРЛОКИ ВСЕ СИЛЬНЕЕ НАСТУПАЮТ')
        time.sleep(2)
        await message_fight.channel.send('ЦАРЬ МУРЛОК ИЗДАЕТ БОЕВОЙ КЛИЧ! МГРЛЛЛЛЛЛЛЛЛЛЛЛЛЛЛЛЛЛЛЛЛЛЛ!!!!!!!!')
        # ============= СРАВНЕНИЕ АТАКИ ================
        time.sleep(5)
        if attack_murlock > updd_solder:
            figthM_counter += 1
            await message_fight.channel.send('МРГЛЛЛЛЛЛЛЛ!!!!!!')
        elif attack_murlock == updd_solder:
            if 0 < r_fight <= 50:
                figthM_counter += 1
                await message_fight.channel.send('МРГЛЛЛЛЛЛЛЛЛЛЛЛЛЛЛЛ!!!!!!!!')
            elif 51 < r_fight <= 100:
                figthS_counter += 1
                await message_fight.channel.send('Удерживаем позиции!!!!!')
        elif attack_murlock < updd_solder:
            figthS_counter += 1
            await message_fight.channel.send('Удерживаем позиции!!!!!')
        # ============= СРАВНЕНИЕ ЗАЩИТЫ ================
        time.sleep(5)
        if protection_murlock > updef_solder:
            figthM_counter += 1
            await message_fight.channel.send('МРГЛЛЛЛЛЛЛЛ!!!!!!')
        elif protection_murlock == updef_solder:
            if 0 < r_fight <= 50:
                figthM_counter += 1
                await message_fight.channel.send('МРГЛЛЛЛЛЛЛЛЛЛЛЛЛЛЛЛ!!!!!!!!')
            elif 51 < r_fight <= 100:
                figthS_counter += 1
                await message_fight.channel.send('Удерживаем позиции!!!!!')
        elif protection_murlock < updef_solder:
            figthS_counter += 1
            await message_fight.channel.send('Удерживаем позиции!!!!!')
        # ============= СРАВНЕНИЕ ЗДОРОВЬЯ ================
        time.sleep(5)
        if health_murlock > uphp_solder:
            figthM_counter += 1
            await message_fight.channel.send('МРГЛЛЛЛЛЛЛЛ!!!!!!')
        elif health_murlock == uphp_solder:
            if 0 < r_fight <= 50:
                figthM_counter += 1
                await message_fight.channel.send('МРГЛЛЛЛЛЛЛЛЛЛЛЛЛЛЛЛ!!!!!!!!')
            elif 51 < r_fight <= 100:
                figthS_counter += 1
                await message_fight.channel.send('Удерживаем позиции!!!!!')
        elif health_murlock < uphp_solder:
            figthS_counter += 1
            await message_fight.channel.send('Удерживаем позиции!!!!!')
        time.sleep(2)
        if figthM_counter > figthS_counter:
            await message_fight.channel.send('МУРЛОКИ ПРОРВАЛИ ОБОРОНУ, СОЛДАТЫ ОТСТУПАЮТ!')
        elif figthM_counter == figthS_counter:
            await message_fight.channel.send('СРАЖЕНИЕ ВСЕ ПРОДОЛЖАЕТСЯ!')
        elif figthM_counter < figthS_counter:
            await message_fight.channel.send('СОЛДАТЫ ВЗЯЛИ ИНИЦИАТИВУ НА СЕБЯ, ОНИ НАСТУПАЮТ!')

        # ============= ПОДКРЕПЛЕНИЕ ================
        time.sleep(5)
        await message_fight.channel.send('======================= \n'
        'ПОДКРЕПЛЕНИЕ С ОБЕИХ СТОРОН! *специальный войска вступают в схватку* \n')
        if 0 < stormtrooper_counter <= 10 and 0 < sniper_counter <= 2:
            await message_fight.channel.send('Штурмовики вступают в бой!')
            time.sleep(4)
            await message_fight.channel.send('СНАЙПЕРЫ!!!!!!')
        if 0 < stormtrooper_counter <= 10 and murloc_army >= 0:
            await message_fight.channel.send('*противник на 12 градусов, открыть огонь!* \n'
                                             'Шквал пуль обружился на мурлоков \n')
        time.sleep(3)
        if 0 < gunner_counter <= 5 and 0 < flamethrower_counter <= 2:
            await message_fight.channel.send('Пулеметчики открыли огонь \n'
                                             'Огнеметчики открыли огонь \n')
        if 0 < gunner_counter <= 5 and murloc_army >= 0:
            await message_fight.channel.send('НЫЫЫЫААААААААААААААААААААААААААА!!!!!!!!! \n'
                                             'МЯСОООООООООО!!!!! \n')
        time.sleep(5)
        if 0 < tank_counter <= 2 and 0 < bomber_counter <= 2:
            await message_fight.channel.send('Танки!')
            time.sleep(2)
            await message_fight.channel.send('БАХ!')
        if 0 < tank_counter <= 2 and murloc_army >= 0:
            await message_fight.channel.send('Мурлоки бегут на танк!')
        time.sleep(10)
        await message_fight.channel.send('Солдаты и мурлоки схлеснулись в ожесточонной схватке \n'
                                         'Результаты сражения: \n'
                                         '======================= \n')                                 

        # ============= ПОДСЧЕТ ПОТЕРЬ ================
        if figthM_counter > figthS_counter:     # ПОТЕРИ ЛЮДЕЙ, при плохих навыках и ПОТЕРИ МУРЛОКОВ, при хороших навыках
            if 0 < r_fight <= 50:       # Ужасный исход для людей
                solder_army -= 100
                if solder_army < 0:
                    solder_army = 0
                stormtrooper_counter -= 4
                if stormtrooper_counter < 0:
                    stormtrooper_counter = 0
                gunner_counter -= 3
                if gunner_counter < 0:
                    gunner_counter = 0
                tank_counter -= 2
                if tank_counter < 0:
                    tank_counter = 0
                await message_fight.channel.send('Со стороны людей огромные потери!')
            if 51 < r_fight <= 60:      # Благоприятный исход для людей
                solder_army -= 50
                if solder_army < 0:
                    solder_army = 0
                stormtrooper_counter -= 2
                if stormtrooper_counter < 0:
                    stormtrooper_counter = 0
                gunner_counter -= 1
                if gunner_counter < 0:
                    gunner_counter = 0
                tank_counter -= 1
                if tank_counter < 0:
                    tank_counter = 0
                await message_fight.channel.send('Со стороны людей маленькие потери!')
            if 61 < r_fight <= 100:      # Посредственный исход для людей
                solder_army -= 75
                if solder_army < 0:
                    solder_army = 0
                stormtrooper_counter -= 3
                if stormtrooper_counter < 0:
                    stormtrooper_counter = 0
                gunner_counter -= 2
                if gunner_counter < 0:
                    gunner_counter = 0
                tank_counter -= 1
                if tank_counter < 0:
                    tank_counter = 0
                await message_fight.channel.send('Со стороны людей средние потери!')

            # ================================================
            if 0 < r_fight <= 50:       # Хороший исход для мурлоков
                murloc_army -= 50
                if murloc_army < 0:
                    murloc_army = 0
                sniper_counter -= 0
                if sniper_counter < 0:
                    sniper_counter = 0
                flamethrower_counter -= 1
                if flamethrower_counter < 0:
                    flamethrower_counter = 0
                bomber_counter -= 1
                if bomber_counter < 0:
                    bomber_counter = 0
                await message_fight.channel.send('Со стороны мурлоков слабые потери!')
            if 51 < r_fight <= 90:  # Средний исход для мурлоков
                murloc_army -= 100
                if murloc_army < 0:
                    murloc_army = 0
                sniper_counter -= 1
                if sniper_counter < 0:
                    sniper_counter = 0
                flamethrower_counter -= 1
                if flamethrower_counter < 0:
                    flamethrower_counter = 0
                bomber_counter -= 1
                if bomber_counter < 0:
                    bomber_counter = 0
                await message_fight.channel.send('Со стороны мурлоков средние потери!')
            if 91 < r_fight <= 100:  # Плохой исход для мурлоков
                murloc_army -= 200
                if murloc_army < 0:
                    murloc_army = 0
                sniper_counter -= 2
                if sniper_counter < 0:
                    sniper_counter = 0
                flamethrower_counter -= 2
                if flamethrower_counter < 0:
                    flamethrower_counter = 0
                bomber_counter -= 2
                if bomber_counter < 0:
                    bomber_counter = 0
                await message_fight.channel.send('Со стороны мурлоков сильные потери!')
            await message_fight.channel.send('Результаты боя! \n')

            await message_fight.channel.send('======================= \n'
                                            'АРМИЯ МУРЛОКОВ: \n'
                                            'Мурлоки: {} \n'
                                            'Подрывники: {} \n'
                                            'Снайперы: {} \n'
                                            'Огнеметчики: {} \n'
                                            '======================= \n'.format(murloc_army, bomber_counter,
                                                                  sniper_counter, flamethrower_counter))
            await message_fight.channel.send('======================= \n'
                                             'АРМИЯ ЛЮДЕЙ: \n'
                                             'Солдаты: {} \n'
                                             'Штурмовики: {} \n'
                                             'Пулеметчики: {} \n'
                                             'Танки: {} \n'
                                             '======================= \n'.format(solder_army, stormtrooper_counter,
                                                                  gunner_counter, tank_counter))
        
        
        if figthM_counter < figthS_counter:     # ПОТЕРИ МУРЛОКОВ, при плохих навыках и ПОТЕРИ ЛЮДЕЙ, при хороших навыках
            if 0 < r_fight <= 50:       # Ужасный исход для мурлоков
                murloc_army -= 400
                if murloc_army < 0:
                    murloc_army = 0
                sniper_counter -= 2
                if sniper_counter < 0:
                    sniper_counter = 0
                flamethrower_counter -= 2
                if flamethrower_counter < 0:
                    flamethrower_counter = 0
                bomber_counter -= 2
                if bomber_counter < 0:
                    bomber_counter = 0
                await message_fight.channel.send('Со стороны мурлоков огромные потери!')
            if 51 < r_fight <= 60:      # Благоприятный исход для мурлоков
                murloc_army -= 200
                if murloc_army < 0:
                    murloc_army = 0
                sniper_counter -= 1
                if sniper_counter < 0:
                    sniper_counter = 0
                flamethrower_counter -= 1
                if flamethrower_counter < 0:
                    flamethrower_counter = 0
                bomber_counter -= 1
                if bomber_counter < 0:
                    bomber_counter = 0
                await message_fight.channel.send('Со стороны мурлоков маленькие потери!')
            if 61 < r_fight <= 100:      # Посредственный исход для мурлоков
                murloc_army -= 300
                if murloc_army < 0:
                    murloc_army = 0
                sniper_counter -= 1
                if sniper_counter < 0:
                    sniper_counter = 0
                flamethrower_counter -= 1
                if flamethrower_counter < 0:
                    flamethrower_counter = 0
                bomber_counter -= 2
                if bomber_counter < 0:
                    bomber_counter = 0
                await message_fight.channel.send('Со стороны мурлоков средние потери!')

            # ================================================
            if 0 < r_fight <= 50:       # Хороший исход для людей
                solder_army -= 25
                if solder_army < 0:
                    solder_army = 0
                stormtrooper_counter -= 0
                if stormtrooper_counter < 0:
                    stormtrooper_counter = 0
                gunner_counter -= 0
                if gunner_counter < 0:
                    gunner_counter = 0
                tank_counter -= 0
                if tank_counter < 0:
                    tank_counter = 0
                await message_fight.channel.send('Со стороны людей слабые потери!')
            if 51 < r_fight <= 90:  # Средний исход для людей
                solder_army -= 50
                if solder_army < 0:
                    solder_army = 0
                stormtrooper_counter -= 2
                if stormtrooper_counter < 0:
                    stormtrooper_counter = 0
                gunner_counter -= 1
                if gunner_counter < 0:
                    gunner_counter = 0
                tank_counter -= 0
                if tank_counter < 0:
                    tank_counter = 0
                await message_fight.channel.send('Со стороны людей средние потери!')
            if 91 < r_fight <= 100:  # Плохой исход для людей
                solder_army -= 100
                if solder_army < 0:
                    solder_army = 0
                stormtrooper_counter -= 5
                if stormtrooper_counter < 0:
                    stormtrooper_counter = 0
                gunner_counter -= 4
                if gunner_counter < 0:
                    gunner_counter = 0
                tank_counter -= 1
                if tank_counter < 0:
                    tank_counter = 0
                await message_fight.channel.send('Со стороны людей сильные потери!')
            await message_fight.channel.send('Результаты боя! \n')

            await message_fight.channel.send('======================= \n'
                                            'АРМИЯ МУРЛОКОВ: \n'
                                             'Мурлоки: {} \n'
                                            'Подрывники: {} \n'
                                            'Снайперы: {} \n'
                                            'Огнеметчики: {} \n'
                                            '======================= \n'.format(murloc_army, bomber_counter,
                                                                  sniper_counter, flamethrower_counter))
            await message_fight.channel.send('======================= \n'
                                             'АРМИЯ ЛЮДЕЙ: \n'
                                             'Солдаты: {} \n'
                                             'Штурмовики: {} \n'
                                             'Пулеметчики: {} \n'
                                             'Танки: {} \n'
                                             '======================= \n'.format(solder_army, stormtrooper_counter,
                                                                  gunner_counter, tank_counter))


keep_alive.keep_alive()
token = os.environ.get("Token")
bot.run(TOKEN)