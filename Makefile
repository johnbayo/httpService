.PHONY: install develop test uninstall build
.DEFAULT_GOAL := install

install:
	@echo "Installing HTTP Service"
	@echo " "
	@python setup.py install --record installed_files.txt
	@echo "you can run the server using the"
	@echo "myhttpservice -p <PORT>"

develop:
	@echo "Installing in Development Mode"
	@python setup.py develop

test:
	@echo "Testing HTTP Package"
	python -m unittest -v

uninstall:
	@echo "Removing the HTTP Service Package"
ifneq ($(wildcard installed_files.txt), '')
	@echo "Deleting Installed Packages"
	@cat installed_files.txt
	@xargs rm -rf < installed_files.txt
	@rm -rf installed_files.txt
else
	@echo "Installer Files not Found"
endif

build:
	@echo "Creating Source Distribution"
	@python setup.py sdist