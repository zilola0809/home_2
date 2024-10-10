def salom_ber(ism):
    """Foydalanuvchui ismini qabul qilib, unga salon beruvchi funksiya!"""
    print(f"Assalomu aleykum hurmatli  {ism.title()}")
salom_ber('zilola')
salom_ber('guli')
print(salom_ber.__doc__)


def toliq_ism(ism, familiya):
     """Foydalanuvchui ismini qabul qilib, unga salon beruvchi funksiya!"""
     print(f"Foydalanuvchi ismi: {ism.title()}\n"
           f"Foydalanuvchi familiyasi: {familiya.title()}")

toliq_ism("Zilola", "Iskandaorva")

def yosh_hisobla(t_yil, j_yil=2024):
    """Foydalanuvchui ismini qabul qilib, unga salon beruvchi funksiya!"""
    print(f"Siz {j_yil-t_yil} yoshdasiz")
yosh_hisobla(2009)



def toliq_ism_yasa(ism, familiya):
    """Toliq ism qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism
# print(toliq_ism_yasa("Zilola", 'Iskandarova'))

talaba1 = toliq_ism_yasa('Zilola', 'iskandarova')
talaba2 = toliq_ism_yasa('shaydo', 'bekturdiyeva')
print(talaba1)
print(talaba2)
def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
    """Toliq isma qaytaruvchi funksiya"""
    if otasining_ismi:
        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
    else:
        toliq_ism = f"{ism} {familiya}"
    return toliq_ism.title()
talaba1 = toliq_ism_yasa('zilola','iskandarova')
talaba2 = toliq_ism_yasa('shaxnoza ','tuliyeva','abrorovich')
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")


              # Uyga vazifa
# 1
def tugilgan_yil_hisobla(h_yil=2024):
    ismi = input("Ismingizni kiriting: ")
    yosh = int(input("Yoshingizni kiriting: "))
    print(f"{ismi}, siz {h_yil-yosh}- yilda tug'ilgansiz")

tugilgan_yil_hisobla()

# 2
def sonni_hisobla():
    son = int(input("Sonni kiriting: "))

    kvadrat = son ** 2
    kub = son ** 3

    print(f"{son} ning kvadrati: {kvadrat}")
    print(f"{son} ning kubi: {kub}")

sonni_hisobla()

# 3
def j_yk_t():
    son = int(input("Sonni kiriting: "))

    if son % 2 == 0:
        print(f"{son} soni juft son.")
    else:
        print(f"{son} soni toq son.")

j_yk_t()


# 4
def katta():
    son1 = int(input("Birinchi sonni kiriting: "))
    son2 = int(input("Ikkinchi sonni kiriting: "))

    if son1 > son2:
        print(f"Katta son: {son1}")
    elif son1 < son2:
        print(f"Katta son: {son2}")
    else:
        print("Sonlar teng.")

katta()



