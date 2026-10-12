from abc import ABC, abstractmethod


# ================= Buuz6-аас ХЭВЭЭР хуулсан хэсэг =================
class Food(ABC):
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count
        self.cooked = False

    def describe(self):
        print("[Цэс]", self.name, "-", self.price, "төгрөг")

    def show_status(self):
        if self.cooked:
            state = "болсон"
        else:
            state = "түүхий"
        print("[Таваг]", self.name, "|", self.count, "ширхэг |", state)

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


class Buuz(Food):
    def __init__(self, filling, count=10):
        super().__init__(filling + " бууз", 1500, count)

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

    def cook(self):
        self.cooked = True
        print("[Жигнэх]", self.name, "жигнэгдлээ!")


class Khuushuur(Food):
    def __init__(self, filling, count=10):
        super().__init__(filling + " хуушуур", 2500, count)

    def cook(self):
        self.cooked = True
        print("[Шарах]", self.name, "шарагдлаа!")


class Bansh(Food):
    def __init__(self, filling, count=10):
        super().__init__(filling + " банш", 1000, count)

    def cook(self):
        self.cooked = True
        print("[Чанах]", self.name, "чанагдлаа!")


# ---- ШИНЭ: дөрөв дэх хоол ----
class Tsuivan(Food):
    def __init__(self, filling, count=10):
        super().__init__(filling + " цуйван", 3000, count)

    def cook(self):
        self.cooked = True
        print("[Хуурах]", self.name, "хуурагдлаа!")


class Customer:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

    def can_pay(self, amount):
        return amount <= self.budget

    def pay(self, amount):
        self.budget = self.budget - amount


class Order:
    def __init__(self, customer, food_name, amount):
        self.customer = customer
        self.food_name = food_name
        self.amount = amount


class Shop:
    def __init__(self, name, goal):
        self.name = name
        self.goal = goal
        self.income = 0
        self.menu = []

    def add_food(self, food):
        self.menu.append(food)

    # ---- ШИНЭ ----
    def show_menu(self):
        for food in self.menu:
            food.describe()

    # ---- ШИНЭ: ПОЛИМОРФИЗМ ----
    def cook_all(self):
        for food in self.menu:
            food.cook()

    def find(self, food_name):
        for food in self.menu:
            if food.name == food_name:
                return food
        return None

    def serve(self, order):
        print("--- Захиалга:", order.customer.name + ",", order.amount, order.food_name, "---")
        food = self.find(order.food_name)
        if food is None:
            print("[Алдаа] Цэсэнд байхгүй:", order.food_name)
            return
        cost = order.amount * food.price
        if not order.customer.can_pay(cost):
            print("[Алдаа]", order.customer.name, "- мөнгө хүрэхгүй! Хэрэгтэй:", cost, "| Байгаа:", order.customer.budget)
            return
        money = food.sell(order.amount)
        order.customer.pay(money)
        self.income = self.income + money

    def report(self):
        print("--- Өдрийн төгсгөл ---")
        print("[Орлого]", self.income, "төгрөг")
        if self.income >= self.goal:
            print("[Үр дүн] ЗОРИЛГО БИЕЛЭВ!")
        else:
            print("[Үр дүн] Зорилгод", self.goal - self.income, "төгрөг дутлаа.")


shop = Shop("Монгол бууз", 35000)
shop.add_food(Buuz("мах", 20))
shop.add_food(Khuushuur("мах", 8))
shop.add_food(Bansh("мах", 10))
shop.add_food(Tsuivan("мах", 6))

print("===== БУУЗНЫ ГАЗАР: ӨДӨР 6 =====")
print("[Газар]", shop.name, "| Зорилго:", shop.goal, "төгрөг")

print("--- Цэс ---")
shop.show_menu()
print("--- Бэлтгэх ---")
shop.cook_all()

dorj = Customer("Дорж", 10000)
bold = Customer("Болд", 20000)
saraa = Customer("Сараа", 9000)

orders = [
    Order(dorj, "мах бууз", 4),
    Order(bold, "мах цуйван", 4),
    Order(saraa, "мах хуушуур", 3),
    Order(bold, "мах хуушуур", 3),
    Order(dorj, "мах банш", 5),
    Order(saraa, "мах цуйван", 3),
]

for order in orders:
    shop.serve(order)
shop.report()