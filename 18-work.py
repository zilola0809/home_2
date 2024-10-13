# # 1
def foydalanuvchi_malumotlari(ism, familiya, tugilgan_yil, tugilgan_joy):
    hozir = 2024
    yosh = hozir- tugilgan_yil

    foydalanuvchi = {
        'ism': ism,
        'familiya': familiya,
        'tugilgan_yil': tugilgan_yil,
        'tugilgan_joy': tugilgan_joy,
        'yosh': yosh,
    }
    return foydalanuvchi

user_info = foydalanuvchi_malumotlari('Zilola', 'Iskandarova', 2009, 'Xorazm')
print(user_info)

# 2

def foydalanuvchi_malumotlari(ism, familiya, tugilgan_yil, tugilgan_joy):
    hozir = 2024
    yosh = hozir- tugilgan_yil

    foydalanuvchi = {
        'ism': ism,
        'familiya': familiya,
        'tugilgan_yil': tugilgan_yil,
        'tugilgan_joy': tugilgan_joy,
        'yosh': yosh,
    }
    return foydalanuvchi
mijozlar = []

while True:
    ism = input("Ismingizni kiriting (to'xtatish uchun 'exit' yozing): ")
    if ism.lower() == 'exit':
        break
    familiya = input("Familiyangizni kiriting: ")
    tugilgan_yil = int(input("Tug'ilgan yilingizni kiriting: "))
    tugilgan_joy = input("Tug'ilgan joyingizni kiriting: ")

    mijoz = foydalanuvchi_malumotlari(ism, familiya, tugilgan_yil, tugilgan_joy)
    mijozlar.append(mijoz)

print("\nMijozlar ro'yxati:")
for mijoz in mijozlar:
    print(mijoz)

# 3
def eng_katta_son(a, b, c):
    return max(a, b, c)

son = eng_katta_son(5, 12, 7)
print("Eng katta son:", son)

# 4
import math

def aylana_hisobla(radius):

    diametr = 2 * radius
    perimetr = 2 * math.pi * radius
    yuzi = math.pi * radius ** 2

    natija = {
        'radius': radius,
        'diametr': diametr,
        'perimetr': perimetr,
        'yuzi': yuzi
    }

    return natija


radius = float(input("Aylaning radiusini kiriting: "))

result = aylana_hisobla(radius)
print(result)

