# QECTOR Decoder Workbench

**Version 3.5.1** · Backend: `qector-decoder-v3==0.6.9`

Professional desktop application for quantum error correction research, evaluation, and documentation.

- 13 decoder algorithms
- 9 code families (surface, toric, heavy hex, bicycle qLDPC, and more)
- 47-tool Model Context Protocol (MCP) server for AI agents
- Portable Windows executable, Linux `.deb`, macOS `.dmg`
- Full GUI, command line, and headless MCP mode

**Website:** [qector.store](https://qector.store)
**Author:** Guillaume Lessard / iD01t Productions · ORCID: [0009-0000-3465-3753](https://orcid.org/0009-0000-3465-3753)

## 🚀 Support QECTOR Development

[![Sponsor qectorlab](https://img.shields.io/badge/Sponsor-qectorlab-ea4aaa?style=for-the-badge&logo=github)](https://github.com/sponsors/qectorlab)

[![Open Collective Banner](https://opencollective.com)](https://opencollective.com/qector-research-and-benchmark)


I am dedicated to building high-performance, production-ready Quantum Error Correction (QEC) software infrastructure designed for the next era of fault-tolerant computing.

My primary focus is the development of the QECTOR Decoder engine—a high-throughput decoding framework written in pure Rust and engineered for bare-metal performance, bypassing standard heap allocations and utilizing zero-allocation hot paths.

### Why Your Sponsorship Matters

Maintaining and engineering a deep-tech software stack requires extensive time, computational research, and hardware resources. Your sponsorship directly enables me to remain focused full-time on refining algorithms, expanding hardware compatibility, and keeping advanced quantum research utilities free for the global scientific community.

### 💻 Infrastructure & Hardware Requirements

Running continuous integration pipelines for high-distance qLDPC codes and massive syndrome defect datasets requires uninterrupted access to specialized hardware. Reaching $1,500 per month directly funds:

- Dedicated bare-metal GPU regression testing instances.
- Cloud cluster runtimes.
- Local hardware workshop infrastructure overhead.

This financial baseline ensures that every zero-allocation hot-path optimization is thoroughly benchmarked on enterprise-grade hardware before deployment. Whether you choose a monthly or one-time contribution, your support provides the essential runway needed to maintain this complex toolchain independently.

👉 **[Click here to sponsor iD01t Productions & QECTOR](https://github.com/sponsors/qectorlab)**

## Downloads

| Platform | File | Notes |
|---|---|---|
| Windows | `QectorWorkbench-Portable.exe` or `.zip` | Fully portable, no install required |
| Linux | `qector-workbench_3.5.1_amd64.deb` | Ubuntu 20.04+ / Debian 11+ |
| macOS | `QectorWorkbench-3.5.1.dmg` | macOS 12+ (Apple Silicon & Intel) |

👉 **[Download Latest Release](https://qector.store)**

## Quick Start

### Windows

1. Extract the zip (or run the portable `.exe` directly).
2. Double-click `QectorWorkbench-Portable.exe`.

### Linux

```bash
sudo apt install ./qector-workbench_3.5.1_amd64.deb
qector-workbench
```

### macOS

1. Mount the DMG and drag to Applications.

### MCP Server (AI Agents)

```bash
QectorWorkbench-Portable.exe --mcp          # Windows
qector-workbench --mcp                      # Linux / macOS
```

## Key Features

- **Interactive GUI:** Code Explorer, Decoder Lab, Benchmark Suite, Batch/Streaming, Diagnostics, Documentation Studio.
- **13 Decoders:** Includes exact Blossom MWPM, Union Find family, BP OSD, belief matching, auto router, hybrid cascade.
- **9 Code Families:** Graph-like and qLDPC.
- **Publication-Grade Charts:** Multi-format export (MD, JSON, HTML, LaTeX, PDF, SVG).
- **47-Tool MCP Server:** stdio JSON-RPC 2.0.
- **Automatic Provisioning:** Auto-fetches backend from PyPI on first run (subsequent runs fully offline).
- **Self-Healing Engine:** Built-in diagnostic and recovery routines.

## Licensing

- **Workbench (this application):** See `EULA.txt`. Royalty-free for any purpose (including commercial) as long as QECTOR notices are retained.
- **Backend (`qector-decoder-v3`):** Separately licensed. Free for personal, academic, and non-commercial research. Commercial use requires a paid license at [qector.store/pricing](https://qector.store/pricing).

## Documentation

Included in release packages:

- `README.txt` — Full package overview
- `EULA.txt` — End User License Agreement
- Platform user manuals (Windows / Linux / macOS)
- `QECTOR_API_Reference.md` / `.pdf`
- `QECTOR_MCP_Integration_Guide.pdf`
- `QECTOR_Quick_Start_Guide.pdf`
- `QECTOR_LLM_Manual.json` — Machine-readable agent guide

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
```

## Related

- **Core Library:** [GuillaumeLessard/qector-decoder](https://github.com/GuillaumeLessard/qector-decoder)
- **PyPI Package:** [qector-decoder-v3](https://pypi.org/project/qector-decoder-v3/)
- **Commercial Licensing:** [qector.store](https://qector.store)
