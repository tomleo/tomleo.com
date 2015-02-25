# This project is intentended to work with both Python 2.7 and Python 3.4
#
# It will be a merge of https://bitbucket.org/TomLeo/tomleo3000 and https://github.com/tomleo/tomleo.com
#
# Will also merge in content from:
# - https://github.com/tomleo/CactusBlog
# 
# Progress:
# - merged https://bitbucket.org/TomLeo/tomleo3000
# - removed https://bitbucket.org/TomLeo/tblog
# - removed https://bitbucket.org/TomLeo/pelican-blog
#
# Leaving Along for now:
# - https://bitbucket.org/TomLeo/blog.tomleo.com
#   This is a statically generated blog using Pelican
# - https://bitbucket.org/TomLeo/tumblrpy
#   This converts all tumblr posts into stand-alone HTML pages

REMOTE_REPO=git@github.com:tomleo/tomleo.com.git

getrepo:
	git clone $(REMOTE_REPO)

config:
	#curl config.tar.gz.dat
	openssl enc -aes-256-cbc -d -in ./config.tar.gz.dat | tar xz;

packconfig:
	tar cz config/ | openssl enc -aes-256-cbc -out ./config.tar.gz.dat;

cleanconfig:
	rm -r ./config

py2venv:
	virtualenv py2venv

py3venv:
	py3venv py3venv

