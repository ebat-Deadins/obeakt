class Buuz:
    def __init__(self, filling, count=10, cooked=False, sauces=None):
        self.filling = filling
        self.count = count          
        self.cooked = cooked
        if sauces is None:
            self.sauces = []
        else:
            self.sauces = sauces

    # ---- ШИНЭ: хамгаалагдсан count ----
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

    # ---- ШИНЭ: зөвхөн унших шинж чанар ----
    @property
    def is_empty(self):
        return self._count == 0

    def show_status(self):
        if self.cooked:
            state = "болсон"
        else:
            state = "түүхий"
        print("[Таваг]", self.filling, "бууз |", self.count, "ширхэг |", state)

    def steam(self):
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
            print("[Зарлаа]", amount, self.filling, "бууз | +" + str(money), "төгрөг")
            return money

    # ---- ШИНЭ: нөөц нэмэх ----
    def add(self, amount=1):
        self.count = self.count + amount
        return self.count

    def add_sauce(self, sauce):
        self.sauces.append(sauce)


print("===== БУУЗНЫ ГАЗАР: ӨДӨР 2 =====")
income = 0
meat = Buuz("мах", count=100)
print("[Тогоо] 100 бууз хийхийг оролдлоо")
meat.show_status()
meat.steam()

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

print("--- Өдрийн төгсгөл ---")
print("[Орлого]", income, "төгрөг")