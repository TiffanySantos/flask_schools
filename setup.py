from setuptools import setup, find_packages

requires = [
  'flask',
  'flask-sqlalchemy',
  'psycopg2',
]

setup(
  name='flask_todo',
  version='0.0',
  description='A todo list built with flask',
  author='https://opensource.com/article/18/4/flask and me',
  keywords='web flask',
  packages=find_packages(),
  include_paclage_data=True,
  install_requires=requires
)