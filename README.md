# QECTOR Decoder Workbench

**Version 3.5.1** · Backend: qector-decoder-v3==0.6.9

Professional desktop application for quantum error correction research, evaluation, and documentation.

* 13 decoder algorithms
* 9 code families (surface, toric, heavy hex, bicycle qLDPC, and more)
* 47 tool Model Context Protocol (MCP) server for AI agents
* Portable Windows executable, Linux .deb, macOS .dmg
* Full GUI, command line, and headless MCP mode

**Website**: https://www.qector.store
**Author**: Guillaume Lessard / iD01t Productions · ORCID 0009-0000-3465-3753

## Downloads

| Platform | File | Notes |
|----------|------|-------|
| **Windows** | `QectorWorkbench-Portable.exe` or `.zip` | Fully portable, no install required |
| **Linux** | `qector-workbench_3.5.1_amd64.deb` | Ubuntu 20.04+ / Debian 11+ |
| **macOS** | `QectorWorkbench-3.5.1.dmg` | macOS 12+ (Apple Silicon & Intel) |

**[Latest Release](https://github.com/GuillaumeLessard/qector-workbench/releases/latest)**


## Quick Start

**Windows**

1. Extract the zip (or run the portable `.exe` directly)
2. Double click `QectorWorkbench-Portable.exe`

**Linux**

```bash
sudo apt install ./qector-workbench_3.5.1_amd64.deb
qector-workbench
```

**macOS**

Mount the DMG and drag to Applications.

**MCP Server (AI agents)**

```bash
QectorWorkbench-Portable.exe --mcp          # Windows
qector-workbench --mcp                      # Linux / macOS
```

## Key Features

* Interactive GUI (Code Explorer, Decoder Lab, Benchmark Suite, Batch/Streaming, Diagnostics, Documentation Studio)
* 13 decoders including exact Blossom MWPM, Union Find family, BP OSD, belief matching, auto router, hybrid cascade
* 9 code families (graph like and qLDPC)
* Publication grade charts and multi format export (MD, JSON, HTML, LaTeX, PDF, SVG)
* 47 tool MCP server (stdio JSON RPC 2.0)
* Automatic backend provisioning from PyPI on first run (subsequent runs fully offline)
* Self healing decoder engine

## Licensing

**Workbench (this application)** — see `EULA.txt`
Royalty free for any purpose (including commercial) as long as QECTOR notices are retained.

**Backend (qector-decoder-v3)** — separately licensed
Free for personal, academic, and non commercial research.
Commercial use requires a paid license: qector.store/pricing

## Documentation

Included in releases:

* `README.txt`. Full package overview
* `EULA.txt`. End User License Agreement
* Platform user manuals (Windows / Linux / macOS)
* `QECTOR_API_Reference.md` / `.pdf`
* `QECTOR_MCP_Integration_Guide.pdf`
* `QECTOR_Quick_Start_Guide.pdf`
* `QECTOR_LLM_Manual.json`. Machine readable agent guide

## Citation

```bibtex
@software{lessard2026qector,
  author  = {Guillaume Lessard},
  title   = {{QECTOR Decoder v3}: Rust/Python Quantum Error Correction Decoding Platform},
  year    = {2026},
  version = {0.6.9},
  url     = {https://www.qector.store},
  orcid   = {0009-0000-3465-3753}
}


## Related

* Core library: GuillaumeLessard/qector-decoder
* PyPI: qector-decoder-v3
* Website & commercial licensing: qector.store
