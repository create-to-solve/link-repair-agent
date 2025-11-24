# Copilot Instructions — Link Repair Agent

These instructions guide GitHub Copilot and AI coding agents when operating inside this repository.

---

## Project Purpose

This codebase implements a minimal link-resolution agent for UK open-data systems. It extracts candidate links from dataset landing pages, ranks and classifies them, profiles files, and records results in a JSONL registry.

The project must remain:

- Modular  
- Deterministic  
- Testable  
- Dependency-light  
- Aligned with the existing architecture  

---

## Architectural Boundaries

Maintain the following structure:

- `agent/` — orchestration logic  
- `strategies/` — functional components for fetch, parse, classify, profile  
- `models/` — Pydantic models and enums  
- `storage/` — caching + registry I/O  
- `config/` — global settings  
- `registry/` — YAML + JSONL registries  
- `scripts/` — CLI entrypoints  
- `tests/` — required for correctness  

---

## Rules for Copilot

### Must:
- Keep logic pure and modular  
- Add new strategies only under `strategies/`  
- Keep tests passing  
- Use relative imports  
- Maintain JSONL registry compatibility  

### Must Not:
- Introduce new top-level directories  
- Overwrite existing registry files without instruction  
- Replace synchronous code with async unless requested  
- Introduce heavy dependencies or frameworks  

---

## Testing Requirements

- All new logic must be covered by pytest  
- Existing tests must pass  
- No side effects at import time  

---

## Output Expectations

Generated code should:

- Follow PEP-8  
- Include docstrings on public functions  
- Remain consistent with existing module boundaries  

