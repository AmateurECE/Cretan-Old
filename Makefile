###############################################################################
# NAME:		    Makefile
#
# AUTHOR:	    Ethan D. Twardy <edtwardy@mtu.edu>
#
# DESCRIPTION:	    Makefile for the project. Includes a target to setup the
#		    venv.
#
# CREATED:	    01/23/2019
#
# LAST EDITED:	    01/25/2019
###

# Force pipenv to put the package cache here
export PIPENV_CACHE_DIR=$(PWD)
# Force pipenv to put the venv in the project directory
export PIPENV_VENV_IN_PROJECT=1

.PHONY: pipenv

pipenv:
	pipenv install

##############################################################################
