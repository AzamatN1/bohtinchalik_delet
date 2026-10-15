import json

from model import Vazifa


class Royxat:
    def __init__(self):
        self.vazifalar = []

    def __len__(self):
        return len(self.vazifalar)

    def qosh(self,matn, muhim = False):
        vazifa = Vazifa(matn, muhim)
        self.vazifalar.append(vazifa)

        return len(self.vazifalar) - 1


    def bajar(self, idx):
        v = self.vazifalar[idx]

        if v.bajarildi:
            return False

        v.bajar()
        return True


    def ochir(self, idx):
        del self.vazifalar[idx]


    def bajarilmaganlar(self):
        natija = []
        for i in self.vazifalar:
            if not i.bajarildi:
                natija.append(i)

        return natija

    def saqla(self, fayl = "vazifalar.json"):
        data = []
        for i in self.vazifalar:
            vazifa = {
                "matn" : i.matn,
                "muhim" : i.muhim,
                "bajarildi" : i.bajarildi
            }
            data.append(vazifa)

        with open(fayl,"w" ) as file:
            json.dump( data, file, indent=2)


    @classmethod
    def yukla(cls, fayl="vazifalar.json"):
        a = cls()

        try:
            with open(fayl, "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            return a


        for i in data:
            idx = a.qosh(i["matn"], i["muhim"])

            if i["bajarildi"]:
                a.bajar(idx)

        return a

def tanlovni_tekshir(matn, max_raqam):
    matn = matn.strip()

    if not matn.isdigit():
        return None
    n = int(matn)
    if 0 <= n <= max_raqam:
        return n

    return None

def ha_yoq(matn):
    matn = matn.strip().lower()
    return matn in ("h", "ha")



def menyu():
    print("""
=== 📝 VAZIFALAR ===
1. Ro'yxat
2. Qo'shish
3. Bajarildi deb belgilash
4. O'chirish
5. Bajarilmaganlar
0. Chiqish
""")


def main():

    r = Royxat.yukla()

    while True:
        menyu()
        tanlov = tanlovni_tekshir(input("Tanlang: "), 5)

        try:
            if tanlov is None:
                print(" 0 dan 5 gacha son kirit")

            elif tanlov == 1:
                if not r.vazifalar:
                    print("  (royxat bosh)")
                else:
                    for i, v in enumerate(r.vazifalar):
                        print(f"  #{i} {v}")

            elif tanlov == 2:
                matn = input("Vazifa: ")
                muhim = ha_yoq(input("Muhimmi? (h/y): "))
                idx = r.qosh(matn, muhim)
                print(f"✅ #{idx} qo'shildi: {r.vazifalar[idx]}")

            elif tanlov == 3:
                idx = int(input("Vazifa raqami: "))
                if r.bajar(idx):
                    print(f"✔️ #{idx} bajarildi")
                else:
                    print(" Allaqachon bajarilgan")

            elif tanlov == 4:
                idx = int(input("Vazifa raqami: "))
                r.ochir(idx)
                print(f"🗑 #{idx} ochirildi")

            elif tanlov == 5:
                qolgan = r.bajarilmaganlar()
                print(f"⏳ Bajarilmagan: {len(qolgan)} ta")
                for v in qolgan:
                    print(v)

            elif tanlov == 0:
                r.saqla()
                print("💾 Saqlandi. 👋 Xayr!")
                break

        except ValueError as e:
            print(
                " Son kiriting!"
                if "invalid literal" in str(e)
                else f" Xato: {e}"
            )
        except IndexError:
            print(" Bunday vazifa yo'q")


if __name__ == "__main__":
    main()