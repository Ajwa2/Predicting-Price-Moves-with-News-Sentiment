from nbformat import read, write
from nbclient import NotebookClient
from pathlib import Path
import sys

def main():
    if len(sys.argv) < 2:
        print('Usage: run_notebook_path.py <notebook_path>')
        sys.exit(2)
    p = Path(sys.argv[1])
    if not p.exists():
        print('Notebook not found:', p)
        sys.exit(2)
    print('Reading', p)
    nb = read(str(p), as_version=4)
    client = NotebookClient(nb, timeout=1800, kernel_name='python3')
    print('Executing notebook...')
    client.execute()
    out = p.parent / (p.stem + '_executed.ipynb')
    print('Writing executed notebook to', out)
    write(nb, str(out))
    print('Done. Wrote', out)

if __name__ == '__main__':
    main()
