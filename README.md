# Overview

This is an ansible playbook for deploying [Sentry](http://getsentry.com ) on a local target. It assumes Ubuntu running on the target.

# Usage

First, generate your vars and inventory files:

	python ./autogen.py --smtp-server=yoursmtp.server.com --server-email=noreply@somedomain.com --target=myserver.com --root-url=http://myserver.com

And then run ansible:

	ansible-playbook -u root -i inventory deploy.yml

