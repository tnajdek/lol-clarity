#!/usr/bin/env python
import unittest
from hud import Vec2, Rect
from clarity import Clarity, UIElement

with open('spectator.bin', 'rb') as f:
    test_data = f.read()

with open('spectator-reanchored.bin', 'rb') as f:
    test_data_reanchored = f.read()

class TestClarity(unittest.TestCase):
    def setUp(self):
        self.spectator_data = test_data

    def test_read_clarity(self):
        spectatorUI = Clarity.from_binary(test_data)
        # self.assertEqual(spectatorUI.name, "None")
        self.assertEqual(len(spectatorUI.elements), 2)
        minimap_frame = spectatorUI.elements['MinimapFrame']
        self.assertIsInstance(minimap_frame, UIElement)
        self.assertEqual(minimap_frame.name, 'MinimapFrame')
        self.assertIsInstance(minimap_frame.anchor, Vec2)
        self.assertIsInstance(minimap_frame.position, Rect)

    def test_write_clarity(self):
        spectatorUI = Clarity.from_binary(test_data)
        reAnchored = Clarity.from_binary(test_data_reanchored)

        minimap_content = spectatorUI.elements['MinimapContent']
        minimap_content.anchor = Vec2(2.0, 3.0)

        target_minimap_content = reAnchored.elements['MinimapContent']
        self.assertEqual(minimap_content.anchor, target_minimap_content.anchor)

    def test_write_clarity_binary_contents(self):
        spectatorUI = Clarity.from_binary(test_data)
        minimap_content = spectatorUI.elements['MinimapContent']
        minimap_content.anchor = Vec2(2.0, 3.0)
        minimap_content.position = Rect(Vec2(1234, 5678), minimap_content.position.end)
        self.assertEqual(spectatorUI.to_binary(), test_data_reanchored)


if __name__ == '__main__':
    unittest.main()
