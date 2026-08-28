# test_karmasway.py
"""
Tests for KarmaSway module.
"""

import unittest
from karmasway import KarmaSway

class TestKarmaSway(unittest.TestCase):
    """Test cases for KarmaSway class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = KarmaSway()
        self.assertIsInstance(instance, KarmaSway)
        
    def test_run_method(self):
        """Test the run method."""
        instance = KarmaSway()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
