#!/usr/bin/env python3
import re
import sys
import time
import argparse
import bibtexparser
from urllib.parse import quote_plus
import requests
from bs4 import BeautifulSoup
import scholarly

def parse_bibtex_file(file_path):
    """Parse BibTeX file and return a list of entries."""
    with open(file_path, 'r', encoding='utf-8') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    return bib_database.entries

def search_google_scholar(title, authors):
    """Search Google Scholar for a paper and return the first result."""
    query = f"{title} {authors.split(',')[0]}"
    print(f"Searching Google Scholar for: {query}")
    
    try:
        # Using scholarly as it's more reliable than direct web scraping
        search_query = scholarly.search_pubs(query)
        result = next(search_query, None)
        if result:
            return {
                'found': True,
                'title': result.bib.get('title'),
                'authors': result.bib.get('author'),
                'url': result.bib.get('url', ''),
                'year': result.bib.get('year'),
                'venue': result.bib.get('journal', ''),
                'result': result
            }
    except Exception as e:
        print(f"Error searching Google Scholar: {e}")
    
    return {'found': False}

def get_bibtex_from_scholarly(result):
    """Get BibTeX entry from scholarly result."""
    try:
        if 'result' in result and result['result']:
            # Get detailed information including citation data
            scholarly_result = result['result']
            try:
                scholarly.fill(scholarly_result)
                return scholarly_result.bibtex
            except Exception as e:
                print(f"Error getting BibTeX: {e}")
    except Exception as e:
        print(f"Error processing scholarly result: {e}")
    
    return None

def manual_search_option(entry):
    """Provide manual search URL for the user."""
    title = entry.get('title', '')
    author = entry.get('author', '').split(' and ')[0]
    year = entry.get('year', '')
    
    query = f"{title} {author} {year}"
    encoded_query = quote_plus(query)
    
    google_scholar_url = f"https://scholar.google.com/scholar?q={encoded_query}"
    return f"Manual search URL: {google_scholar_url}"

def check_reference(entry):
    """Check if a reference exists and get its correct BibTeX."""
    title = entry.get('title', '')
    authors = entry.get('author', '')
    citation_key = entry.get('ID', 'unknown')
    
    print(f"\nChecking: {citation_key}")
    print(f"Title: {title}")
    print(f"Authors: {authors}")
    
    result = search_google_scholar(title, authors)
    
    if result['found']:
        print(f"✅ Found matching paper: {result['title']}")
        print(f"Authors: {result['authors']}")
        print(f"Venue: {result['venue']}")
        print(f"Year: {result['year']}")
        
        bibtex = get_bibtex_from_scholarly(result)
        if bibtex:
            print("\nBibTeX entry:")
            print(bibtex)
            return True, bibtex
        else:
            print("Couldn't retrieve BibTeX automatically.")
    else:
        print("❌ No exact match found on Google Scholar")
        
    # Always provide manual search option as fallback
    print(manual_search_option(entry))
    return False, None

def main():
    parser = argparse.ArgumentParser(description='Check academic references against Google Scholar')
    parser.add_argument('bibtex_file', help='Path to the BibTeX file')
    parser.add_argument('--check-all', action='store_true', help='Check all references, not just suspicious ones')
    args = parser.parse_args()
    
    try:
        entries = parse_bibtex_file(args.bibtex_file)
        print(f"Found {len(entries)} references in {args.bibtex_file}")
        
        verified_count = 0
        problematic_count = 0
        
        for entry in entries:
            # Let's check if the reference looks suspicious
            suspicious = False
            
            # Academic papers typically have volume, number, pages for journals
            if entry.get('ENTRYTYPE') == 'article':
                if 'journal' in entry and entry['journal'] == 'Netflix documentary':
                    suspicious = True  # This is clearly not an academic article
                if not args.check_all:
                    # Check for missing expected fields in journal articles
                    if 'volume' not in entry or 'pages' not in entry:
                        suspicious = True
            
            # Preprints should have arXiv IDs
            if 'journal' in entry and 'arxiv' in entry['journal'].lower():
                if not re.search(r'arXiv:\d{4}\.\d{5}', entry.get('journal', '')):
                    suspicious = True
            
            # Check all references if flag is set, otherwise only check suspicious ones
            if args.check_all or suspicious:
                verified, bibtex = check_reference(entry)
                
                if verified:
                    verified_count += 1
                else:
                    problematic_count += 1
                
                # Add a small delay to avoid rate limiting
                time.sleep(2)
        
        print(f"\nSummary: Checked {verified_count + problematic_count} references")
        print(f"Verified: {verified_count}")
        print(f"Problematic: {problematic_count}")
        
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())