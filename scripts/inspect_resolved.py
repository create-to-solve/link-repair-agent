from storage.registry_io import iter_resolved_sources

if __name__ == "__main__":
    for r in iter_resolved_sources():
        print(r.model_dump())
