# gilded_rose.py
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

# Constants
AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"
CONJURED = "Conjured"

class ItemUpdater:
    def update(self, item):
        pass

    def _constrain_quality(self, quality):
        return max(0, min(50, quality))

class NormalItemUpdater(ItemUpdater):
    def update(self, item):
        item.sell_in -= 1
        item.quality = self._constrain_quality(item.quality - (1 if item.sell_in >= 0 else 2))

class AgedBrieUpdater(ItemUpdater):
    def update(self, item):
        item.sell_in -= 1
        item.quality = self._constrain_quality(item.quality + 1)

class BackstagePassUpdater(ItemUpdater):
    def update(self, item):
        item.sell_in -= 1
        increase = 1
        if item.sell_in < 10:
            increase += 1
        if item.sell_in < 5:
            increase += 1
        if item.sell_in < 0:
            item.quality = 0
        else:
            item.quality = self._constrain_quality(item.quality + increase)

class SulfurasUpdater(ItemUpdater):
    def update(self, item):
        pass  # Sulfuras doesn't change

class ConjuredItemUpdater(ItemUpdater):
    def update(self, item):
        item.sell_in -= 1
        item.quality = self._constrain_quality(item.quality - (2 if item.sell_in >= 0 else 4))

class GildedRose:
    def __init__(self, items):
        self.items = items
        self.updaters = {
            AGED_BRIE: AgedBrieUpdater(),
            BACKSTAGE_PASSES: BackstagePassUpdater(),
            SULFURAS: SulfurasUpdater(),
        }

    def update_quality(self):
        for item in self.items:
            if CONJURED in item.name:
                updater = ConjuredItemUpdater()
            else:
                updater = self.updaters.get(item.name, NormalItemUpdater())
            updater.update(item)