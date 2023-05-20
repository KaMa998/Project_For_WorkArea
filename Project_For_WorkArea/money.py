import json

def malumot_qidirish():
    try:
        with open("login.py", "r") as fayl:
            malumotlar = json.load(fayl)
            if "llobin" in malumotlar and "pyni" in malumotlar["llobin"]:
                return malumotlar
            else:
                return None
    except FileNotFoundError:
        return None

qidirilgan_malumot = malumot_qidirish()

if qidirilgan_malumot is not None:
    print(qidirilgan_malumot)
else:
    print("Malumot topilmadi.")
