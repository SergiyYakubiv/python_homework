# method
import datetime
from datetime import datetime
from typing import List, Union

class Fish:
    def __init__(self) -> None:
        self.name = "oseledets"
        self.price_in_uah_per_kilo = 11.2
        self.catch_date = datetime("21/01/2022")
        self.origin = "Norway"
        self.body_only = True
        self.weight = 100

class FishShop:
    def add_fish(self, fish_name: str, total_weight: float) -> None:
        fish_amount_in_kilo = {"korop": 23.4,"salmon": 331.9}
        fish_amount_in_kilo["salmon"] = 30

        fish_name = "salmon"
        pass

    def get_fish_names_sort_by_price(self) -> List[Union[str, float]]:
        pass

    def sell_fish(self, fish_name: str, weight: float) -> float:
        pass

    def cast_out_old_fish(self) -> List[Union[str, float]]:
        pass




class Seller:
    def salary(self) -> None:
        pass

    def calculate_fish_price_in_uah(self, fish_name: str, weight: float, price_in_uah_per_kilo: float) -> float:
        pass

class Buyer:
    def buy_fish(self, fish_name: str, price_in_uah_for_fish: float,weight: float, fish_is_fresh: bool) -> bool:
        pass