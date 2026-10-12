class Buuz:
    def __init__(self, filling, count):
        self.filling = filling
        self.count = count
        self.cooked = False

    def show_status(self):
        if self.cooked:
            state = "болсон"
        else:
            state = "түүхий"
        print("[Таваг]", self.filling, "бууз |", self.count, "ширхэг |", state)

    def steam(self):
        self.cooked = True
        print("[Жигнэх]", self.filling, "Buuz jignegdlee!")

    def sell(self, amount):
        if not self.cooked:
            print("[Алдаа] Түүхий бууз зарж болохгүй!")
        elif amount > self.count:
            print("[Алдаа] Ердөө", self.count, "бууз байна!")
        else:
            self.count = self.count - amount
            print("[Зарлаа]", amount, "бууз. Үлдсэн:", self.count)

print("===== БУУЗНЫ ГАЗАР: ӨДӨР 1 =====")
meat = Buuz("мах", 10)
meat.show_status()
print("--- Захиалга 1: Дорж, 3 бууз ---")
meat.sell(3)
meat.steam()
meat.sell(3)
print("--- Захиалга 2: Болд, 20 бууз ---")
meat.sell(20)
print("--- Өдрийн төгсгөл ---")
meat.show_status()
