class Daniswara:
    def __init__(self, umur, lucky_number_1, lucky_number_2):
        self.umur = umur
        self.lucky_number_1 = lucky_number_1
        self.lucky_number_2 = lucky_number_2

    def getName(self):
        print("Hallo! Nama saya Daniswara")

    def getAge(self):
        print("18 tahun")

    def calculateOnesLuck(self):
        luckyness = ((self.lucky_number_1 + self.lucky_number_2) * self.umur) / 100
        print(f"Keberuntunganmu hari ini adalah {luckyness} %")