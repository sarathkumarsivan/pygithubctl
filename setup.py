from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='pygithubctl',
      version='2.7.10',
      description='The GitHub command-line tool, pygithubctl, allows you to run commands against GitHub repository',
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
