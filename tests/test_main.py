"""
Unit-Tests für das CPRSW Probe Repository
"""

import sys
import os

# Füge das src-Verzeichnis zum Python-Path hinzu
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import gruss


def test_gruss():
    """Test der gruss-Funktion"""
    ergebnis = gruss("Test")
    assert "Hallo Test" in ergebnis
    assert "CPRSW" in ergebnis
    print("✓ test_gruss bestanden")


def test_gruss_mit_verschiedenen_namen():
    """Test der gruss-Funktion mit verschiedenen Namen"""
    namen = ["Alice", "Bob", "Charlie"]
    for name in namen:
        ergebnis = gruss(name)
        assert f"Hallo {name}" in ergebnis
    print("✓ test_gruss_mit_verschiedenen_namen bestanden")


if __name__ == "__main__":
    test_gruss()
    test_gruss_mit_verschiedenen_namen()
    print("\nAlle Tests erfolgreich!")
