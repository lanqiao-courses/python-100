from enum import Enum


class Data(object):

    def __init__(self, timestamp, num_people, event_type):
        self.timestamp = timestamp
        self.num_people = num_people
        self.event_type = event_type

    def __lt__(self, other):
        return self.timestamp < other.timestamp


class Period(object):

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __repr__(self):
        return str(self.start) + ', ' + str(self.end)


class EventType(Enum):

    ENTER = 0
    EXIT = 1


class Solution(object):

    def find_busiest_period(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if not data:
            return None
        data.sort()
        max_period = Period(0, 0)
        max_people = 0
        curr_people = 0
        for index, interval in enumerate(data):
            if interval.event_type == EventType.ENTER:
                curr_people += interval.num_people
            elif interval.event_type == EventType.EXIT:
                curr_people -= interval.num_people
            else:
                raise ValueError('Invalid event type')
            if (index < len(data) - 1 and
                    data[index].timestamp == data[index + 1].timestamp):
                continue
            if curr_people > max_people:
                max_people = curr_people
                max_period.start = data[index].timestamp
                if index < len(data) - 1:
                    max_period.end = data[index + 1].timestamp
                else:
                    max_period.end = data[index].timestamp
        return max_period