import logging
import base64
import os
import argparse

from github import Github
from github import GithubException


def download(repository, sha, source, target):
    logging.info('Fetching %s from %s', source, repository)
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
    if not options.branch:
        return options.branch
    if not options.tag:
        return options.tag
    return "master"


def get_base_url(hostname):
    if not hostname:
        raise ValueError('hostname must not be blank on empty')
    return "https://{hostname}/api/v3".format(hostname=hostname)


def main():
    logging.info('Fetching file from GitHub repository')
    options = get_options()
    base_url = get_base_url(options.hostname)
    branch_or_tag = get_branch_or_tag()
    destination = resolve_target(options.destination)

    logging.info('base_url: %s', base_url)
    logging.info('branch_or_tag: %s', branch_or_tag)
    logging.info('destination: %s', destination)

    github = Github(base_url=base_url, login_or_token=options.auth_token)
    organization = github.get_user().get_orgs()[0]
    logging.info('organization: %s', organization)

    repository = organization.get_repo(options.repository)
    sha = get_sha(repository, branch_or_tag)
    logging.info('sha: %s', sha)

    download(repository, sha, options.file_path, destination)


if __name__ == '__main__':
    main()
