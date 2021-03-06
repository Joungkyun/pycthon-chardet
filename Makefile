PYTHON = /usr/bin/python
NAME = chardet
PROG = chardet
MAKE = make
ARCH = $(shell uname -m)

DIST_FILES = COPYING INSTALL Changes README


all: build

build:
	$(PYTHON) setup.py build

install:
	$(PYTHON) setup.py install

test: build
	$(MAKE) -C tests

clean:
	rm -rf build *.bz2 MANIFEST chardet.egg-info
	find . -name "*.pyc" -exec rm -f {} \;

distclean: clean
	rm -rf dist

dist:
	$(PYTHON) setup.py sdist --formats=bztar
#	version=`cat src/version.h | grep MOD_CHARDET_VERSION | awk '{print $$3}' | sed 's/"//g'`; \
#	mkdir -p dist/$(NAME)-$$version; \
#	cp -af $(DIST_FILES) Makefile src *.py chardet dist/$(NAME)-$$version/; \
#	cd dist; tar cvfpj $(NAME)-$$version.tar.bz2 $(NAME)-$$version; cd -; \
#	rm -fr dist/$(NAME)-$$version

bdist:
	$(PYTHON) setup.py bdist_wheel --plat-name manylinux1_$(ARCH)
