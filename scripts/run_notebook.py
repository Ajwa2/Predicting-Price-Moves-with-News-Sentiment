from nbformat import read, write
from nbclient import NotebookClient
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
nb_path = ROOT / 'notebooks' / 'Quant_task2.ipynb'
out_path = ROOT / 'notebooks' / 'Quant_task2_executed_nbclient.ipynb'

print('Reading', nb_path)
nb = read(str(nb_path), as_version=4)
client = NotebookClient(nb, timeout=600, kernel_name='python3')
print('Executing notebook...')
client.execute()
print('Writing executed notebook to', out_path)
write(nb, str(out_path))
print('Done')
