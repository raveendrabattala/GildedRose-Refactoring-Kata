from typing import List


class Item:
    def __init__(self, name: str, sell_in: int, quality: int):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self) -> str:
        return f"{self.name}, {self.sell_in}, {self.quality}"


# Constants
AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"
CONJURED = "Conjured"


class ItemUpdater:
    """Base class for updating item properties."""
    def update(self, item: Item) -> None:
        pass

    def _constrain_quality(self, quality: int) -> int:
        """Ensure quality is between 0 and 50."""
        return max(0, min(50, quality))


class NormalItemUpdater(ItemUpdater):
    """Updater for standard items."""
    def update(self, item: Item) -> None:
        item.sell_in -= 1
        item.quality = self._constrain_quality(
            item.quality - (1 if item.sell_in >= 0 else 2)
        )


class AgedBrieUpdater(ItemUpdater):
    """Updater for Aged Brie, which increases in quality."""
    def update(self, item: Item) -> None:
        item.sell_in -= 1
        item.quality = self._constrain_quality(item.quality + 1)


class BackstagePassUpdater(ItemUpdater):
    """Updater for Backstage Passes, with variable quality increase."""
    def update(self, item: Item) -> None:
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
    """Updater for Sulfuras, which never changes."""
    def update(self, item: Item) -> None:
        pass


class ConjuredItemUpdater(ItemUpdater):
    """Updater for Conjured items, which degrade twice as fast."""
    def update(self, item: Item) -> None:
        item.sell_in -= 1
        item.quality = self._constrain_quality(
            item.quality - (2 if item.sell_in >= 0 else 4)
        )


class GildedRose:
    """Manages inventory updates for items."""
    def __init__(self, items: List[Item]):
        self.items = items
        self.updaters = {
            AGED_BRIE: AgedBrieUpdater(),
            BACKSTAGE_PASSES: BackstagePassUpdater(),
            SULFURAS: SulfurasUpdater(),
        }

    def update_quality(self) -> None:
        """Update quality and sell_in for all items."""
        for item in self.items:
            updater = self.updaters.get(item.name, NormalItemUpdater())
            if CONJURED in item.name:
                updater = ConjuredItemUpdater()
            updater.update(item)

