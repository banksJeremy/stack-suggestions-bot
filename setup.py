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
        'ChatExchange==0.0.0dev1'
    ],
    dependency_links=[
        ("git+ssh://git@github.com/jeremybanks/ChatExchange.git"
         "@dd4ed4f4e22f6f668d1c60c4f7fa09cf43f2e290#egg=ChatExchange-0.0.0dev1")
    ]
)
