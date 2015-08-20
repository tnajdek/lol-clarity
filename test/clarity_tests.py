#!/usr/bin/env python
import os
import unittest
from clarity.hud import Vec2, Rect
from clarity.clarity import Clarity, UIElement



with open(os.path.dirname(__file__) + '/spectator.bin', 'rb') as f:
    test_data = f.read()

with open(os.path.dirname(__file__) + '/clarity.bin', 'rb') as f:
    ui_data = f.read()

with open(os.path.dirname(__file__) + '/spectator-reanchored.bin', 'rb') as f:
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

    def test_process_clarity(self):
        ui = Clarity.from_binary(ui_data)
        self.assertEqual(len(ui.elements), 1379)

        element = ui.elements['TargetAD_Icon']
        self.assertEqual(element.anchor.x, 0)
        self.assertEqual(element.anchor.y, 0)
        self.assertEqual(element.position.start.x, 14)
        self.assertEqual(element.position.start.y, 16)
        self.assertEqual(element.position.end.x, 33)
        self.assertEqual(element.position.end.y, 35)

        element.anchor = Vec2(0.5, 0)
        new_data = ui.to_binary()

        new_ui = Clarity.from_binary(new_data)
        new_element = new_ui.elements['TargetAD_Icon']
        self.assertEqual(new_element.anchor.x, 0.5)
        self.assertEqual(new_element.anchor.y, 0)
        self.assertEqual(new_element.position.start.x, 14)
        self.assertEqual(new_element.position.start.y, 16)
        self.assertEqual(new_element.position.end.x, 33)
        self.assertEqual(new_element.position.end.y, 35)

    def test_dogfood(self):
        ui = Clarity.from_binary(ui_data)
        element = ui.elements['TargetAD_Icon']
        element.anchor = Vec2(element.anchor.x, element.anchor.y)
        element.position = Rect(
            Vec2(
                element.position.start.x,
                element.position.start.y
            ),
            Vec2(
                element.position.end.x,
                element.position.end.y
            )
        )
        processed_data = ui.to_binary()
        self.assertEqual(ui_data, processed_data)


if __name__ == '__main__':
    unittest.main()
