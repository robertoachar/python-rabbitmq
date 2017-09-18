from setuptools import setup

setup(name='python_rabbitmq',
      version='1.0.0',
      description='A playground for Python and RabbitMQ.',
      author='Roberto Achar',
      author_email='robertoachar@gmail.com',
      license='MIT',
      packages=['python_rabbitmq'],
      entry_point={
          'console_scripts': [
              'python_rabbitmq=python_rabbitmq.__main__:main'
          ]
      },
      install_requires=[],
      zip_safe=False)
