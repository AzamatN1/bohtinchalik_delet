# 📝 Vazifalar ro'yxati

## 👥 Jamoa
| Rol | Ism | GitHub |
|---|---|---|
| 🧑‍✈️ Kapitan | Azamat | @AzamatN1 |
| 🧠 Mantiqchi | Ilhomjon | @... |
| 🖥 Interfeyschi | Ibrohim | @... |

## 🔌 Shartnoma
# model.py  (🧑‍✈️ Kapitan)
class Vazifa(matn, muhim=False)
    bo'sh matn ("" yoki faqat probel) → ValueError("Matn bo'sh bo'lmasin")
    self.matn (strip qilingan), self.muhim, self.bajarildi = False
    bajar()                      # bajarildi = True
    __str__  →  "[ ] Dars qilish"   yoki   "[x] Non olish ⭐"   (muhim bo'lsa ⭐)

# xizmat.py  (🧠 Mantiqchi)
class Royxat()
    self.vazifalar = []          # Vazifa obyektlari
    __len__                      # len(r)
    qosh(matn, muhim=False) → int        # yangi vazifa raqami (0, 1, 2...)
    bajar(idx) → bool            # allaqachon bajarilgan bo'lsa False; yo'q idx → IndexError
    ochir(idx)
    bajarilmaganlar() → list
    saqla(fayl="vazifalar.json")
    @classmethod yukla(fayl="vazifalar.json")   # fayl yo'q → bo'sh Royxat

# main.py  (🖥 Interfeyschi) — toza funksiyalar
tanlovni_tekshir(matn, max) → int | None    # "3",5 → 3;  "abc" → None;  "9",5 → None
ha_yoq(matn) → bool                         # "h" / "Ha" → True, qolgani → False


## 🚀 Ishga tushirish
git clone https://github.com/AzamatN1/to_do_list-python
cd vazifalar
python main.py

## 🧪 Testlar
python -m unittest -v