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


    def bajarilmagan(self):
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



