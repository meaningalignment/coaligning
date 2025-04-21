#!/bin/bash

# Copy contents of chapters 0-8 to clipboard
cat 0-abstract.md 1-introduction.md 2-existing_toolkits.md 3-new_toolkit.md 4-case_studies.md 5-roadmap.md 6-conclusion.md 7-footnotes.md 8-related_work.md | pbcopy

echo "Contents of chapters 0-8 copied to clipboard!" 