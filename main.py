import time

class main():

    def __init__(self, rates, bands):
        self.rates = rates
        self.bands = bands

    def determineBands(self):
        for i in range(len(self.bands)):
            if i==(len(self.bands)-1) or self.salary >= self.bands[i] and self.salary < self.bands[i+1]:
                return i
        return "X"

    def recurseTax(self, bandIndex):
        levy = 0
        for x in range(bandIndex+1):
            if not x == bandIndex:
                levy += (self.bands[x+1] - self.bands[x]) * self.rates[x]
            elif x == bandIndex:
                levy += (self.salary - self.bands[x]) * self.rates[x]
        return levy
                
    def run(self):
        salaryBox = Element("salary-box")
        self.salary = float(salaryBox.element.value)
        bandIndex = self.determineBands()
        if type(bandIndex) == str:
            print("no tax levied")
            #self.run()
        totalTax = self.recurseTax(bandIndex)
        print(f"Band Index: {bandIndex} \nTax levied: {totalTax}")
        #self.run()

def parseRatesAndBands():
    rates = Element("rates-box").value.split(",")
    for i in rates:
        rates[rates.index(i)] = float(i.strip())
    bands = Element("bands-box").value.split(",")
    for j in bands:
        bands[bands.index(j)] = float(j.strip())
    global main
    main = main(rates, bands)
