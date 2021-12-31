##############################################################################################
# PROJECT-SPECIFIC PARAMETERS                                                                #
##############################################################################################


PROJECT_NAME = thermal-cam
PYTHON ?= python3
SOURCE_FOLDER = pithermalcam
EXAMPLES_FOLDER = examples
SEQENTIAL_FOLDER = sequential_versions
##############################################################################################
# ENVIRONMENT SETUP                                                                          #
##############################################################################################


.PHONY: env-create
env-create:
	$(PYTHON) -m venv .venv --prompt $(PROJECT_NAME)
	make env-update
	#
	# Don't forget to activate the environment before proceeding! You can run:
	# source .venv/bin/activate


.PHONY: env-update
env-update:
	bash -c "\
                . .venv/bin/activate && \
                pip install wheel && \
                CFLAGS=-fcommon pip install --upgrade -r requirements.txt \
        "


.PHONY: env-delete
env-delete:
	rm -rf .venv


.PHONY: requirements-update
requirements-update:
	pip-compile


.PHONY: env-reset
env-reset:
	pip-sync

##############################################################################################
# BUILD                                                                                      #
##############################################################################################

.PHONY: clean
clean:
	find $(SOURCE_FOLDER) -name __pycache__ | xargs rm -rf
	find $(SOURCE_FOLDER) -name '*.pyc' -delete
	rm -rf .*cache


.PHONY: reformat
reformat:
	isort $(SOURCE_FOLDER) $(EXAMPLES_FOLDER) $(SEQENTIAL_FOLDER)
	black $(SOURCE_FOLDER) $(EXAMPLES_FOLDER) $(SEQENTIAL_FOLDER)


.PHONY: lint
lint:
	$(PYTHON) -m pycodestyle . --exclude '.venv'
	isort --check-only $(SOURCE_FOLDER) $(EXAMPLES_FOLDER) $(SEQENTIAL_FOLDER)
	black --check $(SOURCE_FOLDER) $(EXAMPLES_FOLDER) $(SEQENTIAL_FOLDER)
	pylint $(SOURCE_FOLDER) $(EXAMPLES_FOLDER) $(SEQENTIAL_FOLDER)
	# mypy $(SOURCE_FOLDER)


###############################################################################
# START WEB SERVER                                                            #
###############################################################################

.PHONY: start_server
start_server:
	mkdir -p logs && \
	. .venv/bin/activate && PYTHONPATH=. python examples/web_server.py > logs/thermal_out.txt 2>logs/thermal_err.txt
