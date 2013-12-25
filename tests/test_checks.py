import os
from unittest import TestCase
from dodgy.checks import check_file


class TestChecks(TestCase):

    def _run_checks(self, file_name):
        filepath = os.path.join(os.path.dirname(__file__), 'testdata', file_name)
        with open(filepath) as f:
            file_contents = f.read()
        return check_file(file_contents)

    def _check_messages(self, messages, expected_keys):
        for key in expected_keys:
            for message in messages:
                if key == message[1]:
                    break
            else:
                self.fail("Expected key %s but was not found" % key)

    def _do_test(self, file_name, *expected_keys):
        messages = self._run_checks(file_name)
        self._check_messages(messages, expected_keys)

    def test_amazon_keys(self):
        self._do_test('amazon.py', 'aws_secret_key', 'aws_access_key')

    def test_diffs(self):
        self._do_test('diff.py', 'diff')

    def test_password_varnames(self):
        self._do_test('passwords1.py', 'password')
        self._do_test('passwords2.py', 'password')
        self._do_test('passwords3.py', 'password')

    def test_secret_varnames(self):
        self._do_test('secrets1.py', 'secret')
        self._do_test('secrets2.py', 'secret')
        self._do_test('secrets3.py', 'secret')
