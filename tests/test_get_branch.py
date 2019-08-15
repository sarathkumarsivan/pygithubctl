#!/usr/bin/env python

# Copyright (c) 2019 Sarath Kumar Sivan, https://github.com/sarathkumarsivan
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from unittest import TestCase

from pygithubctl.pygithubctl import get_branch_or_tag
from pygithubctl.pygithubctl import get_options


class TestGetBranch(TestCase):

    def test_with_branch_option(self):
        expected = "dev"
        options = get_options(['fetch',
                               '--auth-token', 'someToken',
                               '--repository', 'pygithubctl',
                               '--owner', 'sarathkumarsivan',
                               '--branch', 'dev',
                               '--path', 'README.rst',
                               '--type', 'file',
                               '--destination', '/tmp',
                               '--http-ssl-verify', 'True'])
        actual = get_branch_or_tag(options)
        self.assertEqual(actual, expected)

    def test_with_branch_option_master(self):
        expected = "master"
        options = get_options(['fetch',
                               '--auth-token', 'someToken',
                               '--repository', 'pygithubctl',
                               '--owner', 'sarathkumarsivan',
                               '--branch', 'master',
                               '--path', 'README.rst',
                               '--type', 'file',
                               '--destination', '/tmp',
                               '--http-ssl-verify', 'True'])
        actual = get_branch_or_tag(options)
        self.assertEqual(actual, expected)

    def test_without_branch_option(self):
        expected = "master"
        options = get_options(['fetch',
                               '--auth-token', 'someToken',
                               '--repository', 'pygithubctl',
                               '--owner', 'sarathkumarsivan',
                               '--path', 'README.rst',
                               '--type', 'file',
                               '--destination', '/tmp',
                               '--http-ssl-verify', 'True'])
        actual = get_branch_or_tag(options)
        self.assertEqual(actual, expected)

    def test_with_branch_tag_option(self):
        expected = "dev"
        options = get_options(['fetch',
                               '--auth-token', 'someToken',
                               '--repository', 'pygithubctl',
                               '--owner', 'sarathkumarsivan',
                               '--branch', 'dev',
                               '--tag', 'release-1.0',
                               '--path', 'README.rst',
                               '--type', 'file',
                               '--destination', '/tmp',
                               '--http-ssl-verify', 'True'])
        actual = get_branch_or_tag(options)
        self.assertEqual(actual, expected)


