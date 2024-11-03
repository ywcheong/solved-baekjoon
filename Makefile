# THIS IS CHATGPT-GENERATED MAKEFILE
# QUERY: "Makefile s.t. `make clean` deletes every no-extension file under /solve"

# Define the directory to clean
SOLVE_DIR := solve

# Find all files without extensions in the solve directory
NO_EXT_FILES := $(shell find $(SOLVE_DIR) -type f ! -name "*.*")

# Default target (does nothing)
all:
	@echo "Use 'make clean' to remove files without extensions in $(SOLVE_DIR)"

# Clean target to remove files without extensions
clean:
	@echo "Removing files without extensions in $(SOLVE_DIR)..."
	@if [ -n "$(NO_EXT_FILES)" ]; then \
		rm -f $(NO_EXT_FILES); \
		echo "Removed files:"; \
		echo "$(NO_EXT_FILES)" | tr ' ' '\n'; \
	else \
		echo "No files without extensions found in $(SOLVE_DIR)"; \
	fi

# Phony targets
.PHONY: all clean
