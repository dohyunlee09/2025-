print("게임에 오신 것을 환영합니다!")
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
        choice = input("숫자를 입력하세요 (1. 무기 강화 / 0. 종료하기): ")


        if choice == "0":
            print("게임을 종료합니다.")
            break
        elif choice == "1":
            import random
            ran_num = random.randint(0, 99)
            rate = upgrade_rates[weapon_level]

            print(weapon_level)
            print(ran_num)
            print(rate)
            if ran_num<rate['up']:
                    print('레벨업')
                    weapon_level+=1
            elif ran_num<rate['up']+rate['keep']:
                    print("유지")
            elif ran_num<rate['up']+rate['keep']+rate['down']:
                    print("하락")
                    weapon_level -= 1
            elif ran_num<rate['up']+rate['keep']+rate['down']+rate['break']:
                    print("qudtls")
                    weapon_level = 0








