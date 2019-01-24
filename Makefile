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
# LAST EDITED:	    01/23/2019
###

.PHONY: virtualenv

virtualenv:
	virtualenv -p `which python3 || which python` .
	source bin/activate && pip install -r ./requirements.txt

##############################################################################
