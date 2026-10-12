class Buuz:
    def __init__(self, filling, count):
        self.filling = filling
        self.count = count
        self.cooked = False
    def show_status(self):
        if self.cooked:
            state = "bolson"
        else:
            state = "raw"
        print(f"Buuz with {self.filling} filling, count: {self.count}, state: {state}")
    def steam(self):
        self.cooked = True
        print(f"Buuz with {self.filling} filling is now cooked.")
    def sell(self, amount):
        if not self.count:
            print(f"Raw buuz zarj bolhku")
        elif amount > self.count:
            print(f"Not enough buuz to sell. Available: {self.count}, requested: {amount}.")
        else:
            self.count -= amount
            print(f"Sold {amount} buuz with {self.filling} filling. Remaining: {self.count}.")
print("========Buuznii gazar: udur 1=======.")
meat = Buuz("meat", 10)
meat.show_status()
print("--------zahialga 1: dorj, 3 buuz avah")
meat.sell(3)
meat.steam()
meat.sell(3)
print("--------zahialga 2: dorj, 20 buuz avah")
meat.sell(20)
print("--------Udriin tugsgul------------------")
meat.show_status()