from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='pygithubctl',
      version='2.7.11',
      description='The GitHub command-line tool, pygithubctl.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/sarathkumarsivan/pygithubctl',
      author='Sarath Kumar Sivan',
      author_email='sarathkumarsivan@gmail.com',
      license='MIT',
      packages=['pygithubctl'],
      install_requires=[
          'PyGithub',
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['pygithubctl=pygithubctl:main'],
      },
      include_package_data=True,
      zip_safe=False
      )
