from setuptools import setup, find_packages


setup(
    name='chacal',
    version='0.0.1',
    author='Jack Moreno',
    author_email='jack12972@gmail.com',
    packages=find_packages(),
    install_requires=[
            'click',
            'rich',
            'requests',
            'beautifulsoup4'
    ],
    entry_points={
        'console_scripts': ['chacal=chacal:cli']
    }
)
