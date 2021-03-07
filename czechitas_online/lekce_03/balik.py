class Package:
    def __init__(self, address, weight_in_kilos):
        self.address = address
        self.weight_in_kilos = weight_in_kilos
        self.delivered = False

    def get_info(self):
        return f"Balík doručován na adresu {self.address} o váze {self.weight_in_kilos} byl doručen: {self.delivered}."

    def deliver(self):
        self.delivered = True
        #print(f"Doručuji balík na adresu {self.address}.")

package1 = Package("Mozartova 10", 0.44)
package2 = Package("Bachova 12", 0.33)

package1.deliver()

print(package1.get_info())
print(package2.get_info())