from unittest import TestCase

import pygithubctl


class TestResolveTarget(TestCase):

    def test_resolve_target(self):
        source = "/var/lib/pygithubctl/README.rst"
        target = "/tmp"
        expected = "/tmp/README.rst"
        actual = pygithubctl.resolve_target()
        self.assertTrue(isinstance(actual, expected))