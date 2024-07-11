class main():

    def __init__(self, rates, bands):
        self.rates = rates
        self.bands = bands

    def determineBands(self):
        for i in range(len(self.bands)):
            if i == (len(self.bands) - 1) or self.salary >= self.bands[i] and self.salary < self.bands[i + 1]:
                return i
        return "X"

    def recurseTax(self, bandIndex):
        levy = 0
        for x in range(bandIndex + 1):
            if not x == bandIndex:
                levy += (self.bands[x + 1] - self.bands[x]) * self.rates[x]
            elif x == bandIndex:
                levy += (self.salary - (self.bands[x] - 1)) * self.rates[x]
        return levy

    def run(self):
        salaryBox = Element("ivtm8")
        self.salary = float(salaryBox.element.value)
        bandIndex = self.determineBands()
        if type(bandIndex) == str:
            print("no tax levied")
        totalTax = self.recurseTax(bandIndex)
        taxBox = Element("tax-value")
        taxBox.element.innerText = "£" + str(round(totalTax,2))
        # print(f"Band Index: {bandIndex} \nTax levied: {totalTax}")


def parseRatesAndBands():
    rates = []
    bands = []
    try:
        rates = Element("ie9a9").value.split(",")
        for i in rates:
            rates[rates.index(i)] = float(i.strip())
        bands = Element("i2t08").value.split(",")
        for j in bands:
            bands[bands.index(j)] = float(j.strip())
        global instance
        instance = main(rates, bands)
    except:
        taxBox = Element("tax-value")
        taxBox.element.innerText = "err << parse rates and bands failed at parse time"


def start():
    try:
        parseRatesAndBands()
        instance.run()
    except:
        taxBox = Element("tax-value")
        taxBox.element.innerText = "err << run failed potential object error"
