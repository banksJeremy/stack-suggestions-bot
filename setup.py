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
        ("git+https://github.com/jeremybanks/ChatExchange.git"
         "@acc83976e07ca0be0a97006809d7b5abda02f88e#egg=ChatExchange-0.0.0dev2")
    ]
)
