import setuptools
import time


setuptools.setup(
    name='stack-suggestions-bot',
    url='https://github.com/jeremybanks/stack-suggestions-bot',
    author='Jeremy Banks',
    author_email='j@jeremybanks.ca',
    license='MIT',
    packages=[
        'stackexchange',
    ],
    py_modules=[
        'stacksuggestionsbot',
    ],
    package_dir={
        '': 'src'
    },
    install_requires=[
        'httmock==1.2.2',
        'irc==8.7',
        'pprintpp==0.2.1',
        'pytest==2.5.2',
        'pytest-capturelog==0.7',
        'requests==2.2.1'
    ]
)
