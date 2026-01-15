import pandas as pd
from io import StringIO
import re
import argparse
import sys

def parse_markdown_tables(markdown_content):
    """
    Parses all markdown tables from a string and returns them as a list of pandas DataFrames.
    """
    # Find all markdown tables
    table_pattern = re.compile(r'|.*?\n|[-|: ]+|(|.*?\n)*', re.MULTILINE)
    tables_str = table_pattern.findall(markdown_content)
    
    dataframes = []
    for table_match in tables_str:
        # The first part of the tuple is the full match
        table_str = ''.join(table_match)
        # Use StringIO to treat the string as a file for pandas
        table_io = StringIO(table_str)
        try:
            # Read the table, using the first row as header
            df = pd.read_csv(table_io, sep='|', header=0).dropna(axis=1, how='all').iloc[1:]
            # Strip whitespace from column headers and data
            df.columns = [col.strip() for col in df.columns]
            for col in df.columns:
                df[col] = df[col].str.strip()
            dataframes.append(df)
        except Exception as e:
            # Silently ignore tables that can't be parsed (like the header separator)
            pass
            
    return dataframes

def generate_mermaid_graph(dataframes):
    """
    Generates a Mermaid graph syntax from a list of pandas DataFrames.
    """
    if not dataframes:
        return ""

    mermaid_str = "graph TD\n"
    
    # Use a set to avoid duplicate nodes
    nodes = set()
    edges = []

    for df in dataframes:
        if df.shape[1] < 3:
            continue

        # Assumes the first three columns are [Source, Target, Relationship]
        source_col = df.columns[0]
        target_col = df.columns[1]
        relation_col = df.columns[2]

        for _, row in df.iterrows():
            source = row[source_col]
            target = row[target_col]
            relation = row[relation_col]
            
            if pd.isna(source) or pd.isna(target) or pd.isna(relation):
                continue

            # Clean names for use as Mermaid node IDs
            source_id = re.sub(r'\W+', '_', source)
            target_id = re.sub(r'\W+', '_', target)

            if source not in nodes:
                mermaid_str += f'    {source_id}["{source}"]\n'
                nodes.add(source)
            if target not in nodes:
                mermaid_str += f'    {target_id}["{target}"]\n'
                nodes.add(target)
            
            edges.append(f'    {source_id} -- "{relation}" --> {target_id}')

    mermaid_str += "\n".join(edges)
    return mermaid_str

def main():
    """
    Main function to execute the script from the command line.
    """
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate a Mermaid graph from relationship tables in a markdown file.")
    parser.add_argument("file_path", type=str, help="The path to the markdown file.")
    
    # Add a quiet flag
    parser.add_argument("-q", "--quiet", action="store_true", help="Suppress error messages.")

    args = parser.parse_args()

    try:
        with open(args.file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        if not args.quiet:
            print(f"Error: File not found at {args.file_path}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        if not args.quiet:
            print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)

    # 1. Parse tables
    all_dataframes = parse_markdown_tables(content)
    
    # 2. Generate Mermaid graph
    mermaid_code = generate_mermaid_graph(all_dataframes)
    
    # 3. Print the output
    if mermaid_code:
        print("```mermaid")
        print(mermaid_code)
        print("```")
    else:
        if not args.quiet:
            print("No valid relationship tables found to generate a graph.", file=sys.stderr)
        sys.exit(0) # Exit gracefully if no tables are found


if __name__ == "__main__":
    main()