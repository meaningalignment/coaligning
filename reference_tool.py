#!/usr/bin/env python3
import re
import sys
import time
import json
import argparse
import bibtexparser
from urllib.parse import quote_plus, urlencode
import requests
from bs4 import BeautifulSoup

def load_references_from_file(file_path):
    """Parse BibTeX file and return a list of entries."""
    try:
        with open(file_path, 'r', encoding='utf-8') as bibtex_file:
            bib_database = bibtexparser.load(bibtex_file)
        return bib_database.entries
    except Exception as e:
        print(f"Error loading references: {e}")
        return []

def save_references_to_file(entries, file_path):
    """Save a list of BibTeX entries to a file."""
    db = bibtexparser.bibdatabase.BibDatabase()
    db.entries = entries
    
    writer = bibtexparser.bwriter.BibTexWriter()
    with open(file_path, 'w', encoding='utf-8') as bibtex_file:
        bibtex_file.write(writer.write(db))
    
    print(f"Saved {len(entries)} references to {file_path}")

def search_google_scholar(query, num_results=5):
    """Search Google Scholar and return multiple potential matches."""
    print(f"Searching for: {query}")
    encoded_query = quote_plus(query)
    url = f"https://scholar.google.com/scholar?q={encoded_query}&hl=en&as_sdt=0,5&num={num_results}"
    
    # Set a User-Agent to avoid being blocked
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        
        # Extract search results
        for i, result in enumerate(soup.select('.gs_ri')):
            title_element = result.select_one('.gs_rt')
            title = title_element.text if title_element else "No title found"
            
            # Remove [PDF], [BOOK], etc. from title
            title = re.sub(r'\[.*?\]\s*', '', title).strip()
            
            authors_year_element = result.select_one('.gs_a')
            authors_year = authors_year_element.text if authors_year_element else ""
            
            # Extract year using regex (usually in format "... - ‎YYYY - ...")
            year_match = re.search(r'(\d{4})', authors_year)
            year = year_match.group(1) if year_match else "Unknown"
            
            # Extract authors (usually before the first dash)
            authors = authors_year.split('-')[0].strip() if '-' in authors_year else authors_year
            
            # Get the venue/journal (usually after authors, before year)
            venue_match = re.search(r'- (.*?) - \d{4}', authors_year)
            venue = venue_match.group(1).strip() if venue_match else ""
            
            # Get the citation URL if available (for BibTeX extraction)
            cite_link = None
            for link in result.parent.select('.gs_or_cit a'):
                if 'Cite' in link.text:
                    cite_url = 'https://scholar.google.com' + link['href']
                    cite_link = cite_url
                    break
            
            snippet_element = result.select_one('.gs_rs')
            snippet = snippet_element.text if snippet_element else ""
            
            # Attempt to find detailed links
            detail_links = {}
            if title_element and title_element.select_one('a'):
                detail_links['title_link'] = title_element.select_one('a')['href']
            
            # Look for PDF links
            pdf_link = None
            for link in result.parent.select('.gs_or_ggsm a'):
                if '[PDF]' in link.text:
                    pdf_link = link['href']
                    break
            
            detail_links['pdf'] = pdf_link
            
            results.append({
                'id': i + 1,
                'title': title,
                'authors': authors,
                'year': year,
                'venue': venue,
                'snippet': snippet,
                'cite_link': cite_link,
                'detail_links': detail_links
            })
        
        return results
    
    except Exception as e:
        print(f"Error searching Google Scholar: {e}")
        return []

def get_bibtex_from_citation_link(cite_link):
    """Retrieve BibTeX entry from Google Scholar citation link."""
    if not cite_link:
        return None
    
    # Set a User-Agent to avoid being blocked
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # First get the citation page
        response = requests.get(cite_link, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Find the BibTeX link
        soup = BeautifulSoup(response.text, 'html.parser')
        bibtex_link = None
        
        for link in soup.find_all('a'):
            if link.text.strip() == 'BibTeX':
                bibtex_link = 'https://scholar.google.com' + link['href']
                break
        
        if not bibtex_link:
            return None
        
        # Get the BibTeX content
        bibtex_response = requests.get(bibtex_link, headers=headers, timeout=10)
        bibtex_response.raise_for_status()
        
        return bibtex_response.text.strip()
    
    except Exception as e:
        print(f"Error retrieving BibTeX: {e}")
        return None

def search_semantic_scholar(query):
    """Search Semantic Scholar API for papers and return results with BibTeX."""
    print(f"Searching Semantic Scholar for: {query}")
    
    base_url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        "query": query,
        "limit": 5,
        "fields": "title,authors,venue,year,url,citationCount,openAccessPdf"
    }
    
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        results = []
        for i, paper in enumerate(data.get('data', [])):
            authors = [author.get('name', '') for author in paper.get('authors', [])]
            authors_str = ', '.join(authors)
            
            results.append({
                'id': i + 1,
                'title': paper.get('title', 'No title'),
                'authors': authors_str,
                'year': paper.get('year'),
                'venue': paper.get('venue', ''),
                'url': paper.get('url', ''),
                'citation_count': paper.get('citationCount', 0),
                'pdf_url': paper.get('openAccessPdf', {}).get('url') if paper.get('openAccessPdf') else None,
                'paper_id': paper.get('paperId')
            })
            
        return results
    
    except Exception as e:
        print(f"Error searching Semantic Scholar: {e}")
        return []

def get_bibtex_from_semantic_scholar(paper_id):
    """Retrieve BibTeX for a paper from Semantic Scholar using its ID."""
    if not paper_id:
        return None
    
    try:
        url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}?fields=title,authors,venue,year,journal,url,abstract"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        paper = response.json()
        
        # Generate BibTeX from paper data
        authors = [author.get('name', '') for author in paper.get('authors', [])]
        authors_bibtex = ' and '.join(authors)
        
        # Generate a citation key from first author's last name and year
        first_author = authors[0] if authors else "Unknown"
        last_name = first_author.split()[-1].lower() if ' ' in first_author else first_author.lower()
        year = paper.get('year', 'unknown')
        key = f"{last_name}{year}"
        
        # Determine entry type (article, inproceedings, etc.)
        venue = paper.get('venue', '')
        journal = paper.get('journal', {}).get('name', '')
        entry_type = "article" if journal else "inproceedings" if "proceedings" in venue.lower() else "misc"
        
        # Construct BibTeX
        bibtex = f"@{entry_type}{{{key},\n"
        bibtex += f"  title={{{paper.get('title', 'Unknown title')}}},\n"
        bibtex += f"  author={{{authors_bibtex}}},\n"
        
        if journal:
            bibtex += f"  journal={{{journal}}},\n"
        elif venue:
            bibtex += f"  booktitle={{{venue}}},\n"
        
        if paper.get('year'):
            bibtex += f"  year={{{paper.get('year')}}},\n"
        
        if paper.get('url'):
            bibtex += f"  url={{{paper.get('url')}}},\n"
        
        # Remove trailing comma and close
        bibtex = bibtex.rstrip(',\n') + "\n}"
        return bibtex
    
    except Exception as e:
        print(f"Error retrieving BibTeX from Semantic Scholar: {e}")
        return None

def search_crossref(query):
    """Search CrossRef API for papers."""
    print(f"Searching CrossRef for: {query}")
    
    base_url = "https://api.crossref.org/works"
    params = {
        "query": query,
        "rows": 5,
        "sort": "relevance"
    }
    
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        results = []
        for i, item in enumerate(data.get('message', {}).get('items', [])):
            # Extract authors
            authors = []
            for author in item.get('author', []):
                if 'given' in author and 'family' in author:
                    authors.append(f"{author.get('family')}, {author.get('given')}")
                elif 'name' in author:
                    authors.append(author.get('name'))
            
            authors_str = '; '.join(authors)
            
            # Extract DOI
            doi = item.get('DOI', '')
            
            # Extract type and title
            type_name = item.get('type', 'unknown')
            title = ', '.join(item.get('title', ['No title']))
            
            # Extract container (journal/conference)
            container = item.get('container-title', [''])[0] if item.get('container-title') else ''
            
            # Extract year
            year = None
            if 'published' in item and 'date-parts' in item['published']:
                date_parts = item['published']['date-parts']
                if date_parts and date_parts[0]:
                    year = date_parts[0][0]
            
            results.append({
                'id': i + 1,
                'title': title,
                'authors': authors_str,
                'year': year,
                'venue': container,
                'doi': doi,
                'type': type_name,
                'url': f"https://doi.org/{doi}" if doi else None
            })
            
        return results
    
    except Exception as e:
        print(f"Error searching CrossRef: {e}")
        return []

def get_bibtex_from_doi(doi):
    """Retrieve BibTeX for a paper using its DOI."""
    if not doi:
        return None
    
    headers = {
        'Accept': 'application/x-bibtex',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        url = f"https://doi.org/{doi}"
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # If response is BibTeX
        if 'application/x-bibtex' in response.headers.get('Content-Type', ''):
            return response.text.strip()
        
        # If not, the response might be HTML, so we need to parse it
        # This is a simplified approach and might not work for all DOI providers
        soup = BeautifulSoup(response.text, 'html.parser')
        for script in soup.find_all('script'):
            if script.string and '@' in script.string and 'title' in script.string:
                # This might be a script containing BibTeX
                bibtex_match = re.search(r'(@[a-zA-Z]+{.*?})', script.string, re.DOTALL)
                if bibtex_match:
                    return bibtex_match.group(1)
        
        # If we couldn't find BibTeX in the response, try another approach
        return construct_bibtex_from_crossref(doi)
    
    except Exception as e:
        print(f"Error retrieving BibTeX from DOI: {e}")
        # Try fallback
        return construct_bibtex_from_crossref(doi)

def construct_bibtex_from_crossref(doi):
    """Construct BibTeX entry from CrossRef metadata for a DOI."""
    try:
        url = f"https://api.crossref.org/works/{doi}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        item = data.get('message', {})
        
        # Extract authors
        authors = []
        for author in item.get('author', []):
            if 'given' in author and 'family' in author:
                authors.append(f"{author.get('family')}, {author.get('given')}")
            elif 'name' in author:
                authors.append(author.get('name'))
        
        authors_bibtex = ' and '.join(authors)
        
        # Extract type and title
        type_name = item.get('type', 'misc')
        title = ', '.join(item.get('title', ['No title']))
        
        # Map CrossRef type to BibTeX entry type
        entry_type_map = {
            'journal-article': 'article',
            'proceedings-article': 'inproceedings',
            'book': 'book',
            'book-chapter': 'incollection',
            'posted-content': 'misc'
        }
        entry_type = entry_type_map.get(type_name, 'misc')
        
        # Extract container (journal/conference)
        container = item.get('container-title', [''])[0] if item.get('container-title') else ''
        
        # Extract year
        year = None
        if 'published' in item and 'date-parts' in item['published']:
            date_parts = item['published']['date-parts']
            if date_parts and date_parts[0]:
                year = date_parts[0][0]
        
        # Extract volume, issue, pages
        volume = item.get('volume', '')
        issue = item.get('issue', '')
        pages = item.get('page', '')
        
        # Generate citation key
        first_author = authors[0] if authors else "Unknown"
        last_name = first_author.split(',')[0].lower() if ',' in first_author else first_author.lower()
        key = f"{last_name}{year}" if year else f"{last_name}_unknown"
        
        # Construct BibTeX
        bibtex = f"@{entry_type}{{{key},\n"
        bibtex += f"  title={{{title}}},\n"
        bibtex += f"  author={{{authors_bibtex}}},\n"
        
        if entry_type == 'article' and container:
            bibtex += f"  journal={{{container}}},\n"
        elif entry_type == 'inproceedings' and container:
            bibtex += f"  booktitle={{{container}}},\n"
        
        if year:
            bibtex += f"  year={{{year}}},\n"
        
        if volume:
            bibtex += f"  volume={{{volume}}},\n"
        
        if issue:
            bibtex += f"  number={{{issue}}},\n"
        
        if pages:
            bibtex += f"  pages={{{pages}}},\n"
        
        bibtex += f"  doi={{{doi}}},\n"
        bibtex += f"  url={{https://doi.org/{doi}}},\n"
        
        # Remove trailing comma and close
        bibtex = bibtex.rstrip(',\n') + "\n}"
        return bibtex
    
    except Exception as e:
        print(f"Error constructing BibTeX from CrossRef: {e}")
        return None

def estimate_best_match_score(query, result):
    """Calculate a simple similarity score between query and result."""
    query_lower = query.lower()
    title_lower = result['title'].lower()
    
    # Extract key terms from query (assume they're separated by spaces)
    query_terms = set(re.findall(r'\b\w{3,}\b', query_lower))
    
    # Count how many key terms appear in the title
    title_match_count = sum(1 for term in query_terms if term in title_lower)
    title_match_ratio = title_match_count / len(query_terms) if query_terms else 0
    
    # Check if authors are mentioned in the query
    author_mentioned = False
    if 'authors' in result:
        author_mentioned = any(author.strip().lower() in query_lower 
                            for author in result['authors'].split(','))
    
    # Check if year is mentioned in the query
    year_mentioned = str(result.get('year', '')) in query
    
    # Calculate final score (simple weighted sum)
    score = (title_match_ratio * 0.6) + (0.2 if author_mentioned else 0) + (0.2 if year_mentioned else 0)
    
    return score

def search_command(args):
    """Handle the search subcommand."""
    all_results = []
    
    # 1. Try Google Scholar
    google_results = search_google_scholar(args.query, args.num_results)
    if google_results:
        print(f"\nFound {len(google_results)} results from Google Scholar")
        all_results.extend([{'source': 'google_scholar', 'data': r} for r in google_results])
    
    # 2. Try Semantic Scholar
    semantic_results = search_semantic_scholar(args.query)
    if semantic_results:
        print(f"\nFound {len(semantic_results)} results from Semantic Scholar")
        all_results.extend([{'source': 'semantic_scholar', 'data': r} for r in semantic_results])
    
    # 3. Try CrossRef
    crossref_results = search_crossref(args.query)
    if crossref_results:
        print(f"\nFound {len(crossref_results)} results from CrossRef")
        all_results.extend([{'source': 'crossref', 'data': r} for r in crossref_results])
    
    if not all_results:
        print("No results found from any source.")
        return 1
    
    # Combine and display results
    print("\nCombined search results:")
    print("-" * 80)
    
    displayed_results = []
    for i, result in enumerate(all_results, 1):
        source = result['source']
        data = result['data']
        
        # Normalize result data
        normalized = {
            'id': i,
            'title': data.get('title', 'No title'),
            'authors': data.get('authors', 'No authors'),
            'year': data.get('year', 'Unknown'),
            'venue': data.get('venue', ''),
            'source': source,
            'original_id': data.get('id', 0),
        }
        
        # Add source-specific data
        if source == 'google_scholar':
            normalized['cite_link'] = data.get('cite_link')
        elif source == 'semantic_scholar':
            normalized['paper_id'] = data.get('paper_id')
        elif source == 'crossref':
            normalized['doi'] = data.get('doi')
        
        displayed_results.append(normalized)
        
        # Display the result
        score = estimate_best_match_score(args.query, data)
        confidence = "High" if score > 0.7 else "Medium" if score > 0.4 else "Low"
        
        print(f"[{i}] {normalized['title']}")
        print(f"    Authors: {normalized['authors']}")
        print(f"    Year: {normalized['year']}, Venue: {normalized['venue']}")
        print(f"    Source: {source.replace('_', ' ').title()}")
        print(f"    Match confidence: {confidence} ({score:.2f})")
        
        if source == 'google_scholar':
            print(f"    Citation link available: {'Yes' if data.get('cite_link') else 'No'}")
        elif source == 'semantic_scholar':
            print(f"    Paper ID: {data.get('paper_id', 'N/A')}")
            print(f"    Citations: {data.get('citation_count', 0)}")
        elif source == 'crossref':
            print(f"    DOI: {data.get('doi', 'N/A')}")
        
        print("-" * 80)
    
    print("\nTo get BibTeX for a specific result, run:")
    print(f"python {sys.argv[0]} fetch --id <result_id> --source <source> --identifier <identifier>")
    
    # Find the best match across all sources
    best_result = None
    best_score = -1
    
    for result in all_results:
        score = estimate_best_match_score(args.query, result['data'])
        if score > best_score:
            best_score = score
            best_result = result
    
    if best_result and best_score > 0.6:
        print("\nSuggested command for best match:")
        source = best_result['source']
        data = best_result['data']
        result_id = all_results.index(best_result) + 1
        
        if source == 'google_scholar' and data.get('cite_link'):
            print(f"python {sys.argv[0]} fetch --id {result_id} --source google_scholar --identifier \"{data['cite_link']}\"")
        elif source == 'semantic_scholar' and data.get('paper_id'):
            print(f"python {sys.argv[0]} fetch --id {result_id} --source semantic_scholar --identifier \"{data['paper_id']}\"")
        elif source == 'crossref' and data.get('doi'):
            print(f"python {sys.argv[0]} fetch --id {result_id} --source crossref --identifier \"{data['doi']}\"")
    
    # Save results to a temporary file for easier fetching
    if not args.no_save:
        with open('.search_results.json', 'w') as f:
            json.dump(displayed_results, f)
        print("\nResults saved to .search_results.json for easier fetching.")
    
    return 0

def fetch_bibtex_command(args):
    """Handle the fetch subcommand to retrieve BibTeX."""
    print(f"Fetching BibTeX for result #{args.id}...")
    
    # Try to load saved results if identifier is not provided
    if not args.identifier and not args.source:
        try:
            with open('.search_results.json', 'r') as f:
                saved_results = json.load(f)
                
                # Find the result with the given ID
                result = next((r for r in saved_results if r['id'] == args.id), None)
                
                if result:
                    args.source = result['source']
                    
                    if args.source == 'google_scholar':
                        args.identifier = result.get('cite_link')
                    elif args.source == 'semantic_scholar':
                        args.identifier = result.get('paper_id')
                    elif args.source == 'crossref':
                        args.identifier = result.get('doi')
                    
                    print(f"Found saved result: {result['title']}")
                    print(f"Source: {args.source}")
                    print(f"Identifier: {args.identifier}")
        except Exception as e:
            print(f"Error loading saved results: {e}")
    
    if not args.identifier or not args.source:
        print("Error: Must provide both source and identifier.")
        return 1
    
    # Get BibTeX based on the source
    bibtex = None
    
    if args.source == 'google_scholar':
        bibtex = get_bibtex_from_citation_link(args.identifier)
    elif args.source == 'semantic_scholar':
        bibtex = get_bibtex_from_semantic_scholar(args.identifier)
    elif args.source == 'crossref':
        bibtex = get_bibtex_from_doi(args.identifier)
    
    if not bibtex:
        print("Failed to retrieve BibTeX. The identifier may be invalid or the source might be blocking the request.")
        return 1
    
    print("\nRetrieved BibTeX entry:")
    print("-" * 80)
    print(bibtex)
    print("-" * 80)
    
    # Parse the BibTeX to get the citation key
    try:
        bib_database = bibtexparser.loads(bibtex)
        citation_key = bib_database.entries[0]['ID'] if bib_database.entries else None
        print(f"Citation key: {citation_key}")
        
        # Use custom citation key if provided
        if args.key:
            old_key = citation_key
            citation_key = args.key
            bibtex = bibtex.replace(f"{{{old_key},", f"{{{citation_key},", 1)
            print(f"Using custom citation key: {citation_key}")
    except Exception as e:
        print(f"Warning: Could not parse BibTeX: {e}")
        citation_key = None
    
    if args.output:
        # First read existing references if the file exists
        existing_entries = []
        try:
            existing_entries = load_references_from_file(args.output)
        except:
            pass  # File doesn't exist yet, that's fine
        
        # Parse the new BibTeX entry
        try:
            new_entry = bibtexparser.loads(bibtex).entries[0]
            
            # Check if we should use a custom citation key
            if args.key:
                new_entry['ID'] = args.key
            
            # Add the new entry
            existing_entries.append(new_entry)
            save_references_to_file(existing_entries, args.output)
            print(f"Added entry with key '{new_entry['ID']}' to {args.output}")
        except Exception as e:
            print(f"Error adding BibTeX to output file: {e}")
            
            # Try a simpler approach - just append the BibTeX text
            try:
                with open(args.output, 'a') as f:
                    f.write("\n\n" + bibtex)
                print(f"Added BibTeX entry to {args.output} using simple append")
            except Exception as e2:
                print(f"Error appending BibTeX: {e2}")
                return 1
    
    return 0

def extract_citations_from_md(file_path):
    """Extract potential citation identifiers from a Markdown file."""
    citation_patterns = [
        r'\[@([a-zA-Z0-9_-]+)(?:,|\])',  # Pandoc style [@citation]
        r'\[([a-zA-Z0-9_-]+)(?: |, |\])',  # Simple style [citation]
        r'(?:\s|^)\^([a-zA-Z0-9_-]+)(?:\s|$)',  # Footnote style ^citation
        r'(?:^|\s)([A-Z][a-zA-Z]*(?:,? (?:et al\.?|and others)?)?(?:, |\s\()(\d{4})(?:\)|\.)',  # Harvard style "Author (2020)"
    ]
    
    citations = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
            for pattern in citation_patterns:
                matches = re.finditer(pattern, content)
                for match in matches:
                    citations.append(match.group(1))
        
        # Remove duplicates while preserving order
        seen = set()
        unique_citations = [x for x in citations if not (x in seen or seen.add(x))]
        return unique_citations
    
    except Exception as e:
        print(f"Error extracting citations from {file_path}: {e}")
        return []

def extract_citations_from_tex(file_path):
    """Extract citation keys from a LaTeX file."""
    citation_patterns = [
        r'\\cite(?:\[.*?\])?{([^}]+)}',  # \cite{key} or \cite[p. 123]{key}
        r'\\citep(?:\[.*?\])?{([^}]+)}',  # \citep{key} or \citep[p. 123]{key}
        r'\\citet(?:\[.*?\])?{([^}]+)}',  # \citet{key} or \citet[p. 123]{key}
        r'\\citeauthor{([^}]+)}',        # \citeauthor{key}
        r'\\citeyear{([^}]+)}',          # \citeyear{key}
        r'\\textcite{([^}]+)}',          # \textcite{key}
        r'\\parencite{([^}]+)}',         # \parencite{key}
        r'\\autocite{([^}]+)}'           # \autocite{key}
    ]
    
    citations = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
            for pattern in citation_patterns:
                matches = re.finditer(pattern, content)
                for match in matches:
                    # Handle multiple keys separated by commas
                    keys = match.group(1).split(',')
                    for key in keys:
                        citations.append(key.strip())
        
        # Remove duplicates while preserving order
        seen = set()
        unique_citations = [x for x in citations if not (x in seen or seen.add(x))]
        return unique_citations
    
    except Exception as e:
        print(f"Error extracting citations from {file_path}: {e}")
        return []

def check_references(args):
    """Check references against existing BibTeX file."""
    # Load existing references
    existing_refs = load_references_from_file(args.bibtex_file)
    existing_keys = {ref['ID'] for ref in existing_refs}
    
    # Extract citations from all provided files
    all_citations = []
    for file_path in args.files:
        if file_path.endswith('.tex'):
            citations = extract_citations_from_tex(file_path)
        else:
            citations = extract_citations_from_md(file_path)
        
        all_citations.extend(citations)
        print(f"Found {len(citations)} citations in {file_path}")
    
    # Remove duplicates while preserving order
    seen = set()
    unique_citations = [x for x in all_citations if not (x in seen or seen.add(x))]
    
    # Check which citations are missing from references
    missing_citations = [cite for cite in unique_citations if cite not in existing_keys]
    
    print(f"\nFound {len(unique_citations)} unique citations across all files")
    print(f"Missing {len(missing_citations)} citations from references file")
    
    if missing_citations:
        print("\nMissing citations:")
        for cite in missing_citations:
            print(f"- {cite}")
    
    return 0

def extract_command(args):
    """Extract citation information from text files and create search queries."""
    all_citations = []
    
    # Extract citations from provided files
    for file_path in args.files:
        if file_path.endswith('.tex'):
            citations = extract_citations_from_tex(file_path)
        else:
            citations = extract_citations_from_md(file_path)
            
        all_citations.extend(citations)
        print(f"Found {len(citations)} citation keys in {file_path}")
    
    # Remove duplicates while preserving order
    seen = set()
    unique_citations = [x for x in all_citations if not (x in seen or seen.add(x))]
    
    # If reference pattern is provided, extract information about each citation
    if args.reference_pattern:
        citation_info = {}
        
        for file_path in args.files:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    
                    # Find all instances matching the reference pattern
                    matches = re.finditer(args.reference_pattern, content, re.MULTILINE)
                    for match in matches:
                        if len(match.groups()) >= 2:  # Need at least key and some info
                            key = match.group(1).strip()
                            info = match.group(2).strip()
                            citation_info[key] = info
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
        
        # Generate search queries for each citation
        print("\nSuggested search queries:")
        for cite_key in unique_citations:
            if cite_key in citation_info:
                print(f"[{cite_key}] python {sys.argv[0]} search --query \"{citation_info[cite_key]}\"")
            else:
                # Just use the key if we don't have info
                print(f"[{cite_key}] python {sys.argv[0]} search --query \"{cite_key}\"")
    else:
        print("\nFound citation keys (use with search command):")
        for cite_key in unique_citations:
            print(f"- {cite_key}")
    
    return 0

def main():
    parser = argparse.ArgumentParser(description='Reference management tool for academic papers')
    subparsers = parser.add_subparsers(dest='command', help='Command to run')
    
    # Search command
    search_parser = subparsers.add_parser('search', help='Search for papers on Google Scholar, Semantic Scholar, and CrossRef')
    search_parser.add_argument('--query', required=True, help='Search query')
    search_parser.add_argument('--num-results', type=int, default=5, help='Number of results to return')
    search_parser.add_argument('--no-save', action='store_true', help='Do not save results to temporary file')
    
    # Fetch command 
    fetch_parser = subparsers.add_parser('fetch', help='Fetch BibTeX for a specific result')
    fetch_parser.add_argument('--id', type=int, required=True, help='Result ID from search')
    fetch_parser.add_argument('--source', choices=['google_scholar', 'semantic_scholar', 'crossref'], 
                             help='Source of the result (google_scholar, semantic_scholar, crossref)')
    fetch_parser.add_argument('--identifier', help='Citation link (for Google Scholar), paper ID (for Semantic Scholar), or DOI (for CrossRef)')
    fetch_parser.add_argument('--output', help='BibTeX file to append the result to')
    fetch_parser.add_argument('--key', help='Custom citation key to use (overrides the default)')
    
    # Check references command
    check_parser = subparsers.add_parser('check', help='Check citations against existing references')
    check_parser.add_argument('--bibtex-file', required=True, help='BibTeX file with references')
    check_parser.add_argument('files', nargs='+', help='Files to check for citations')
    
    # Extract command
    extract_parser = subparsers.add_parser('extract', help='Extract citation information from text files')
    extract_parser.add_argument('files', nargs='+', help='Files to extract citation information from')
    extract_parser.add_argument('--reference-pattern', help='Regex pattern to extract citation information (should have 2 groups: key and info)')
    
    args = parser.parse_args()
    
    if args.command == 'search':
        return search_command(args)
    elif args.command == 'fetch':
        return fetch_bibtex_command(args)
    elif args.command == 'check':
        return check_references(args)
    elif args.command == 'extract':
        return extract_command(args)
    else:
        parser.print_help()
        return 1

if __name__ == '__main__':
    sys.exit(main())