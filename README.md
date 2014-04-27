stack-suggestions-bot
=====================

[![Travis CI build status for master](https://travis-ci.org/jeremybanks/stack-suggestions-bot.svg?branch=master)](https://travis-ci.org/jeremybanks/stack-suggestions-bot)

This will be an IRC chat bot which suggests relevant Stack Exchange
questions when questions are asked in chat.

For simplicity, the Makefile will install dependencies, run tests, and
run the application, but you must first have installed pip, and you
are *strongly* recommended to also have installed virtualenv and
activated a new environment. (Particularly because when the Makefile
installs dependencies it will also link our packages into environment's
site packages.)
