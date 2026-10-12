from abc import ABC, abstractmethod


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
            total_price = amount * self.price
            print(f"[Зарлаа] {amount} {self.name} | +{total_price} төгрөг")
            return total_price

    @abstractmethod
    def cook(self):
        pass


class Buuz(Food):
    def __init__(self, filling, count=10):
        super().__init__(filling + " бууз", 1500, count)

    # Лаб 3: count 0–30 хооронд (зөвхөн Buuz-д)
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


# ===== Лаб 6: шинэ классууд =====

class Customer:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

    def can_pay(self, amount):
        return amount <= self.budget

    def pay(self, amount):
        self.budget -= amount


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

    def find(self, food_name):
        for food in self.menu:
            if food.name == food_name:
                return food
        return None

    def serve(self, order):
        print(f"--- Захиалга: {order.customer.name}, {order.amount} {order.food_name} ---")

        food = self.find(order.food_name)
        if food is None:
            print(f"[Алдаа] Цэсэнд байхгүй: {order.food_name}")
            return

        cost = order.amount * food.price
        if not order.customer.can_pay(cost):
            print(f"[Алдаа] {order.customer.name} - мөнгө хүрэхгүй! "
                  f"Хэрэгтэй: {cost} | Байгаа: {order.customer.budget}")
            return

        money = food.sell(order.amount)
        order.customer.pay(money)
        self.income += money

    def report(self):
        print("--- Өдрийн төгсгөл ---")
        print(f"[Орлого] {self.income} төгрөг")
        if self.income >= self.goal:
            print("[Үр дүн] ЗОРИЛГО БИЕЛЭВ!")
        else:
            print(f"[Үр дүн] Зорилгод {self.goal - self.income} төгрөг дутлаа.")


# ===== Үндсэн програм =====

shop = Shop("Монгол бууз", 20000)
shop.add_food(Buuz("мах", 20))
shop.add_food(Khuushuur("мах", 8))
shop.add_food(Bansh("мах", 10))

print("===== БУУЗНЫ ГАЗАР: ӨДӨР 5 =====")
print("[Газар]", shop.name, "| Зорилго:", shop.goal, "төгрөг")
for food in shop.menu:
    food.show_status()

print("--- Бэлтгэх ---")
shop.menu[0].cook()
shop.menu[1].cook()
shop.menu[2].cook()

dorj = Customer("Дорж", 6000)
bold = Customer("Болд", 20000)
saraa = Customer("Сараа", 3000)
tugsuu = Customer("Төгөлдөр", 5000)

orders = [
    Order(dorj, "мах бууз", 3),
    Order(bold, "мах хуушуур", 4),
    Order(saraa, "мах бууз", 5),
    Order(tugsuu, "пицца", 1),
    Order(bold, "мах банш", 6),
]

for order in orders:
    shop.serve(order)

shop.report()