# test_gilded_rose.py
import pytest
from gilded_rose import Item, GildedRose

def test_conjured_item_degrades_twice_as_fast_before_sell_in():
    items = [Item("Conjured Mana Cake", 3, 6)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 2
    assert items[0].quality == 4  # Decreases by 2

def test_conjured_item_degrades_twice_as_fast_after_sell_in():
    items = [Item("Conjured Mana Cake", 0, 6)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == -1
    assert items[0].quality == 2  # Decreases by 4

def test_conjured_item_quality_never_negative():
    items = [Item("Conjured Mana Cake", 3, 1)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 0  # Cannot go below 0

def test_conjured_item_quality_never_above_50():
    items = [Item("Conjured Mana Cake", 3, 50)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 48  # Decreases by 2

# Add to existing tests
def test_aged_brie_quality_increases_after_sell_in():
    items = [Item("Aged Brie", 0, 48)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == -1
    assert items[0].quality == 49

def test_backstage_passes_quality_zero_after_concert():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == -1
    assert items[0].quality == 0

def test_sulfuras_no_change():
    items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 5
    assert items[0].quality == 80

def test_normal_item_quality_never_above_50():
    items = [Item("Elixir of the Mongoose", 5, 50)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 49