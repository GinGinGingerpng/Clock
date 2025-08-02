from pathlib import Path
p = Path(r"C:\Users\oreor\OneDrive\Documents\clock\clock\taiyo.png").resolve()
print(p)
print(p.relative_to(Path.cwd()))