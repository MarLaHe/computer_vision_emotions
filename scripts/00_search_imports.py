import os
import json
import re
import sys

# Liste der Standardbibliotheks-Module
standard_libs = {
    'abc', 'argparse', 'array', 'asyncio', 'base64', 'binascii', 'bisect', 'builtins', 'calendar',
    'collections', 'concurrent', 'contextlib', 'copy', 'csv', 'ctypes', 'datetime', 'decimal', 'difflib',
    'email', 'enum', 'errno', 'faulthandler', 'fnmatch', 'fractions', 'functools', 'gc', 'getopt', 'getpass',
    'gettext', 'glob', 'gzip', 'hashlib', 'heapq', 'hmac', 'html', 'http', 'imaplib', 'importlib', 'inspect',
    'io', 'ipaddress', 'itertools', 'json', 'keyword', 'linecache', 'locale', 'logging', 'lzma', 'math',
    'mimetypes', 'multiprocessing', 'numbers', 'operator', 'os', 'pathlib', 'pickle', 'platform', 'plistlib',
    'pprint', 'profile', 'pstats', 'queue', 'random', 're', 'sched', 'secrets', 'select', 'selectors', 'shlex',
    'shutil', 'signal', 'site', 'socket', 'sqlite3', 'ssl', 'stat', 'statistics', 'string', 'struct', 'subprocess',
    'sys', 'tempfile', 'textwrap', 'threading', 'time', 'timeit', 'traceback', 'types', 'typing', 'unittest',
    'urllib', 'uuid', 'warnings', 'wave', 'weakref', 'webbrowser', 'xml', 'zipfile', 'zoneinfo'
}

# Map von Modulname zu PyPI-Paketname (wenn unterschiedlich)
package_aliases = {
    'PIL': 'pillow',
    'sklearn': 'scikit-learn'
}

def extract_imports_from_ipynb(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    imports = set()
    for cell in notebook.get('cells', []):
        if cell.get('cell_type') == 'code':
            for line in cell.get('source', []):
                match_import = re.match(r'^\s*import (\S+)', line)
                match_from = re.match(r'^\s*from (\S+)', line)
                if match_import:
                    module = match_import.group(1).split('.')[0]
                    imports.add(module)
                elif match_from:
                    module = match_from.group(1).split('.')[0]
                    imports.add(module)
    return imports

def clean_imports(imports):
    cleaned = set()
    for imp in imports:
        if imp in standard_libs:
            continue  # Überspringe Standardbibliothek
        cleaned.add(package_aliases.get(imp, imp))  # Ersetze Alias, falls vorhanden
    return cleaned

def collect_all_imports():
    all_imports = set()
    for file in os.listdir('.'):
        if file.endswith('.ipynb'):
            print(f"Verarbeite: {file}")
            all_imports.update(extract_imports_from_ipynb(file))
    return all_imports

def write_requirements(imports, output_file='requirements.txt'):
    with open(output_file, 'w', encoding='utf-8') as f:
        for package in sorted(imports):
            f.write(f"{package}\n")
    print(f"\nrequirements.txt wurde erstellt mit {len(imports)} Paketen.")

if __name__ == "__main__":
    raw_imports = collect_all_imports()
    cleaned_imports = clean_imports(raw_imports)
    write_requirements(cleaned_imports)

