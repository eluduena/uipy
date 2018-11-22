from setuptools import setup

setup(
   name='uipy3',
   version='1.0',
   description='A user interface for ipython3',
   author='Emilio L.',
   author_email='eludena@gmail.com',
   #packages=['uipy3'],
   #package_dir={'uipy3': 'src/uipy3'},
   # package_data={'mypkg': ['data/*.dat']},
   scripts=[
            'scripts/uipy3',
           ]
)
