import os
import re
import glob

# Step 1: Parse scopus.txt to extract DOI -> abstract mapping
scopus_path = os.path.join(os.path.dirname(__file__), 'scopus.txt')
with open(scopus_path, 'r', encoding='utf-8-sig') as f:
    scopus_content = f.read()

# Parse entries: URL line (with DOI) followed by blank line, then 摘要: line
entries = re.split(r'\n(?=https://www\.scopus\.com)', scopus_content)
doi_to_abstract = {}

for entry in entries:
    entry = entry.strip()
    if not entry:
        continue
    
    # Extract DOI from URL
    doi_match = re.search(r'doi=([^&]+)', entry)
    if not doi_match:
        continue
    
    doi_raw = doi_match.group(1)
    # URL-decode the DOI
    doi = doi_raw.replace('%2f', '/').replace('%2F', '/').replace('%3a', ':').replace('%3A', ':').replace('%28', '(').replace('%29', ')').replace('%20', ' ')
    
    # Extract abstract
    abstract_match = re.search(r'摘要:\s*(.*)', entry, re.DOTALL)
    if abstract_match:
        abstract = abstract_match.group(1).strip()
        # Remove trailing copyright markers
        abstract = re.sub(r'\s*©.*$', '', abstract)
        abstract = re.sub(r'\s*Copyright.*$', '', abstract)
        doi_to_abstract[doi] = abstract

print(f"Parsed {len(doi_to_abstract)} abstracts from scopus.txt")

# Step 2: Match each publication and add abstract
pub_dir = os.path.join(os.path.dirname(__file__), '_publications')
pub_files = sorted(glob.glob(os.path.join(pub_dir, '*.md')))

matched = 0
unmatched = []

for pub_file in pub_files:
    with open(pub_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract paperurl (DOI)
    paperurl_match = re.search(r'paperurl:\s*["\']?(https?://doi\.org/([^\s"\']+))["\']?', content)
    if not paperurl_match:
        # Try alternate format without https
        paperurl_match = re.search(r'paperurl:\s*["\']?(doi:\s*([^\s"\']+))["\']?', content)
        if not paperurl_match:
            unmatched.append(os.path.basename(pub_file) + ' (no paperurl)')
            continue
        doi = paperurl_match.group(2).strip()
    else:
        doi = paperurl_match.group(2)
    
    # Remove the doi.org/ prefix if present
    if doi.startswith('doi.org/'):
        doi = doi[8:]
    elif doi.startswith('https://doi.org/'):
        doi = doi[16:]
    
    # Check if we have this DOI's abstract
    matched_abstract = None
    if doi in doi_to_abstract:
        matched_abstract = doi_to_abstract[doi]
    
    if not matched_abstract:
        # Try URL-decoded version in keys
        for k in doi_to_abstract:
            if k.replace('%2F', '/').replace('%2f', '/').replace('%3A', ':').replace('%3a', ':') == doi:
                matched_abstract = doi_to_abstract[k]
                break
    
    if not matched_abstract:
        # Try the raw key lookup (our scopus parser already decoded)
        for k in doi_to_abstract:
            if k == doi:
                matched_abstract = doi_to_abstract[k]
                break
    
    if not matched_abstract:
        # Debug: show similar keys
        similar = [k for k in doi_to_abstract if doi.split('/')[0] in k]
        if similar:
            matched_abstract = doi_to_abstract[similar[0]]
            print(f"  [MATCHED by prefix] {os.path.basename(pub_file)}: {doi} -> {similar[0]}")
        else:
            unmatched.append(os.path.basename(pub_file) + ' DOI:' + doi)
            continue
    
    abstract = matched_abstract
    
    # Remove old body content (everything after front matter)
    # Find the closing --- of front matter
    fm_end = content.find('\n---', content.find('---') + 3)
    if fm_end == -1:
        unmatched.append(os.path.basename(pub_file) + ' (no front matter end)')
        continue
    
    # Check if there's existing body content
    existing_body = content[fm_end + 4:].strip()
    
    # Build new content: front matter + blank line + abstract
    new_content = content[:fm_end + 4] + '\n' + abstract + '\n'
    
    with open(pub_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    matched += 1
    print(f"  ✓ {os.path.basename(pub_file)}: {doi[:60]}... ({len(abstract)} chars)")

print(f"\nMatched: {matched}/{len(pub_files)}")
if unmatched:
    print(f"Unmatched ({len(unmatched)}):")
    for u in unmatched:
        print(f"  ✗ {u}")
