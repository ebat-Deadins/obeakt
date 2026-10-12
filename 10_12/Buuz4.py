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

    def __init__(self, filling, count=10, taste=Taste.SALTY):
        self.filling = filling
        self.count = count
        self.cooked = False
        self.taste = taste
        Buuz.total += 1 

    def show_status(self):
        if self.cooked:
            state = "болсон"
        else:
            state = "түүхий"
        print("[Таваг]", self.filling, "бууз |", self.count, "ширхэг |", state, "|", self.taste.value)

    def cook(self):
        self.cooked = True
        print("[Жигнэх]", self.filling, "бууз жигнэгдлээ!")

    def sell(self, amount):
        if not self.cooked:
            print("[Алдаа] Түүхий бууз зарж болохгүй!")
        elif amount > self.count:
            print("[Алдаа] Ердөө", self.count, "бууз байна!")
        else:
            self.count = self.count - amount
            total_price = amount * 1500  
            print(f"[Зарлаа] {amount} {self.filling} бууз | +{total_price} төгрөг")
            return total_price

    @staticmethod
    def is_valid_filling(name):
        return len(name) >= 2

    @classmethod
    def get_total(cls):
        return cls.total

    @classmethod
    def create_meat(cls, count=10):
        return cls("мах", count, Taste.SALTY)


print("===== БУУЗНЫ ГАЗАР: ӨДӨР 3 =====")

print("--- Дүүргэлт шалгах ---")
fillings = ["мах", "м", "бяслаг"]
for f in fillings:
    if Buuz.is_valid_filling(f):
        print(f"[Шалгалт] {f} - зөв")
    else:
        print(f"[Шалгалт] {f} - хэт богино, бууз хийхгүй")

print("--- Бууз хийх ---")
meat = Buuz.create_meat()  # Defolt 10 mah buuz
spicy = Buuz("хүнсний ногоо", 5, Taste.SPICY)
meat.show_status()
spicy.show_status()
print("[Нийт] Өнөөдөр хийсэн бууз:", Buuz.get_total())

print("--- Захиалга: Дорж, халуун амттай 2 бууз ---")
income = 0
spicy.cook()
revenue = spicy.sell(2)
income += revenue
if spicy.taste == Taste.SPICY:
    income += 500
    print("[Амт] Халуун амт таарлаа! +500 төгрөг")
print(f"[Орлого] {income} төгрөг")

print("--- Загвар шалгах ---")
try:
    f_obj = Food()
except TypeError:
    print("[Алдаа] Food-оос шууд хоол хийж болохгүй")
