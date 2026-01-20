# Dokumentation

## Übersicht

Dieses Dokument beschreibt die Struktur und Verwendung des CPRSW Probe Repositories.

## Funktionen

### gruss(name)

Die `gruss`-Funktion nimmt einen Namen als Parameter und gibt eine personalisierte Begrüßungsnachricht zurück.

**Parameter:**
- `name` (str): Der Name der zu begrüßenden Person

**Rückgabewert:**
- `str`: Eine formatierte Begrüßungsnachricht

**Beispiel:**
```python
from main import gruss

nachricht = gruss("Finn")
print(nachricht)  # Ausgabe: Hallo Finn, willkommen zum CPRSW Probe Repository!
```

## Tests ausführen

Um die Tests auszuführen, navigieren Sie zum Repository-Verzeichnis und führen Sie aus:

```bash
python tests/test_main.py
```

## Hauptprogramm ausführen

Um das Hauptprogramm auszuführen:

```bash
python src/main.py
```
