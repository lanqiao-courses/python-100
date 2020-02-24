from collections import OrderedDict


class Anagram(object):

    def group_anagrams(self, items):
        if items is None:
            raise TypeError('items cannot be None')
        if not items:
            return items
        anagram_map = OrderedDict()
        for item in items:
            # Use a tuple, which is hashable and
            # serves as the key in anagram_map
            sorted_chars = tuple(sorted(item))
            if sorted_chars in anagram_map:
                anagram_map[sorted_chars].append(item)
            else:
                anagram_map[sorted_chars] = [item]
        result = []
        for value in anagram_map.values():
            result.extend(value)
        return result