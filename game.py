from operator import truediv

print("게임에 오신 것을 환영합니다!")
is_dragon_slayer = False
def 강화(weapon_level,upgrade_rates):
    import random
    ran_num = random.randint(0, 99)
    rate = upgrade_rates[weapon_level]
    print(weapon_level)
    if ran_num < rate['up']:
        print('레벨업')
        weapon_level += 1
    elif ran_num < rate['up'] + rate['keep']:
        print("유지")
    elif ran_num < rate['up'] + rate['keep'] + rate['down']:
        print('하락')
        weapon_level -= 1
    elif ran_num < rate['up'] + rate['keep'] + rate['down'] + rate['break']:
        print("qudtls")
        weapon_level = 0
    return weapon_level
upgrade_rates =[
    {"up": 70, "keep": 30, "down": 0,  "break": 0},   # Index 0: 레벨 0
    {"up": 60, "keep": 25, "down": 10, "break": 5},   # Index 1: 레벨 1
    {"up": 50, "keep": 30, "down": 15, "break": 5},   # Index 2: 레벨 2
    {"up": 45, "keep": 30, "down": 20, "break": 5},   # Index 3: 레벨 3
    {"up": 40, "keep": 30, "down": 20, "break": 10},  # Index 4: 레벨 4
    {"up": 35, "keep": 30, "down": 25, "break": 10},  # Index 5: 레벨 5
    {"up": 30, "keep": 30, "down": 30, "break": 10},  # Index 6: 레벨 6
    {"up": 25, "keep": 30, "down": 30, "break": 15},  # Index 7: 레벨 7
    {"up": 20, "keep": 30, "down": 30, "break": 20},  # Index 8: 레벨 8
    {"up": 15, "keep": 30, "down": 30, "break": 25},  # Index 9: 레벨 9
    {"up": 0,  "keep": 100, "down": 0, "break": 0}]    # Index 10: 레벨 10 }
weapon_level = 0
while True:
    if is_dragon_slayer == True:
        print("조준상급")

        choice = input("숫자를 입력하세요 (2.보스 도전 / 1. 무기 강화 / 0. 종료하기): ")


        if choice == "0":
            print("게임을 종료합니다.")
            break
        elif choice == "1":
            weapon_level = 강화(weapon_level, upgrade_rates)


        elif choice == "2":
            print("보스 도전")

            print(weapon_level)




        def upgrade_weapon(current_lv):
                if current_lv == 10:
                    print("더 이상 업그레이드가 불가합니다.")
                    return current_lv

boss_level = 0
boss_names=["보스 1","보스 2","보스 3","보스 4","보스 5","보스 6","보스 7","보스 8","보스 9","보스 10"]


def start_battle(weapon_level,boss_level):
    level_diff = (weapon_level - boss_level)

    if level_diff <= -3:
        win_rate = 0
    elif level_diff == -2:
        win_rate = 20
    elif level_diff == -1:
        win_rate = 30
    elif level_diff == 0:
        win_rate = 50
    elif level_diff == 1:
        win_rate = 70
    elif level_diff == 2:
        win_rate = 90
    elif level_diff >= 3:
        win_rate = 100

    dice = random.randint(0, 99)

    print(f"주사위 값: {dice}")
    print(f"승리 확률: {win_rate}%")

    if dice > win_rate:
        print("축하합니다! 모든 보스를 제압했습니다!" )
        is_dragon_slayer = True




