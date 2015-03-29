# This project is intentended to work with both Python 2.7 and Python 3.4
#
# Need to merge https://github.com/tomleo/tomleo.com into this repo
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
#
# Client side RST parsing:
#   
#   It would be nice to have a medium like editor that represented things as
#   ReStructuredText instead of markdown.
#
#   I want to implement an RST parser that can handle a subset of the lanuage.
#   Tables and potentially other complicated (and lesser used) constructs will
#   not be implemented.
#
#   HTML tables are eaiser to work with than reST ones (and more tooling is
#   available to convert to HTML tables)
#
#   Notes:
#   - Docutils info (current parser) http://docutils.sourceforge.net/docs/dev/hacking.html
#   - Mailing List: docutils-develop@lists.sourceforge.net
#   - Java Parser: http://svn.nuiton.org/jrst/trunk/ (code comments in spanish)
#   - Docutil parser notes: http://code.nabla.net/doc/docutils/api/docutils/parsers/docutils.parsers.rst.html#customizing-the-parser
#   - AST for reST http://nim-lang.org/rstast.html
#   - HTML/Latex generator http://nim-lang.org/rstgen.html
#   - C reST parser http://permalink.gmane.org/gmane.text.docutils.devel/6105

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

serve:
	waitress-serve --port=$PORT tomtleo.wsgi:application

