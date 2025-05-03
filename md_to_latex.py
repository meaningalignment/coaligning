#!/usr/bin/env python3
import re
import os

def convert_markdown_to_latex(input_file):
    """Convert a markdown file to LaTeX syntax"""
    with open(input_file, 'r') as f:
        content = f.read()
    
    # Skip the first line if it's a heading (already handled in main.tex)
    lines = content.split('\n')
    if lines[0].startswith('# '):
        lines = lines[2:]  # Skip title and the blank line after it
    
    content = '\n'.join(lines)
    
    # Convert headings
    content = re.sub(r'# ([^\n]+)', r'\\section{\1}', content)
    content = re.sub(r'## ([^\n]+)', r'\\subsection{\1}', content)
    content = re.sub(r'### ([^\n]+)', r'\\subsubsection{\1}', content)
    
    # Convert bold and italic
    content = re.sub(r'\*\*([^*]+)\*\*', r'\\textbf{\1}', content)
    content = re.sub(r'\*([^*]+)\*', r'\\textit{\1}', content)
    
    # Convert lists
    content = re.sub(r'^\* (.+)$', r'\\begin{itemize}\n\\item \1', content, flags=re.MULTILINE)
    content = re.sub(r'^\* (.+)$', r'\\item \1', content, flags=re.MULTILINE)
    
    # Find where lists end and add closing tag
    lines = content.split('\n')
    in_list = False
    result = []
    
    for i, line in enumerate(lines):
        if line.strip().startswith('\\begin{itemize}'):
            in_list = True
        
        result.append(line)
        
        if in_list and i+1 < len(lines) and not lines[i+1].strip().startswith('\\item'):
            result.append('\\end{itemize}')
            in_list = False
    
    content = '\n'.join(result)
    if in_list:
        content += '\n\\end{itemize}'
    
    # Convert special characters
    content = content.replace('&', '\\&')
    content = content.replace('%', '\\%')
    content = content.replace('$', '\\$')
    content = content.replace('#', '\\#')
    content = content.replace('_', '\\_')
    content = content.replace('{', '\\{')
    content = content.replace('}', '\\}')
    
    # Fix the special characters within commands that we already converted
    content = re.sub(r'\\section\{\\#', r'\\section{', content)
    content = re.sub(r'\\subsection\{\\#', r'\\subsection{', content)
    content = re.sub(r'\\subsubsection\{\\#', r'\\subsubsection{', content)
    content = re.sub(r'\\textbf\{\\', r'\\textbf{', content)
    content = re.sub(r'\\textit\{\\', r'\\textit{', content)
    
    # Convert dashes
    content = content.replace('---', '---')
    
    # Fix quotes
    content = content.replace('"', "``")
    content = content.replace('"', "''")
    
    return content

def add_section_to_main(section_file, main_file="main.tex"):
    """Add converted section content to main LaTeX file"""
    section_name = os.path.basename(section_file).split('.')[0].split('-')[1]
    section_num = os.path.basename(section_file).split('-')[0]
    
    latex_content = convert_markdown_to_latex(section_file)
    
    # Skip the abstract as it's already included
    if section_num == "0":
        return
    
    # Read the main file
    with open(main_file, 'r') as f:
        main_content = f.read()
    
    # Find where to insert the new section
    marker = "% Content will be included here from individual markdown files"
    if marker in main_content:
        # Insert content before the end document tag
        main_content = main_content.replace(marker, 
                                           f"{marker}\n\n% Section {section_num}: {section_name}\n{latex_content}")
    
    # Write back to the main file
    with open(main_file, 'w') as f:
        f.write(main_content)
    
    print(f"Added section {section_num}: {section_name}")

def process_all_sections():
    """Process all markdown sections and add them to main.tex"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    section_files = sorted([f for f in os.listdir(base_dir) if re.match(r'\d+-.*\.md', f)])
    
    for section_file in section_files:
        add_section_to_main(os.path.join(base_dir, section_file))

if __name__ == "__main__":
    process_all_sections()
    print("Conversion complete. Check main.tex for results.")