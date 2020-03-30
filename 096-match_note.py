class Solution(object):

    def match_note_to_magazine(self, ransom_note, magazine):
        if ransom_note is None or magazine is None:
            raise TypeError('ransom_note or magazine cannot be None')
        seen_chars = {}
        for char in magazine:
            if char in seen_chars:
                seen_chars[char] += 1
            else:
                seen_chars[char] = 1
        for char in ransom_note:
            try:
                seen_chars[char] -= 1
            except KeyError:
                return False
            if seen_chars[char] < 0:
                return False
        return True