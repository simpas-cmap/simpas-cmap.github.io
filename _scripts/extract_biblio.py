import requests
import time

# 1. ADD YOUR TEAM IDS HERE
# You can find these in the URL of their HAL profile (e.g., Paul Mangold = 1348236)
author_ids = [
    "1377304",  # Stefano De Marco
    "1259955", # Erwan Le Pennec
    "1028753", # Josselin Garnier
    "751536", # Karim Lounici
    "1109167", # Aymeric Dieuleveut
    "22", # Rémi Flamary
    "1084098", # Alain Durmus
    "995608", # Clément Rey
    "1329830", # El Mahdi El Mhamdi
    "751506",
    "969831", # Gauthier Vermandel
 #    "", # Luiz Chamon (not found on hal)
    "1082246", # Solenne Gaucher
    "1186842", # Clément Bonet
    "1348236"  # Paul Mangold
]

def fetch_bibtex(author_id):
    """Fetches BibTeX entries from HAL for a specific author ID."""
    base_url = "https://api.archives-ouvertes.fr/search/"
    params = {
        "q": f"authIdPerson_i:{author_id}",
        "wt": "bibtex",
        "rows": 1000  # Adjust if an author has > 1000 papers
    }
    
    print(f"Fetching publications for ID: {author_id}...")
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {author_id}: {e}")
        return ""

def main():
    all_entries = {}
    
    for auth_id in author_ids:
        bib_data = fetch_bibtex(auth_id)
        
        # Split by the '@' symbol to separate BibTeX entries
        entries = bib_data.split('\n@')
        
        for entry in entries:
            if not entry.strip():
                continue
            
            # Re-add the '@' if it was removed by split
            full_entry = entry if entry.startswith('@') else '@' + entry
            
            # Use the BibTeX key (e.g., @article{key, ...) as a unique identifier for deduplication
            try:
                key = full_entry.split('{', 1)[1].split(',', 1)[0].strip()
                if key not in all_entries:
                    all_entries[key] = full_entry
            except IndexError:
                continue
        
        # Small delay to be polite to the API
        time.sleep(0.5)

    # Write to file
    with open("_bibliography/papers.bib", "w", encoding="utf-8") as f:
        f.write("\n\n".join(all_entries.values()))
    
    print(f"\nSuccess! Generated papers.bib with {len(all_entries)} unique entries.")

if __name__ == "__main__":
    main()
