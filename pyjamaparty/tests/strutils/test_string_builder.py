import unittest
from pyjamaparty.strutils.string_builder import StringBuilder


class TestStringBuilder(unittest.TestCase):

    def test_noarg_builder(self):
        s = StringBuilder()
        self.assertTrue(isinstance(s, StringBuilder))
        self.assertEqual(len(s), 0)

    def test_empty_builder(self):
        s = StringBuilder("")
        self.assertTrue(isinstance(s, StringBuilder))
        self.assertEqual(len(s), 0)

    def test_arg_builder(self):
        expected_str = "wow"
        s = StringBuilder(expected_str)
        self.assertTrue(isinstance(s, StringBuilder))
        self.assertEqual(len(s), len(expected_str))
        self.assertEqual(expected_str, str(s))

    def test_append_builder(self):
        expected_str = "wow"
        s = StringBuilder()
        s.append(expected_str)
        self.assertEqual(expected_str, str(s))

    def test_chained_append_builder(self):
        expected_str = "wow"
        s = StringBuilder()
        s.append(expected_str).append(expected_str)
        self.assertEqual('{}{}'.format(expected_str, expected_str), str(s))

    def test_modify_str_builder_slice(self):
        original_str = "wow, such a nice builder"
        modified_str = "whee, such a nice builder"
        s = StringBuilder(original_str)
        s[:4] = "whee,"
        self.assertEqual(modified_str, str(s))

    def test_get_substring_builder(self):
        original_str = "wow, such a nice builder"
        s = StringBuilder(original_str)
        sub_str = s[:3]
        self.assertEqual("wow", sub_str)

    def test_convert_to_str_builder(self):
        s = StringBuilder("wow")
        self.assertTrue(isinstance(str(s), str))

    def test_len_str_builder(self):
        original_str = "wow"
        s = StringBuilder(original_str)
        self.assertEqual(len(original_str), len(s))

    def test_iter_str_builder(self):
        original_str = "wow"
        str_builder = StringBuilder(original_str)
        for i, s_char in enumerate(str_builder):
            self.assertEqual(original_str[i], s_char)

    def test_add_operator(self):
        s1 = StringBuilder("hello")
        s2 = s1 + " world"
        self.assertEqual(str(s1), "hello")
        self.assertEqual(str(s2), "hello world")
        self.assertIsNot(s1, s2)

    def test_delitem(self):
        s = StringBuilder("hello")
        del s[1]
        self.assertEqual(str(s), "hllo")

    def test_remove(self):
        s = StringBuilder("hello world")
        s.remove("o w")
        self.assertEqual(str(s), "hellorld")
        with self.assertRaises(ValueError):
            s.remove("foo")

    def test_to_string_builder(self):
        s = StringBuilder("wow")
        self.assertTrue(isinstance(s.to_string(), str))


if __name__ == '__main__':
    unittest.main()