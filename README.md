# Projekt 6 – Automatizované UI testy pro Engeto.cz

Tento repozitář obsahuje **ukázkovou Python aplikaci**, která využívá framework **Playwright** pro testování webové stránky [https://engeto.cz](https://engeto.cz). Projekt slouží jako cvičný a studijní materiál k nácviku:

- psaní **automatizovaných UI testů**,
- práce s knihovnou `pytest` a `playwright`,
- validace vstupů a externích odkazů,
- základní testovací architektura.

## 🔍 Co se testuje

✅ **Validace e-mailu** při odběru newsletteru  
✅ **Reakce na duplicitní e-mail**  
✅ **Odkazy na sociální sítě** (Facebook, YouTube, Instagram, LinkedIn, Discord)

## 📁 Struktura projektu

```
projekt6/
├── tests/               # testovací skripty (Playwright + Pytest)
├── .gitignore
├── requirements.txt     # seznam závislostí
```

## 💻 Požadavky

- Python 3.7+
- Nainstalovaný Playwright a jeho závislosti

Instalace závislostí:

```bash
pip install -r requirements.txt
playwright install
```

## 🚀 Spuštění testů

```bash
pytest
```

## 🛠 Použité technologie

- [Playwright](https://playwright.dev/python/)
- [Pytest](https://docs.pytest.org/)
- [Python](https://www.python.org/)

## ✍️ Autor

**Kryštof Klika**  
