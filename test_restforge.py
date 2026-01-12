# test_restforge.py
"""
Tests for RestForge module.
"""

import unittest
from restforge import RestForge

class TestRestForge(unittest.TestCase):
    """Test cases for RestForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RestForge()
        self.assertIsInstance(instance, RestForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RestForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
