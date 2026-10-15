import json

class Vazifa:
    def __init__(self, matn, muhim=False):
        # 1) matn.strip() == "" bo'lsa → raise ValueError("Matn bo'sh bo'lmasin")
        # 2) self.matn = matn.strip()   self.muhim = muhim   self.bajarildi = False
        if matn.strip() == "":
            raise ValueError("Matn bo'sh bo'lmasin")
        self.matn = matn.strip()
        self.muhim = muhim
        self.bajarildi = False

        

    def bajar(self):
        if not self.bajarildi:
            self.bajarildi = True
            return True
        return False

    def __str__(self):
        status = "[x]" if self.bajarildi else "[ ]"
        return f"{status} {self.matn}{' ⭐' if self.muhim else ''}"