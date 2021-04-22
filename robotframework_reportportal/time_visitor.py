import logging

from robot.api import ResultVisitor

_stack = []
corrections = {}


class TimeVisitor(ResultVisitor):

    @staticmethod
    def _correct_starts(o, node_class):
        """
        starttime wants to be the oldest start time of its children.
        only correcting null starttime.
        """
        if o.starttime:
            corrected = False
            for parent_id in _stack:
                if corrections[parent_id][0] is None or \
                        corrections[parent_id][0] > o.starttime:
                    corrections[parent_id][0] = o.starttime
                    corrected = True
            if corrected:
                logging.debug(
                    "Correcting parents' starttime to {0} based on {2}={1}"
                    .format(o.starttime, o.id, node_class))
        else:
            _stack.append(o.id)
            corrections[o.id] = [None, None]

    @staticmethod
    def _correct_ends(o, node_class):
        """
        endtime wants to be the newest end time of its children.
        only correcting null endtime.
        """
        if o.endtime:
            corrected = False
            for parent_id in _stack:
                if corrections[parent_id][1] is None or \
                        corrections[parent_id][1] < o.endtime:
                    corrections[parent_id][1] = o.endtime
                    corrected = True
            if corrected:
                logging.debug(
                    "Correcting parents' endtime to {0} based on {2}={1}"
                    .format(o.endtime, o.id, node_class))
        if o.id == _stack[-1]:
            _stack.pop()

    def start_suite(self, suite):
        self._correct_starts(suite, "suite")

    def end_suite(self, suite):
        self._correct_ends(suite, "suite")

    def start_test(self, test):
        self._correct_starts(test, "test")

    def end_test(self, test):
        self._correct_ends(test, "test")

    def start_keyword(self, keyword):
        self._correct_starts(keyword, "kw")

    def end_keyword(self, keyword):
        self._correct_ends(keyword, "kw")