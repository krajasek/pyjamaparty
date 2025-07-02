

import io


class StringBuilder(object):

    def __init__(self, strr=''):
        self.str_list = list(strr)

    def __getitem__(self, item):
        if isinstance(item, slice):
            return "".join(self.str_list[item])
        return self.str_list[item]

    def __setitem__(self, key, value):
        if isinstance(key, slice):
            self.str_list[key] = list(value)
        else:
            self.str_list[key] = value

    def __repr__(self):
        return "".join(self.str_list)

    def __len__(self):
        return len(self.str_list)

    def __iter__(self):
        return iter(self.str_list)

    def __add__(self, other):
        new_builder = StringBuilder()
        new_builder.str_list = self.str_list + list(other)
        return new_builder

    def append(self, other):
        self.str_list.extend(list(other))
        return self

    def __str__(self):
        return self.__repr__()

    def __delitem__(self, key):
        del self.str_list[key]

    def remove(self, sub, start=None, end=None):
        """
        Removes the first occurrence of a substring.
        Raises ValueError if the substring is not found.
        """
        index = str(self).find(sub, start, end)
        if index == -1:
            raise ValueError("substring not found")
        del self[index:index+len(sub)]

    def to_string(self):
        return self.__str__()
