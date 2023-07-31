#!/usr/bin/env python3
"""
Unit tests
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import Dict, Tuple, Union


class TestAccessNestedMap(unittest.TestCase):
    """ Contains tests for utils.access_nested_map """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Dict,
                               path: Tuple[str],
                               expected: Union[int, Dict]):
        """ Test function for access_nested_map """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Dict,
                                         path: Tuple[str],
                                         exception: Exception):
        """ Test that assert equal raises KeyError """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)
