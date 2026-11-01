BIN_DIR = $(HOME)/.local/bin
ROOT = $(CURDIR)

.PHONY: install shortcut uninstall

# Creates a virtual environment and installs the dependencies.
install:
	python3 -m venv venv
	venv/bin/pip install spotipy python-dotenv

# Installs the `trebletop` and `trebletop-update` commands.
shortcut:
	mkdir -p $(BIN_DIR)
	ln -sf $(ROOT)/bin/trebletop $(BIN_DIR)/trebletop
	ln -sf $(ROOT)/bin/trebletop-update $(BIN_DIR)/trebletop-update
	@echo "Installed. Make sure $(BIN_DIR) is in your PATH."

uninstall:
	rm -f $(BIN_DIR)/trebletop $(BIN_DIR)/trebletop-update
