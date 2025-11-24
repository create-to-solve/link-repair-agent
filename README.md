# Link Repair Agent

A lightweight, modular Python agent designed to discover, classify, and validate data file links from UK open-data landing pages. This repository provides the minimal viable architecture for a link-resolution subsystem that can be embedded into larger evidence-pipeline systems.

---

## Overview

UK open-data portals often publish datasets through landing pages rather than direct file links. The Link Repair Agent automates three core tasks:

1. Fetch landing page HTML  
2. Extract all candidate links  
3. Rank, classify, and select the most appropriate file (CSV, XLSX, ZIP, etc.)  
4. Optionally profile tabular files by sampling columns  
5. Save structured results in a JSONL registry

This creates a machine-trusted, programmatically usable registry of resolved dataset URLs.

---

## Repository Structure

agent/                 # Main agent implementation  
config/                # Runtime configuration (timeouts, settings)  
models/                # Pydantic models and enums  
registry/              # Raw and resolved dataset registries  
scripts/               # CLI utilities  
storage/               # Registry I/O, caching layer  
strategies/            # Fetching, parsing, classification, selection, profiling  
tests/                 # Pytest unit tests  
logs/                  # Log directory (placeholder)

---

## Usage

Install dependencies:

    pip install -r requirements.txt

Run the resolver:

    python scripts/run_resolver.py

Inspect resolved sources:

    python scripts/inspect_resolved.py

Run tests:

    pytest

---

## Extending the Agent

Future enhancements may include:

- CKAN API discovery  
- Automatic schema inference  
- Multi-page crawling for complex landing pages  
- Integration into broader data harmonisation pipelines  
- Streaming ingest into cloud storage layers  

---

## License

See `LICENSE` for details.
