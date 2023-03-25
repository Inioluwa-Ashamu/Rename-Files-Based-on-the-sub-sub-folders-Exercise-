from pathlib import Path

p1 = Path('files')
p2 = p1.glob('**/*')
for path in p2:
  if path.is_file():
    parent = list(path.parts)
    new_name = '-'.join(parent[1:3]) + path.name
    new_path = path.with_name(new_name)
    path.rename(new_path)