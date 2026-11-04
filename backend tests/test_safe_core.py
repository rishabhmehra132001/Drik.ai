# Cell 3: Test file banao
%%writefile tests/test_safe_core.py
import unittest, sys, os
sys.path.insert(0, 'backend')
from safe_core import check_safety

class TestSafeCore(unittest.TestCase):
    def test_microwave_hard_stop(self):
        self.assertEqual(check_safety("microwave", {})["status"], "HARD_STOP")
    def test_tv_hard_stop(self):
        self.assertEqual(check_safety("led tv", {})["status"], "HARD_STOP")
    def test_swollen_battery_stop(self):
        self.assertFalse(check_safety("smartphone", {"swollen_battery": True})["allowed"])
    def test_fan_without_unplug_stop(self):
        self.assertFalse(check_safety("ceiling fan", {"mains_unplugged": False})["allowed"])
    def test_fan_with_unplug_allowed(self):
        self.assertTrue(check_safety("ceiling fan", {"mains_unplugged": True})["allowed"])
    def test_laptop_allowed(self):
        self.assertTrue(check_safety("laptop", {"swollen_battery": False})["allowed"])
    def test_unknown_device_stop(self):
        self.assertFalse(check_safety("unknown xyz", {})["allowed"])

if __name__ == '__main__':
    unittest.main()
