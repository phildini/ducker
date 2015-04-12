About
-----

Ducker is a chat bot to assist in rubber-duck debugging. Right now, it
does nothing. What it will do, hopfully, is have a knowledge base of 
docs that it can pull from, and then guide a user through asking
questions to the right doc for solving their problem.

Overview
--------

There are three main parts:

- The interface, which will eventually be irc- or slack-compatible, but
  will start as a simple command line input, for testing.
- The docs parser. You point ducker at a repo or url, and it parses the
  documentation it finds into meaningful keywords or topics
- The answering engine, which sits between the interface and the parsed
  docs to ask and answer questions with as much intelligence as possible.

The goal is to have a easily-deployable chat bot (Hubot-on-heroku easy)
whcih cna help eng orgs do better rubbber-duck debugging.

Problem areas
-------------

The interface and the docs parser are more-or-less straightforward
problems. We'll probably be starting development there, since we know
the libraries to use to make those things happen.

The answering engine is a complete unknown to me, and anyone with ideas
or experience greatly appreciated. Create a pull request/issue, or ping
#docker on freenode. 