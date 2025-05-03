# Makefile for building LaTeX document in /doc
# Uses pdflatex with bibliography and puts intermediate files in .build directory

# Configuration variables
DOC_DIR := doc
MAIN_TEX := main.tex
OUTPUT_NAME := coaligning
BIBFILE := real.bib

# LaTeX commands with appropriate flags
LATEX := pdflatex -interaction=nonstopmode
BIBTEX := bibtex

# Main targets
.PHONY: all clean

all: $(DOC_DIR)/$(OUTPUT_NAME).pdf

# Build PDF with bibliography
$(DOC_DIR)/$(OUTPUT_NAME).pdf:
	# Copy neurips_2023.sty to doc directory if needed
	[ -f $(DOC_DIR)/neurips_2023.sty ] || cp neurips_2023.sty $(DOC_DIR)/
	# Run pdflatex in the doc directory
	cd $(DOC_DIR) && $(LATEX) $(MAIN_TEX)
	# Run bibtex for bibliography
	cd $(DOC_DIR) && $(BIBTEX) $(MAIN_TEX:.tex=)
	# Run pdflatex twice more to resolve references
	cd $(DOC_DIR) && $(LATEX) $(MAIN_TEX)
	cd $(DOC_DIR) && $(LATEX) $(MAIN_TEX)
	# Rename the output file
	cd $(DOC_DIR) && mv $(MAIN_TEX:.tex=.pdf) $(OUTPUT_NAME).pdf

# Clean up build files
clean:
	rm -f $(DOC_DIR)/$(OUTPUT_NAME).pdf
	rm -f $(DOC_DIR)/*.aux $(DOC_DIR)/*.bbl $(DOC_DIR)/*.blg $(DOC_DIR)/*.log $(DOC_DIR)/*.out $(DOC_DIR)/main.pdf