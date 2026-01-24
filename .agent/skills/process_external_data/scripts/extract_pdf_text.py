import sys
import argparse
import logging

# Suppress pdfminer internal warnings (like FontBBox errors) that clutter the output
logging.getLogger("pdfminer").setLevel(logging.ERROR)

import pdfplumber

def extract_text_from_pdf(pdf_path, start_page=None, end_page=None):
    """
    Extracts text from a PDF file within a given page range.
    """
    try:
        with pdfplumber.open(pdf_path) as pdf:
            total_pages = len(pdf.pages)
            
            start_index = 0
            if start_page:
                start_index = max(0, start_page - 1)
                
            end_index = total_pages
            if end_page:
                end_index = min(total_pages, end_page)

            print(f"--- Processing {pdf_path} (Pages {start_index+1}-{end_index}) ---")

            for i in range(start_index, end_index):
                page = pdf.pages[i]
                text = page.extract_text()
                print(f"\n--- Page {i+1} ---\n")
                if text:
                    print(text)
                else:
                    print("(No text found on this page)")
                    
    except Exception as e:
        print(f"Error extracting text: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract text from PDF.")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("--start_page", type=int, help="Starting page number (1-indexed)")
    parser.add_argument("--end_page", type=int, help="Ending page number (1-indexed)")
    parser.add_argument("--search", type=str, help="Keyword to search for in the PDF")

    args = parser.parse_args()
    
    # Set stdout to utf-8 to handle special characters on Windows
    sys.stdout.reconfigure(encoding='utf-8')
    
    if args.search:
        try:
            with pdfplumber.open(args.pdf_path) as pdf:
                print(f"--- Searching for '{args.search}' in {args.pdf_path} ---")
                found = False
                for i, page in enumerate(pdf.pages):
                    text = page.extract_text()
                    if text and args.search.lower() in text.lower():
                        print(f"Found '{args.search}' on Page {i+1}")
                        found = True
                        # Optional: Print snippet? For now just page number is enough to locate.
                if not found:
                    print(f"'{args.search}' not found.")
        except Exception as e:
            print(f"Error searching PDF: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        extract_text_from_pdf(args.pdf_path, args.start_page, args.end_page)
