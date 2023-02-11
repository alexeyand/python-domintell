from setuptools import setup

with open('README.md') as file:
    long_description = file.read()

setup(name='python-domintell',
      version='0.0.18.b1',
      url='https://github.com/alexeyand/python-domintell',
      license='MIT',
      author='Alexey And',
      install_requires=["pyserial", "chardet"],
      author_email='alex@icona.one',
      description="Python Library for the Domintell protocol",
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=['domintell', 'domintell.utils', 'domintell.connections', 'domintell.messages', 'domintell.modules'],
      platforms='any',
     )
