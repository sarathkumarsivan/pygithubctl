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

from pygithubctl.pygithubctl import get_options


class TestGetOptions(TestCase):

    def test_required_options(self):
        auth_token = "authToken"
        repository = "repository"
        owner = "owner"
        tag = "tag"
        path = "README.rst"
        type = "f"
        destination = "/home/user/git"
        http_ssl_verify = True
        options = get_options(['fetch',
                               '--auth-token', auth_token,
                               '--repository', repository,
                               '--owner', owner,
                               '--tag', tag,
                               '--path', path,
                               '--type', type,
                               '--destination', destination,
                               '--http-ssl-verify', str(http_ssl_verify)])
        self.assertTrue(options.auth_token)
        self.assertEqual(options.auth_token, auth_token)
        self.assertTrue(options.repository)
        self.assertEqual(options.repository, repository)
        self.assertTrue(options.owner)
        self.assertEqual(options.owner, owner)
        self.assertTrue(options.tag)
        self.assertEqual(options.tag, tag)
        self.assertTrue(options.destination)
        self.assertEqual(options.destination, destination)
        self.assertTrue(options.http_ssl_verify)
        self.assertEqual(options.http_ssl_verify, http_ssl_verify)
