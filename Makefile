# VARIABLE
SCSS_DIR := "assets/scss/vendor"

# LIST OF THE COMMANDS
help:
	@echo "Commands available:"
	@echo "- 'rebuild': rebuild the public directory in the 'site'"

# COMMANDS
rebuild:
	@rm -rf site/public
	@cd site && hugo && cd .. 
	@echo "SITE REBUILT"

chroma:
	hugo gen chromastyles --style=monokai > assets/scss/syntax/syntax-dark.scss