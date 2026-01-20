#!/usr/bin/env python3
"""
Beispiel-Hauptprogramm für das CPRSW Probe Repository
"""

def gruss(name):
    """
    Gibt eine Begrüßung für den angegebenen Namen zurück.
    
    Args:
        name (str): Der Name der zu begrüßenden Person
        
    Returns:
        str: Die Begrüßungsnachricht
    """
    return f"Hallo {name}, willkommen zum CPRSW Probe Repository!"


def main():
    """
    Hauptfunktion des Programms
    """
    print(gruss("Finn"))
    print("Dieses Repository demonstriert grundlegende Programmierkonzepte.")


if __name__ == "__main__":
    main()
