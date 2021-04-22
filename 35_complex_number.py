class Complex:
    def __init__(self):
        real1 = int(input("Enter real1: "))
        imaginary1 = int(input("Enter Imaginary1: "))
        real2 = int(input("Enter real2: "))
        imaginary2 = int(input("Enter Imaginary2: "))
        a = complex(real1, imaginary1)
        b = complex(real2, imaginary2)
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def show_sum(self):
        print(f"Sum: {self.sum()}")

    def mul(self):
        return self.a * self.b

    def show_mul(self):
        print(f"Multiplication: {self.mul()}")

    def sub(self):
        return self.a - self.b

    def show_sub(self):
        print(f"Submission: {self.sub()}")

    def div(self):
        return self.a / self.b

    def show_div(self):
        print(f"Divide: {self.div()}")


res = Complex()

res.show_sum()

res.show_mul()

res.show_sub()

res.show_div()
