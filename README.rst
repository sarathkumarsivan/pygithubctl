pygithubctl
===========
|docs| |travis| |pypi|

.. |docs| image:: http://img.shields.io/badge/Docs-latest-green.svg
.. |travis| image:: https://travis-ci.org/sarathkumarsivan/pygithubctl.svg?branch=master
.. |pypi| image:: https://img.shields.io/pypi/v/pygithubctl.svg

The GitHub command-line tool, pygithubctl, lets you download a specific file, folder or directory from a remote Git repository hosted on GitHub. You can also download an entire project from GitHub without version control data. Git operates on a whole-repository basis and if you have projects where finer-grained access is necessary, you can use submodules; each submodule is a separate Git project, and thus can be cloned individually. But if a project wasn't configured so from the beginning, you can make use of pygithubctl to download the file or folders you are really interested in.

Installation
------------

The pygithubctl can be installed via pip, the Python package manager. If pip isn’t already available on your system of Python, run the following commands to install it:
::

    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py --user

Then install pygithubctl
::

    sudo pip install pygithubctl

Upgrade
-------
You can upgrade pygithubctl via pip, the Python package manager; issue the below command to perform the upgrade:
::

    sudo pip install pygithubctl --upgrade

Run
-------
You can run pygithubctl by issuing the below command. Below command downloads a single file named README.md from <repository-name> repository.
::

    pygithubctl fetch \
	   --hostname github.your.company.com \
   	   --auth_token a13d3ef34aa6d2ffe32c46f84f4f4998c5f3ed9a \
   	   --repository repository-name \
   	   --branch master \
   	   --file_path README.md \
   	   --content_type file \
   	   --destination /tmp \
   	   --http_ssl_verify False


Supports
--------
Tested on Python 2.7