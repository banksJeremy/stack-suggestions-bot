import setuptools


setuptools.setup(
    name='stack-suggestions-bot',
    version='0.0.0dev1',
    url='https://github.com/jeremybanks/stack-suggestions-bot',
    author='Jeremy Banks',
    author_email='j@jeremybanks.ca',
    license='MIT',
    packages=[
        'stackexchange',
        'stacksuggestionsbot'
    ],
    py_modules=[
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
        'requests==2.2.1',
        'ChatExchange==0.0.0dev2'
    ],
    dependency_links=[
        # These should also be specified in requirements.txt.
        ("git+https://github.com/jeremybanks/ChatExchange.git"
         "@b40518ac3b06cfbc759a909ac1cf53075170839f#egg=ChatExchange-0.0.0dev2")
    ]
)
