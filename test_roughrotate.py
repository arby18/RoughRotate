# test_roughrotate.py
"""
Tests for RoughRotate module.
"""

import unittest
from roughrotate import RoughRotate

class TestRoughRotate(unittest.TestCase):
    """Test cases for RoughRotate class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RoughRotate()
        self.assertIsInstance(instance, RoughRotate)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RoughRotate()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
