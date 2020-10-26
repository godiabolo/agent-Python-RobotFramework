import re
import string

from robot.api import ResultVisitor
from robot.result import Result, TestSuite, TestCase, Keyword, Message

from . import listener
from .variables import _variables


class RobotResultsVisitor(ResultVisitor):

    _link_pattern = re.compile("src=[\"\']([^\"\']+)[\"\']")

    def start_result(self, result):
        if ("RP_LAUNCH" not in _variables):
            _variables["RP_LAUNCH"] = result.suite.name
        if ("RP_LAUNCH_DOC" not in _variables):
            _variables["RP_LAUNCH_DOC"] = result.suite.doc

    def start_suite(self, suite):
        attrs = {
            'id': suite.id,
            'longname': suite.longname,
            'doc': suite.doc,
            'metadata': suite.metadata,
            'source': suite.source,
            'suites': suite.suites,
            'tests': suite.tests,
            'totaltests': suite.statistics.all.total,
            'starttime': suite.starttime
        }
        listener.start_suite(suite.name, attrs)

    def end_suite(self, suite):
        attrs = {
            'id': suite.id,
            'longname': suite.longname,
            'doc': suite.doc,
            'metadata': suite.metadata,
            'source': suite.source,
            'suites': suite.suites,
            'tests': suite.tests,
            'totaltests': suite.statistics.all.total,
            'starttime': suite.starttime,
            'endtime': suite.endtime,
            'elapsedtime': suite.elapsedtime,
            'status': suite.status,
            'statistics': suite.statistics,
            'message': suite.message,
        }
        listener.end_suite(None, attrs)

    def start_test(self, test):
        attrs = {
            'id': test.id,
            'longname': test.longname,
            # 'originalname': test.originalname,
            'doc': test.doc,
            'tags': list(test.tags),
            'critical': test.critical,
            'template': '',
            # 'lineno': test.lineno,
            'starttime': test.starttime,
        }
        listener.start_test(test.name, attrs)

    def end_test(self, test):
        attrs = {
            'id': test.id,
            'longname': test.longname,
            # 'originalname': test.originalname,
            'doc': test.doc,
            'tags': list(test.tags),
            'critical': test.critical,
            'template': '',
            # 'lineno': test.lineno,
            'starttime': test.starttime,
            'endtime': test.endtime,
            'elapsedtime': test.elapsedtime,
            'status': test.status,
            'message': test.message,
        }
        listener.end_test(test.name, attrs)

    def start_keyword(self, kw):
        attrs = {
            'type': string.capwords(kw.type),
            'kwname': kw.kwname,
            'libname': kw.libname,
            'doc': kw.doc,
            'args': kw.args,
            'assign': kw.assign,
            'tags': kw.tags,
            'starttime': kw.starttime,
        }
        listener.start_keyword(kw.name, attrs)

    def end_keyword(self, kw):
        attrs = {
            'type': string.capwords(kw.type),
            'kwname': kw.kwname,
            'libname': kw.libname,
            'doc': kw.doc,
            'args': kw.args,
            'assign': kw.assign,
            'tags': kw.tags,
            'starttime': kw.starttime,
            'endtime': kw.endtime,
            'elapsedtime': kw.elapsedtime,
            'status': kw.status,
        }
        listener.end_keyword(kw.name, attrs)

    def start_message(self, msg):
        if (msg.message != ''):
            message = {
                'message': msg.message,
                'level': msg.level,
            }
            m = self._link_pattern.search(msg.message)
            if m:
                message["message"] = m.group()
                listener.log_message_with_image(message, m.group(1))
            else:
                listener.log_message(message)