pygithubctl
===========

.. image:: http://img.shields.io/badge/Docs-latest-green.svg
.. image:: https://travis-ci.org/sarathkumarsivan/pygithubctl.svg?branch=master
.. image:: https://img.shields.io/pypi/v/pygithubctl.svg

The GitHub command-line tool, pygithubctl, allows you to fetch a single file GitHub repository.

Install
-------

::

    pip install pygithubctl

Run
-------

::

    pygithubctl --hostname github.your.company.com \
                --auth_token x12d6ef54aa6d4ffe45c85f84f4f4998c2f9ed2a \
                --repository your-repository \
                --branch master \
                --file_path README.md \
                --destination /tmp \
                --http_ssl_verify False

Supports
--------
Tested on Python 2.7