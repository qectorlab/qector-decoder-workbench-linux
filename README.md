# QECTOR Decoder Workbench

Official desktop application (Windows / Linux / macOS) for the **QECTOR Decoder v3** quantum error-correction platform.

**Python package**: [qector-decoder-v3 on PyPI](https://pypi.org/project/qector-decoder-v3/)  
**Website**: [https://www.qector.store](https://www.qector.store)  
**Author**: Guillaume Lessard (iD01t Productions) · ORCID: [0009-0000-3465-3753](https://orcid.org/0009-0000-3465-3753)

---

## Downloads

| Platform | File | Notes |
|----------|------|-------|
| Windows  | `QECTOR-Workbench-x.y.z-windows-x64.exe` or portable zip | Recommended: portable version |
| Linux    | `QECTOR-Workbench-x.y.z-linux-x86_64.AppImage` | Make executable: `chmod +x *.AppImage` |
| macOS    | `QECTOR-Workbench-x.y.z-macos-arm64.dmg` (or Intel) | — |

**Latest release**: [Releases page](https://github.com/GuillaumeLessard/qector-workbench/releases/latest)

Always verify the SHA-256 checksums published with each release.

---

## Features

- Graphical interface for decoder selection, code generation, and batch runs
- Integration with the `qector-decoder-v3` Python package
- Benchmark orchestration (Workbench harness)
- Stim / Sinter compatible workflows
- Offline license token support (Ed25519)

---

## Licensing

Source-available.

- **Free**: personal, academic, educational, and non-commercial research use
- **Commercial license required** for company use, commercial R&D, SaaS, OEM embedding, or revenue-linked work

Contact: [admin@qector.store](mailto:admin@qector.store)

---

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
