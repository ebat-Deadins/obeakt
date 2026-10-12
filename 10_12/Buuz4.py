from enum import Enum
from abc import ABC, abstractmethod

class Taste(Enum):
    SALTY = "давстай"
    SWEET = "амтат"
    SPICY = "халуун"

class Food(ABC):
    @abstractmethod
    def cook(self):
        pass

class Buuz(Food):
    total = 0  

    def __init__(self, filling, count=10, cooked=False, sauces=None, taste=Taste.SALTY):
        self.filling = filling
        self.count = count          
        self.cooked = cooked
        self.taste = taste
        if sauces is None:
            self.sauces = []
        else:
            self.sauces = sauces
        Buuz.total += 1

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        if value < 0:
            self._count = 0
        elif value > 30:
            self._count = 30
        else:
            self._count = value

    @property
    def is_empty(self):
        return self._count == 0

    def show_status(self):
        if self.cooked:
            state = "болсон"
        else:
            state = "түүхий"
        print("[Таваг]", self.filling, "бууз |", self.count, "ширхэг |", state, "|", self.taste.value)

    def cook(self):
        self.cooked = True
        print("[Жигнэх]", self.filling, "бууз жигнэгдлээ!")

    def sell(self, amount=1, price=1500):
        if not self.cooked:
            print("[Алдаа] Түүхий бууз зарж болохгүй!")
            return 0
        elif amount > self.count:
            print("[Алдаа] Ердөө", self.count, "бууз байна!")
            return 0
        else:
            self.count = self.count - amount
            money = amount * price
            print(f"[Зарлаа] {amount} {self.filling} бууз | +{money} төгрөг")
            return money

    def add(self, amount=1):
        self.count = self.count + amount
        return self.count

    def add_sauce(self, sauce):
        self.sauces.append(sauce)

    @staticmethod
    def is_valid_filling(name):
        return len(name) >= 2

    @classmethod
    def get_total(cls):
        return cls.total

    @classmethod
    def create_meat(cls, count=10, taste=Taste.SALTY):
        return cls("мах", count, False, None, taste)


print("===== БУУЗНЫ ГАЗАР: ӨДӨР 4 =====")
income = 0

print("--- Дүүргэлт шалгах ---")
fillings = ["мах", "м", "бяслаг"]
for f in fillings:
    if Buuz.is_valid_filling(f):
        print(f"[Шалгалт] {f} - зөв")
    else:
        print(f"[Шалгалт] {f} - хэт богино, бууз хийхгүй")

print("--- Бууз хийх ---")
meat = Buuz.create_meat(count=100)
print("[Тогоо] 100 бууз хийхийг оролдлоо")
meat.show_status()
meat.cook()

print("--- Захиалга 1: Дорж, 12 бууз ---")
income = income + meat.sell(12)
print("--- Захиалга 2: Болд, 18 бууз ---")
income = income + meat.sell(18)
print("[Тогоо] Хоосон эсэх:", meat.is_empty)

print("--- Нөөц нэмэх ---")
print("[Нөөц] 40 бууз нэмэхийг оролдлоо. Тогоонд:", meat.add(40))

try:
    meat.is_empty = False
except AttributeError:
    print("[Алдаа] is_empty зөвхөн унших боломжтой")

print("--- Тогоо эвдэрлээ ---")
meat.count = -5
meat.show_status()
print("[Тогоо] Хоосон эсэх:", meat.is_empty)

print("[Нийт] Өнөөдөр хийсэн бууз:", Buuz.get_total())

print("--- Загвар шалгах ---")
try:
    f_obj = Food()
except TypeError:
    print("[Алдаа] Food-оос шууд хоол хийж болохгүй")

print("--- Өдрийн төгсгөл ---")
print("[Орлого]", income, "төгрөг")
