from setuptools import setup

setup(
   name='uipy',
   version='1.0',
   description='A user interface for ipython',
   author='Emilio L.',
   author_email='eludena@gmail.com',
   python_requires='>3',
   install_requires=[
   'ipython'
   ],
   #packages=['uipy'],
   #package_dir={'uipy': 'src/uipy'},
   # package_data={'mypkg': ['data/*.dat']},
   scripts=[
            'scripts/uipy',
           ]
)
