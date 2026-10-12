from abc import ABC, abstractmethod


# ---- ШИНЭ: интерфейс — "зарагдах чадвартай" гэсэн ГЭРЭЭ ----
class Sellable(ABC):
    @abstractmethod
    def describe(self):
        pass

    @abstractmethod
    def sell(self, amount=1):
        pass


# ---- Food одоо Sellable-ийг дагана ----
class Food(Sellable):
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count
        self.cooked = False

    def describe(self):
        print("[Цэс]", self.name, "-", self.price, "төгрөг")

    def sell(self, amount=1):
        if not self.cooked:
            print("[Алдаа]", self.name, "- түүхий байна!")
            return 0
        elif amount > self.count:
            print("[Алдаа] Ердөө", self.count, self.name, "байна!")
            return 0
        else:
            self.count = self.count - amount
            money = amount * self.price
            print("[Зарлаа]", amount, self.name, "| +" + str(money), "төгрөг")
            return money

    @abstractmethod
    def cook(self):
        pass


# ---- Buuz: count-ийн 0–30 хязгаар ЭНЭ ЛАБД БАЙХГҮЙ ----
class Buuz(Food):
    def __init__(self, filling, count=10):
        super().__init__(filling + " бууз", 1500, count)

    def cook(self):
        self.cooked = True
        print("[Жигнэх]", self.name, "жигнэгдлээ!")


class Khuushuur(Food):
    def __init__(self, filling, count=10):
        super().__init__(filling + " хуушуур", 2500, count)

    def cook(self):
        self.cooked = True
        print("[Шарах]", self.name, "шарагдлаа!")


# ---- ШИНЭ: цай. Food БИШ, Sellable-ийг шууд дагана ----
class Drink(Sellable):
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def describe(self):
        print("[Цэс]", self.name, "-", self.price, "төгрөг (бэлэн)")

    def sell(self, amount=1):
        if amount > self.count:
            print("[Алдаа] Ердөө", self.count, self.name, "байна!")
            return 0
        else:
            self.count = self.count - amount
            money = amount * self.price
            print("[Зарлаа]", amount, self.name, "| +" + str(money), "төгрөг")
            return money


class Customer:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

    def can_pay(self, amount):
        return amount <= self.budget

    def pay(self, amount):
        self.budget = self.budget - amount


# ---- ӨӨРЧЛӨГДСӨН: food_name -> item_name ----
class Order:
    def __init__(self, customer, item_name, amount):
        self.customer = customer
        self.item_name = item_name
        self.amount = amount


class Shop:
    def __init__(self, name):           # зорилго одоо энд байхгүй
        self.name = name
        self.income = 0
        self.menu = []

    def add_item(self, item):           # add_food -> add_item
        self.menu.append(item)

    def show_menu(self):
        for item in self.menu:
            item.describe()

    def cook_all(self):
        for item in self.menu:
            if isinstance(item, Food):  # зөвхөн Food-ийг жигнэнэ, цайг үгүй
                item.cook()

    def find(self, item_name):
        for item in self.menu:
            if item.name == item_name:
                return item
        return None

    def serve(self, order):
        print("--- Захиалга:", order.customer.name + ",", order.amount, order.item_name, "---")
        item = self.find(order.item_name)
        if item is None:
            print("[Алдаа] Цэсэнд байхгүй:", order.item_name)
            return
        cost = order.amount * item.price
        if not order.customer.can_pay(cost):
            print("[Алдаа]", order.customer.name, "- мөнгө хүрэхгүй! Хэрэгтэй:", cost, "| Байгаа:", order.customer.budget)
            return
        money = item.sell(order.amount)
        order.customer.pay(money)
        self.income = self.income + money

    # ---- ШИНЭ: нэг өдрийг бүхэлд нь явуулна, хожсон эсэхийг буцаана ----
    def run_day(self, day, goal, orders):
        self.income = 0
        print("===== ӨДӨР", day, "| Зорилго:", goal, "төгрөг =====")
        for order in orders:
            self.serve(order)
        print("--- Өдрийн төгсгөл ---")
        print("[Орлого]", self.income, "төгрөг")
        if self.income >= goal:
            print("[Үр дүн] Өдөр", day, "- ЗОРИЛГО БИЕЛЭВ!")
            return True
        else:
            print("[Үр дүн] Өдөр", day, "- зорилгод", goal - self.income, "төгрөг дутлаа.")
            return False


shop = Shop("Монгол бууз")
shop.add_item(Buuz("мах", 20))
shop.add_item(Khuushuur("мах", 8))
shop.add_item(Drink("сүүтэй цай", 800, 10))

print("===== БУУЗНЫ ГАЗАР: ТОГЛООМ ЭХЭЛЛЭЭ =====")
print("--- Цэс ---")
shop.show_menu()
print("--- Бэлтгэх ---")
shop.cook_all()

dorj = Customer("Дорж", 20000)
bold = Customer("Болд", 12000)
saraa = Customer("Сараа", 9000)

day1 = [
    Order(dorj, "мах бууз", 6),
    Order(bold, "мах хуушуур", 3),
    Order(saraa, "сүүтэй цай", 4),
]
day2 = [
    Order(dorj, "мах хуушуур", 4),
    Order(bold, "мах бууз", 3),
    Order(saraa, "мах хуушуур", 1),
    Order(dorj, "сүүтэй цай", 12),
]

wins = 0
if shop.run_day(1, 18000, day1):
    wins = wins + 1
if shop.run_day(2, 16000, day2):
    wins = wins + 1

print("===== ТОГЛООМЫН ДҮН =====")
print("[Хожсон өдөр]", wins, "/ 2")
if wins == 2:
    print("[Үр дүн] ШИЛДЭГ ЭЗЭН!")
elif wins == 1:
    print("[Үр дүн] Муугүй байлаа.")
else:
    print("[Үр дүн] Дахин оролдоорой.")