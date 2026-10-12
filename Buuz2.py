class Buuz:
    def __init__(self, filling, count=10, cooked=False, sauces=None):
        self.filling = filling
        self.count = count
        self.cooked = cooked
        if sauces is None:
            self.sauces = []
        else:
            self.sauces = sauces

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

    def add_sauce(self, sauce):
        self.sauces.append(sauce)


goal = 14000
income = 0
print("===== БУУЗНЫ ГАЗАР: ӨДӨР 1 =====")
print("[Зорилго]", goal, "төгрөг")

meat = Buuz("мах")
veg = Buuz("хүнсний ногоо", count=5, cooked=True)
meat.show_status()
veg.show_status()
meat.steam()

print("--- Захиалга 1: Дорж, 3 мах бууз ---")
income = income + meat.sell(3)

print("--- Захиалга 2: Болд, 4 мах бууз (нэг нь 1800 төгрөг) ---")
income = income + meat.sell(4, price=1800)

print("--- Захиалга 3: Сараа, 6 мах бууз ---")
income = income + meat.sell(6)

print("--- Захиалга 4: Тэмүүлэн, 2 хүнсний ногоотой бууз ---")
income = income + veg.sell(amount=2)

print("--- Соус ---")
meat.add_sauce("сармис")
print("[Соус] мах бууз:", meat.sauces)
print("[Соус] хүнсний ногоотой бууз:", veg.sauces)

print("--- Өдрийн төгсгөл ---")
print("[Орлого]", income, "төгрөг")
if income >= goal:
    print("[Үр дүн] ЗОРИЛГО БИЕЛЭВ!")
else:
    print("[Үр дүн] Зорилгод", goal - income, "төгрөг дутлаа.")