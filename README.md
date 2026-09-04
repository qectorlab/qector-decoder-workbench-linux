<p align="center">
  <img src="assets/logo_banner.png" alt="QECTOR Logo" width="80%" />
</p>

<h1 align="center">QECTOR Decoder Workbench (Linux Release)</h1>

<p align="center">
  <strong>Professional Quantum Error Correction Analysis Suite</strong><br/>
  <em>19 Decoders · 10 Code Families · 85-tool MCP Server · GPU Acceleration</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.7-0078D4?style=for-the-badge&logo=linux&logoColor=white" alt="Version"/>
  <img src="https://img.shields.io/badge/backend-v1.0.0_(Rust%2FPyO3)-E44D26?style=for-the-badge&logo=rust&logoColor=white" alt="Backend"/>
  <img src="https://img.shields.io/badge/python-3.11--3.13-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/MCP_Tools-85-8A2BE2?style=for-the-badge" alt="MCP Tools"/>
  <img src="https://img.shields.io/badge/platform-Linux_(glibc_>=2.30)-success?style=for-the-badge" alt="Platform"/>
  <img src="https://img.shields.io/badge/license-Source--Available-FFA500?style=for-the-badge" alt="License"/>
</p>

<p align="center">
  <a href="https://www.qector.store">Website</a> ·
  <a href="#-quick-start">Quick Start</a> ·
  <a href="#-features">Features</a> ·
  <a href="INSTALL_LINUX.md">Install</a> ·
  <a href="CHANGELOG.md">CHANGELOG</a> ·
  <a href="#-license">License</a>
</p>

---

## 🚀 Overview

**QECTOR Decoder Workbench** is a production-grade desktop application for quantum error correction (QEC) research, evaluation, and documentation. Built on the high-performance `qector-decoder-v3` Rust/PyO3 engine, it provides interactive decoding, batch simulation, hardware-accelerated compute, and a full local-only MCP server for LLM/AI agent integration.

> **Zero Install · Zero Config · Zero Dependencies**
> Download. `chmod +x`. Decode.

This folder is the **Linux twin of the v1.0.7 Windows app**: identical Python application layer (`app.py`, `backend.py`, `cli.py`, `mcp_server.py`, all 9 tabs), repackaged with Linux-native launchers, paths, icons, and installers. See `LINUX_CHANGES.md` for the exact Windows→Linux diff.

---

## ⚡ Quick Start

### Portable binary (Recommended)

```bash
unzip QectorWorkbench-Linux-v1.0.7.zip
chmod +x QectorWorkbench-Portable
./QectorWorkbench-Portable                 # GUI
./QectorWorkbench-Portable --cli decode --family rotated_surface --distance 5 --decoder blossom
./QectorWorkbench-Portable --cli benchmark --family toric --distance 7 --samples 10000
./QectorWorkbench-Portable --cli diagnostics
./QectorWorkbench-Portable --mcp          # 85-tool MCP server (stdio JSON-RPC 2.0)
```

### From source

```bash
sudo apt install python3-tk python3-pip python3-venv
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements-linux.txt
# Offline labs: pip install --no-index --find-links=wheels-linux qector-decoder-v3==1.0.0
chmod +x qector-workbench
./qector-workbench                         # GUI
./qector-workbench --cli diagnostics
./qector-workbench --mcp
```

### Debian package

```bash
sudo dpkg -i qector-workbench_1.0.7_amd64.deb
qector-workbench                            # GUI
qector-workbench --cli diagnostics
qector-workbench --mcp
```

> **Fully local, no network required.** The portable binary embeds the `qector_decoder_v3-1.0.0` manylinux wheel and provisions it into a per-user managed site on first launch (`~/.local/share/QectorWorkbench/decoder_site/<abi_tag>`), so an air-gapped lab machine runs the complete workbench — including the MCP server.

**Runtime data** (logs, exports, managed decoder site) lives under `~/.local/share/QectorWorkbench` (or `$XDG_DATA_HOME/QectorWorkbench`). Override with `QECTOR_DATA_DIR`. See `utils.get_data_dir()`.

---

## 📥 Release assets (v1.0.7)

| Artifact | Contents |
|:---------|:---------|
| `QectorWorkbench-Linux-v1.0.7.zip` | `QectorWorkbench-Portable` + `wheels-linux/` (manylinux wheel) + `manuals/` + `EULA.txt` + `LICENSE` + `SBOM.json` + `SHA256SUMS.txt` |
| `qector-workbench_1.0.7_amd64.deb` | Thin app layer in `/opt/qector-workbench`, launcher `/usr/local/bin/qector-workbench`, `.desktop` entry; decoder provisioned on first launch from bundled `offline_wheel/` |

| Item | Value |
|:-----|:------|
| Workbench app | `1.0.7` |
| Decoder backend | `qector-decoder-v3 1.0.0` bundled manylinux wheel |
| MCP server | `85` tools over stdio JSON-RPC 2.0 (`2024-11-05`) |
| Decoders | `17` |
| Code families | `10` |

---

## ✨ Features (identical to Windows)

Nine interactive tabs + live Console: **Code Explorer · Decoder Lab · Benchmark · Batch & Streaming · History · Hardware · Diagnostics · Documentation · Lab & Personal Info**, plus CLI (22 subcommands) and the 85-tool MCP server. Code families (10) and decoder algorithms (17) are unchanged — see `README_WINDOWS.md` for the full tables, or run:

```bash
./qector-workbench --cli list-codes
./qector-workbench --cli list-decoders
./qector-workbench --cli matrix --format table
```

### 💻 CLI Reference

```
qector-workbench <command> [options]   # or ./QectorWorkbench-Portable --cli <command>
```

Global flags: `--json --no-color --no-banner --output/-o --verbose/-v --quiet/-q --config/-c --version/-V`.
Subcommands (22): `decode benchmark probe diagnostics hardware list-codes list-decoders docgen version compare batch stream train export import matrix serve doctor compliance entra decode_mmap completions`.

```bash
./qector-workbench --cli decode --family rotated_surface --distance 5 --decoder blossom --error-rate 0.05
./qector-workbench --cli compare --family rotated_surface --distance 5 --decoders blossom,bp_osd,union_find
./qector-workbench --cli batch --family rotated_surface --distance 5 --backend cpu --samples 1000
./qector-workbench --cli stream --family rotated_surface --distance 5 --window 5 --n-rounds 100
./qector-workbench --cli doctor
./qector-workbench --cli compliance
./qector-workbench --cli completions --shell bash >> ~/.bash_completion
```

---

## 🖥️ System Requirements

| Component | Requirement |
|:----------|:------------|
| **OS** | Linux x86_64, glibc ≥ 2.30 (Ubuntu 22.04/24.04, Debian 12, Fedora 39+, Arch) |
| **Runtime** | Portable binary: none (bundles Python 3.12). Source: Python 3.11–3.13 + `python3-tk` |
| **RAM** | 4 GB minimum, 8 GB recommended |
| **GPU** | Optional · CUDA for GPU-accelerated batch decode |
| **Disk** | ~130 MB (portable binary) |
| **Display** | Not required for CLI / MCP headless modes (`--cli`, `--mcp`) |

---

## 🔬 Decoder Runtime Provisioning

1. **Bundled wheel** · `wheels-linux/qector_decoder_v3-1.0.0-*-manylinux*.whl` ships inside the binary
2. **Managed site** · extracted to `~/.local/share/QectorWorkbench/decoder_site/<abi_tag>` on first launch
3. **Self-heal** · corruption rebuilds from the bundled wheel; outdated versions purged automatically
4. No PyPI access at runtime (air-gapped). Source installs may `pip install` the loose wheel.

---

## 🛡️ Air-Gapped Hardening

- Bundled wheel activation works without internet; MCP transport is stdio-only (no HTTP port)
- Version checks resolve against the bundled baseline, not a network update service
- `QECTOR_DATA_DIR` redirects all runtime data; license keys encrypted at rest (Fernet + OS keyring)
- Export artifacts carry SHA-256 sidecars (`sha256sum -c SHA256SUMS.txt`)

---

## 📚 Documentation

| Document | Where |
|:---------|:------|
| Install guide | `INSTALL_LINUX.md` (this folder) |
| Windows→Linux diff | `LINUX_CHANGES.md` |
| Quick Start / User Manual / API / MCP guide | `manuals/` |
| `CHANGELOG.md`, `EULA.txt`, `LICENSE`, `SECURITY.md` | this folder |

---

## ⚖️ License

Workbench: source-available under `EULA.txt` (royalty-free use, retain QECTOR notices, §2).
Backend `qector-decoder-v3`: free for personal/academic/non-commercial research; commercial use requires a [paid license](https://qector.store/pricing) (60-day evaluation available).

---

<p align="center">
  <strong>QECTOR Decoder Workbench v1.0.7 (Linux)</strong><br/>
  Built on <code>qector-decoder-v3</code> v1.0.0 (Rust/PyO3 core)<br/><br/>
  © 2026 Guillaume Lessard / iD01t Productions ·
  ORCID <a href="https://orcid.org/0009-0000-3465-3753">0009-0000-3465-3753</a><br/><br/>
  <em>Powered by QECTOR</em>
</p>

