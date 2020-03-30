class Solution(object):

    def format_license_key(self, license_key, k):
        if license_key is None:
            raise TypeError('license_key must be a str')
        if not license_key:
            raise ValueError('license_key must not be empty')
        formatted_license_key = []
        num_chars = 0
        for char in license_key[::-1]:
            if char == '-':
                continue
            num_chars += 1
            formatted_license_key.append(char.upper())
            if num_chars >= k:
                formatted_license_key.append('-')
                num_chars = 0
        if formatted_license_key and formatted_license_key[-1] == '-':
            formatted_license_key.pop(-1)
        return ''.join(formatted_license_key[::-1])