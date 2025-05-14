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