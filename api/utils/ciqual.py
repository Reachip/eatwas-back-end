from . import ciqual_wb

class Food:
    def __init__(self, name, calories, glucides, protein, lipid):
        self.name = name
        self.calories = calories
        self.glucides = glucides
        self.protein = protein
        self.lipid = lipid

    def __str__(self):
        return self.name


class CiqualTable:
    def __init__(self):
        workbook = ciqual_wb
        self.sheet = workbook.sheet_by_index(0)

    def _get_food_group_characteristics(self, index_start, index_end):
        foods = []

        for index in range(index_start, index_end):
            food_name = self.sheet.cell_value(index, 7)
            food_calories = str(self.sheet.cell_value(index, 9)).replace(",", ".")
            food_glucides = str(self.sheet.cell_value(index, 15)).replace(",", ".")
            food_protein = str(self.sheet.cell_value(index, 13)).replace(",", ".")
            food_lipid = str(self.sheet.cell_value(index, 13)).replace(",", ".")

            foods.append(
                Food(
                    food_name,
                    # 300 représente environ 300 gramme de quantité pour un repas
                    float(food_calories) * 3.5,
                    float(food_glucides) * 3.5,
                    float(food_protein) * 3.5,
                    float(food_lipid) * 3.5,
                )
            )

        return foods

    @property
    def get_mixed_dishes(self):
        return self._get_food_group_characteristics(62, 198)

    @property
    def get_fruits_and_vegetables(self):
        return self._get_food_group_characteristics(310, 746)

    @property
    def get_cereals_products(self):
        return self._get_food_group_characteristics(747, 953)

    @property
    def get_meats_and_eggs(self):
        return self._get_food_group_characteristics(1155, 1894)
