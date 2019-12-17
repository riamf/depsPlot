from setuptools import setup

setup(name='depsPlot',
      version='0.1',
      description='wip',
      url='#',
      author='riamf',
      author_email='riamf2@gmail.com',
      license='MIT',
      py_modules=['depsPlot'],
      install_requires=[
          'Click'
      ],
      entry_points='''
        [console_scripts]
        depsPlot=cli
      ''',
      zip_safe=False)
