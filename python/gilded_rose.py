# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        # Given rules values
        max_quality = 50
        min_quality = 0
        min_day = 0
        lose_quality = 1
        earn_quality = 1
        day_value = 1
        concert_step = {"day_max": 11, "day_min": 6}
        for item in self.items:
            # Sulfuras is constant, initial check
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
            elif item.name != "Backstage passes to a TAFKAL80ETC concert" and item.name != "Aged Brie":
                if item.quality > min_quality:
                    item.quality -= lose_quality
                    # Conjured items special lose quality condition
                    if item.quality > min_quality and item.name == "Conjured Mana Cake" :
                        item.quality -= lose_quality
            else:
                if item.quality < max_quality:
                    item.quality += earn_quality
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < concert_step["day_max"] and item.quality < max_quality:
                            item.quality += earn_quality
                        if item.sell_in < concert_step["day_min"] and item.quality < max_quality:
                            item.quality += earn_quality
            item.sell_in -= day_value
            if item.sell_in < min_day:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.name == "Conjured Mana Cake" and item.quality > min_quality:
                            item.quality -= lose_quality
                        elif item.quality > min_quality:
                            item.quality -= lose_quality
                    else:
                        item.quality -= item.quality
                else:
                    if item.quality < max_quality:
                        item.quality += earn_quality


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
