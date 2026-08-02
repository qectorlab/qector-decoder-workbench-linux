# QECTOR Decoder Workbench

**Windows build · v0.5.2** - Backend: `qector-decoder-v3` **v0.7.0**

Professional quantum error-correction analysis platform built on `qector_decoder_v3` (compiled Rust core + public Python layer). Features 16 decoders, 10 code families (including qLDPC and color codes), batch/streaming decode, hardware detection, a resilient self/auto-debug backend, a 56-tool MCP server, and multi-format documentation export.

[![License](https://img.shields.io/badge/license-source--available-blue)](EULA.txt)
[![Backend](https://img.shields.io/badge/backend-qector--decoder--v3%200.7.0-informational)](https://pypi.org/project/qector-decoder-v3/0.7.0/)

A professional desktop application for quantum error correction (QEC) research, decoder evaluation, and reproducible benchmarking, running fully offline on Windows.

## Table of Contents

- [Overview](#overview)
- [Download & Quick Start](#download--quick-start)
- [System Requirements](#system-requirements)
- [Features](#features)
- [License](#license)
- [Citation](#citation)
- [Related](#related)

## Overview

The Windows portable build bundles its own Python runtime, the scientific stack, **and** the `qector_decoder_v3` wheel. It runs with no external Python, pip, or internet connection: on first launch the bundled decoder wheel is activated into a per-user managed site automatically. No online update checks are performed — the app runs entirely from what ships in the box.

> **Honest posture (from the upstream QECTOR Decoder v3 manual):** every LER/throughput/latency figure is hardware-, driver-, seed-, and workload-dependent simulation — regenerate before quoting. PyMatching is the speed leader on standard surface-code MWPM; QECTOR's exact `BlossomDecoder` reaches its logical error rate but is not faster. Every decoder always satisfies `H·c == s (mod 2)`. This is a research/evaluation platform, not a real-time or fault-tolerant hardware decoder.

## Download & Quick Start

👉 **Download the latest release from this repository's [Releases page](../../releases/latest).**

1. Download `QectorWorkbench-Portable.exe`.
2. Double-click to launch. No installation, no admin rights, no internet connection required.

For the headless MCP server:

```
QectorWorkbench-Portable.exe --mcp     # 56-tool stdio MCP server (no display needed)
```

Runtime data (logs, exported documents) is written to your per-user data directory (`%LOCALAPPDATA%\QectorWorkbench`; override with `QECTOR_DATA_DIR`).

## System Requirements

| Requirement | Detail |
|---|---|
| OS | Windows 10 (64-bit) or later |
| Disk space | Sufficient for the bundled Python runtime, scientific stack, and decoder wheel (portable, single executable) |
| Internet | Not required — the backend is provisioned entirely from the bundled wheel on first launch |
| GPU (optional) | CUDA-capable NVIDIA GPU for accelerated batch decode; CPU-only operation is fully supported |

## Features

### Code Explorer

Build codes from 10 families with configurable distance/parameter. Live properties display including qubits, checks, and code rate, plus a clean bipartite Tanner-graph view.

- **Graphlike / topological:** repetition, ring, rotated_surface, unrotated_surface, toric, heavy_hex, and `hypergraph_product` (a CSS code built from a repetition-code seed — graphlike, so all matching decoders apply).
- **qLDPC:** `bicycle` (parameter = circulant size) and `bivariate_bicycle` (the IBM BB code family — e.g. the [[72,12,6]] "gross" code — selected from verified presets). qLDPC codes are non-graphlike: use `bp_osd`, `blossom`, `hybrid`, or `auto_router` (the Diagnostics tab's resilient decode auto-falls-back to a compatible decoder).
- **Color codes:** `color_code` (triangular & 2D), decoded with the native colour-code decoder.

### Decoder Lab

Test any of 16 decoders with configurable error rate and seed. View error, syndrome, and correction arrays. Every decoder is verified to satisfy `H·c == s (mod 2)`. A **Clear Decoder Cache** button frees cached decoder instances between experiments.

| Decoder | Notes |
|---|---|
| `union_find` / `fast_union_find` | Fast approximate decode; higher LER than exact MWPM (throughput lever). |
| `blossom` | Weight-optimal exact MWPM; matches PyMatching's LER but is not faster. |
| `sparse_blossom` | Region-growing, near-optimal (experimental); **not exact**. |
| `sparse_blossom_radix_neighbors` | Radix-neighbor variant of the region-growing decoder. |
| `bp_osd` | Belief propagation + ordered statistics for LDPC / quantum-LDPC codes; tunable via `bp_method` (exact\|min_sum) and `osd_order` (0\|1\|2). |
| `auto` | Self-selecting decoder: picks the best available backend per problem size. |
| `hybrid` | Combines a fast heuristic pass with exact matching; trainable weights. |
| `lookup_table` | Precomputed syndrome→correction table with O(1) lookup (refused above 20 checks). |
| `predecoded` | Resolves easy/low-weight syndromes in a fast pre-decoding pass before matching. |
| `auto_router` | Policy decoder: inspects the code and dispatches the best concrete decoder — matching for graphlike codes, bp_osd for qLDPC. Universally compatible, including on `bivariate_bicycle`. |
| `hybrid_cascade` | Union-Find pre-filter with Blossom/BP-OSD escalation; exposes live cascade statistics. Graphlike codes only. |
| `gnn_belief_matching` | GNN-predicted per-qubit weights guide a weighted matching decode, with a faithfulness fallback to plain MWPM. Graphlike codes. |
| `belief_matching` | Sum-product BP posteriors reweight an exact Blossom matching step; faithfulness-checked with MWPM fallback. |
| `two_stage` | Two-stage decode pipeline (fast stage + exact escalation). |
| `ambiguity_cluster` | Ambiguity-clustering decoder for degenerate syndrome structure. |
| `colour_code` | Native color-code decoder (restricted to true color-code topologies). |

### Benchmark Suite

Run configurable benchmarks with throughput/latency metrics. Export results to JSON.

### Batch & Streaming

Batch decode multiple error samples with success rate. Sliding-window streaming session controls.

### Hardware Dashboard

Auto-detect CUDA, OpenCL, and CPU backends. System info with CPU/RAM utilization and hardware-optimized decoder recommendations. Note: the standard backend ships a CUDA path but no OpenCL kernels, so OpenCL reports unavailable unless the backend was built from source with the `opencl` feature.

### Diagnostics (Self / Auto-Debug)

- **Run Self-Diagnostics** — environment/decoder/hardware self-test with per-check pass/warn/fail status.
- **Probe Decoders** — reports which decoders produce a valid (syndrome-verified) correction for the current code.
- **Resilient Decode** — decodes with an automatic multi-decoder fallback chain (verifying `H·c == s` at each step) and shows the full attempt trace.

### Documentation Studio

Export professional documentation in Markdown, HTML, JSON, LaTeX, PDF (matplotlib multi-page) and SVG (standalone Tanner graph) with full provenance metadata.

### MCP Server

56-tool Model Context Protocol server (stdio JSON-RPC 2.0) for programmatic access — including `self_diagnostics`, `probe_decoders`, `resilient_decode`, `version_info`, `diagnostic_decode`, `native_recommend`, `native_streaming`, `list_codes`, `compat_report`, hybrid-cascade stats, neural pre-decoder training, and decoder-option-aware decode tools. Every tool is wired to the real decoder backend, not a mock or stub.

### Offline Versioning

- The window title and status bar show the workbench version (v0.5.2) and the installed decoder backend version (qector-decoder-v3 v0.7.0).
- No PyPI queries, no auto-updater: the shipped bundle is the single source of truth.

## License

**Workbench:** source-available — see EULA (free use including commercial, with QECTOR watermark retention per EULA §2).

**Backend `qector-decoder-v3`:** separately licensed by Guillaume Lessard / iD01t Productions — free for personal/academic/non-commercial research; commercial use requires a paid commercial license (www.qector.store, admin@qector.store). Honor the backend license for any commercial deployment.

## Citation

```bibtex
@software{lessard2026qectorworkbench,
  author  = {Guillaume Lessard},
  title   = {{QECTOR Decoder Workbench}: Windows Desktop Application for Quantum Error Correction Analysis},
  year    = {2026},
  version = {0.5.2},
  url     = {https://github.com/qectorlab/qector-decoder-workbench-windows},
  orcid   = {0009-0000-3465-3753}
}
```

## Related

- **PyPI Package:** [qector-decoder-v3 0.7.0](https://pypi.org/project/qector-decoder-v3/0.7.0/)
- **Core Library:** [GuillaumeLessard/qector-decoder](https://github.com/GuillaumeLessard/qector-decoder)
- **Commercial Licensing:** [qector.store](https://qector.store)

Author: Guillaume Lessard / iD01t Productions · ORCID [0009-0000-3465-3753](https://orcid.org/0009-0000-3465-3753) · [www.qector.store](https://www.qector.store)
