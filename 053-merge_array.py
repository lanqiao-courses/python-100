class Array(object):

    def merge_into(self, source, dest, source_end_index, dest_end_index):
        if source is None or dest is None:
            raise TypeError('source or dest cannot be None')
        if source_end_index < 0 or dest_end_index < 0:
            raise ValueError('end indices must be >= 0')
        if not source:
            return dest
        if not dest:
            return source
        source_index = source_end_index - 1
        dest_index = dest_end_index - 1
        insert_index = source_end_index + dest_end_index - 1
        while dest_index >= 0:
            if source[source_index] > dest[dest_index]:
                source[insert_index] = source[source_index]
                source_index -= 1
            else:
                source[insert_index] = dest[dest_index]
                dest_index -= 1
            insert_index -= 1
        return source