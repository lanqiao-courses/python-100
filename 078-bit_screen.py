class BitsScreen(object):

    def draw_line(self, screen, x1, x2):
        if None in (screen, x1, x2):
            raise TypeError('Invalid argument: None')
        if not screen:
            raise ValueError('Invalid arg: Empty screen')
        MAX_BIT_VALUE = len(screen) * 8
        if x1 < 0 or x2 < 0 or x1 >= MAX_BIT_VALUE or x2 >= MAX_BIT_VALUE:
            raise ValueError('Invalid arg: x1 or x2 out of bounds')
        start_bit = x1 % 8
        end_bit = x2 % 8
        first_full_byte = x1 // 8
        if start_bit != 0:
            first_full_byte += 1
        last_full_byte = x2 // 8
        if end_bit != (8 - 1):
            last_full_byte -= 1
        for byte in range(first_full_byte, last_full_byte + 1):
            screen[byte] = int('11111111', base=2)
        start_byte = x1 // 8
        end_byte = x2 // 8
        if start_byte == end_byte:
            left_mask = (1 << (8 - start_bit)) - 1
            right_mask = ~((1 << (8 - end_bit - 1)) - 1)
            mask = left_mask & right_mask
            screen[start_byte] |= mask
        else:
            start_mask = (1 << (8 - start_bit)) - 1
            end_mask = 1 << (8 - end_bit - 1)
            screen[start_byte] |= start_mask
            screen[end_byte] |= end_mask