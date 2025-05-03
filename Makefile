# Makefile for building LaTeX document in /doc
# Uses pdflatex with bibliography and puts intermediate files in .build directory

# Configuration variables
DOC_DIR := doc
MAIN_TEX := main.tex
BIBFILE := real.bib

# LaTeX commands with appropriate flags
LATEX := pdflatex -interaction=nonstopmode
BIBTEX := bibtex

# Main targets
.PHONY: all clean

all: $(DOC_DIR)/$(OUTPUT_NAME).pdf

# Build PDF with bibliography
$(DOC_DIR)/$(OUTPUT_NAME).pdf:
	# Run pdflatex in the doc directory
	cd $(DOC_DIR) && $(LATEX) $(MAIN_TEX)
	# Run bibtex for bibliography
	cd $(DOC_DIR) && $(BIBTEX) $(MAIN_TEX:.tex=)
	# Run pdflatex twice more to resolve references
	cd $(DOC_DIR) && $(LATEX) $(MAIN_TEX)
	cd $(DOC_DIR) && $(LATEX) $(MAIN_TEX)

# Clean up build files
clean:
	rm -f $(DOC_DIR)/*.aux $(DOC_DIR)/*.bbl $(DOC_DIR)/*.blg $(DOC_DIR)/*.log $(DOC_DIR)/*.out