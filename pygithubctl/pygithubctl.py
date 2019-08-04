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

import argparse
import base64
import os
import logging


from github import Github
from github import GithubException
from configurer import configure_logging

logger = configure_logging(logging.getLogger('pygithubctl'))


def download(repository, sha, source, target):
    logger.info('Fetching %s from %s', source, repository)
    try:
        contents = repository.get_contents(source, ref=sha)
        data = base64.b64decode(contents.content)
        output = open(target, "w")
        output.write(data)
        output.close()
    except (GithubException, IOError) as exception:
        logging.error('Error processing %s: %s', source, exception)


def get_sha(repository, tag):
    branches = repository.get_branches()
    matched_branches = [match for match in branches if match.name == tag]

    if matched_branches:
        return matched_branches[0].commit.sha

    tags = repository.get_tags()
    matched_tags = [match for match in tags if match.name == tag]

    if not matched_tags:
        raise ValueError('No Tag or Branch exists with that name')
    return matched_tags[0].commit.sha


def resolve_target(source, target):
    if os.path.isdir(target):
        filename = os.path.basename(source)
        return os.path.join(target, filename)
    else:
        return target


def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('--hostname', required=True)
    parser.add_argument('--auth_token', required=True)
    parser.add_argument('--repository', required=True)
    parser.add_argument('--branch', required=False)
    parser.add_argument('--tag', required=False)
    parser.add_argument('--file_path', required=True)
    parser.add_argument('--destination', required=True)
    args = parser.parse_args()
    return args


def get_branch_or_tag(options):
    branch_or_tag = "master"
    if options.branch:
        branch_or_tag = options.branch
    if options.tag:
        branch_or_tag = options.tag
    return branch_or_tag


def get_base_url(hostname):
    if not hostname:
        raise ValueError('hostname must not be blank on empty')
    return "https://{hostname}/api/v3".format(hostname=hostname)


def main():
    logger.info('Fetching file from GitHub repository')
    options = get_options()
    base_url = get_base_url(options.hostname)
    branch_or_tag = get_branch_or_tag(options)
    destination = resolve_target(options.file_path, options.destination)

    logger.info('base_url: %s', base_url)
    logger.info('branch_or_tag: %s', branch_or_tag)
    logger.info('destination: %s', destination)

    github = Github(base_url=base_url, login_or_token=options.auth_token, verify=False)
    organization = github.get_user().get_orgs()[0]
    logger.info('organization: %s', organization)

    repository = organization.get_repo(options.repository)
    sha = get_sha(repository, branch_or_tag)
    logger.info('sha: %s', sha)

    download(repository, sha, options.file_path, destination)


if __name__ == '__main__':
    main()