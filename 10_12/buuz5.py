from abc import ABC, abstractmethod


class Food(ABC):
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count
        self.cooked = False

    def describe(self):
        print(f"[Цэс] {self.name} - {self.price} төгрөг")

    def show_status(self):
        state = "болсон" if self.cooked else "түүхий"
        print(f"[Таваг] {self.name} | {self.count} ширхэг | {state}")

    def sell(self, amount=1):
        if not self.cooked:
            print(f"[Алдаа] {self.name} - түүхий байна!")
            return 0
        if amount > self.count:
            print(f"[Алдаа] Ердөө {self.count} {self.name} байна!")
            return 0
        self.count -= amount
        money = amount * self.price
        print(f"[Зарлаа] {amount} {self.name} | +{money} төгрөг")
        return money

    @abstractmethod
    def cook(self):
        pass


class Buuz(Food):
    def __init__(self, filling, count=10):
        super().__init__(filling + " бууз", 1500, count)

    # Лаб 3: count-ийн 0–30 хязгаар (зөвхөн Buuz-д)
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        if value < 0:
            value = 0
        elif value > 30:
            value = 30
        self._count = value

    def cook(self):
        self.cooked = True
        print(f"[Жигнэх] {self.name} жигнэгдлээ!")


class Khuushuur(Food):
    def __init__(self, filling, count=10):
        super().__init__(filling + " хуушуур", 2500, count)

    def cook(self):
        self.cooked = True
        print(f"[Шарах] {self.name} шарагдлаа!")


class Bansh(Food):
    def __init__(self, filling, count=10):
        super().__init__(filling + " банш", 1000, count)

    def cook(self):
        self.cooked = True
        print(f"[Чанах] {self.name} чанагдлаа!")


# ---------------- Үндсэн програм ----------------
goal = 25000
income = 0
print("===== БУУЗНЫ ГАЗАР: ӨДӨР 4 =====")
print(f"[Зорилго] {goal} төгрөг")

buuz = Buuz("мах", count=100)
khuushuur = Khuushuur("мах", 8)
bansh = Bansh("мах", 6)

print("--- Цэс ---")
buuz.describe()
khuushuur.describe()
bansh.describe()

print("--- Таваг ---")
buuz.show_status()
khuushuur.show_status()
bansh.show_status()

print("--- Бэлтгэх ---")
buuz.cook()
khuushuur.cook()
bansh.cook()

print("--- Захиалга 1: Дорж, 10 мах бууз ---")
income += buuz.sell(10)
print("--- Захиалга 2: Болд, 4 мах хуушуур ---")
income += khuushuur.sell(4)
print("--- Захиалга 3: Сараа, 7 мах банш ---")
income += bansh.sell(7)
print("--- Захиалга 4: Сараа, 2 мах банш ---")
income += bansh.sell(2)

print("--- Өдрийн төгсгөл ---")
print(f"[Орлого] {income} төгрөг")
if income >= goal:
    print("[Үр дүн] ЗОРИЛГО БИЕЛЭВ!")
else:
    print(f"[Үр дүн] Зорилгод {goal - income} төгрөг дутлаа.")