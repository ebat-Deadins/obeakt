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
        print("--- Zahialga: " + order.customer.name + ", "
              + str(order.amount) + " " + order.food_name + " ---")

        food = self.find(order.food_name)
        if food is None:
            print("[Aldaa] Tsesend baihgui: " + order.food_name)
            return

        cost = order.amount * food.price
        if not order.customer.can_pay(cost):
            print("[Aldaa] " + order.customer.name + " - mungu hurehgui: "
                  + str(cost) + " | baigaa: " + str(order.customer.budget))
            return

        money = food.sell(order.amount)
        order.customer.pay(money)
        self.income += money

    def report(self):
        print("--- udriin tussgul ---")
        print("[Орлого] " + str(self.income) + " tugrug")
        if self.income >= self.goal:
            print("[Ur dun] Zorilgo biylsen!")
        else:
            print("[Ur dun] " + str(self.goal - self.income) + " tugrug dutlaa.")


shop = Shop("Mongol buuz", 20000)
shop.add_food(Buuz("mah", 20))
shop.add_food(Khuushuur("mah", 8))
shop.add_food(Bansh("mah", 10))

print("===== Buuznii gazar: 5 dahi udur =====")
print("[Gazar]", shop.name, "| Zorilgo:", shop.goal, "tugrug")
for food in shop.menu:
    food.show_status()

print("--- Beltgeh ---")
shop.menu[0].cook()
shop.menu[1].cook()
shop.menu[2].cook()

dorj = Customer("Dorj", 6000)
bold = Customer("Bold", 20000)
saraa = Customer("Saraa", 3000)
tugsuu = Customer("Tuguldur", 5000)

orders = [
    Order(dorj, "mahan buuz", 3),
    Order(bold, "mahan khuushuur", 4),
    Order(saraa, "mahan buuz", 5),
    Order(tugsuu, "pizza", 1),
    Order(bold, "mahan bansh", 6),
]

for order in orders:
    shop.serve(order)

shop.report()