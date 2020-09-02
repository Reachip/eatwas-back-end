import datetime
from . import green_peace_wb


class FruitAndVegetable:
    def __init__(self, name, months_of_consumption):
        self.name = name
        self.months_of_consumption = months_of_consumption

    def __str__(self):
        return self.name


class GreenPeaceSheet:
    def __init__(self):
        workbook = green_peace_wb
        self.fruit_sheet = workbook.sheet_by_index(0)
        self.vegetable_sheet = workbook.sheet_by_index(1)
        self.actual_month = datetime.datetime.now().month
        self.month = {y + 1: x for x, y in zip(range(12), range(12))}

    def fruit_according_to_month(self):
        fruit = [
            FruitAndVegetable(
                self.fruit_sheet.cell_value(x, self.month[self.actual_month]),
                self.fruit_sheet.cell_value(0, self.month[self.actual_month])
            )
            for x in range(25)
            if self.fruit_sheet.cell_value(x, self.month[self.actual_month]) != ""
            and self.fruit_sheet.cell_value(x, self.month[self.actual_month]) != " "
        ]
        del fruit[0]
        return fruit

    def vegetable_according_to_month(self):
        fruit = [
            FruitAndVegetable(
                sheet.cell_value(x, self.month[self.actual_month]),
                sheet.cell_value(1, self.month[self.actual_month])
            )
            for x in range(30)
            if self.fruit_sheet.cell_value(x, self.month[self.actual_month]) != ""
            and self.fruit_sheet.cell_value(x, self.month[self.actual_month]) != " "
        ]
        del fruit[0]
        return fruit
