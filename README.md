# Sudoku GUI

Dette prosjektet er et grafisk Sudoku-spill laget i Python med tkinter. Du kan fylle ut Sudoku-brettet, få forslag til løsninger, og sjekke om løsningen din er korrekt.

## Funksjoner
- Genererer tilfeldige Sudoku-brett
- Løser Sudoku automatisk
- Sjekker om brukerens løsning er korrekt
- Flere vanskelighetsgrader ("Lett", "Medium" og "Expert")
- GUI laget med tkinter

## Kom i gang

### Krav
- Python 3.x
- tkinter (følger vanligvis med Python)

### Kjør spillet

Åpne terminalen i prosjektmappen og kjør:

```powershell
python Soduko/sodukobrett.py
```

### Bygg som .exe (valgfritt)
1. Installer PyInstaller:
   ```powershell
   pip install pyinstaller
   ```
2. Bygg .exe:
   ```powershell
   pyinstaller --onefile --windowed Soduko/sodukobrett.py
   ```
   Den ferdige filen finner du i `dist`-mappen.

## Bidra
Pull requests er velkomne!

## Lisens
Dette prosjektet er åpent og fritt til privat bruk.

## Utvikler
Michael Haug
