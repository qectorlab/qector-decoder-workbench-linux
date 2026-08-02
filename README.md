# QECTOR Decoder Workbench — Linux

[![License](https://img.shields.io/badge/license-source--available-blue)](EULA.txt)
[![Backend](https://img.shields.io/badge/backend-qector--decoder--v3%200.7.0-informational)](https://pypi.org/project/qector-decoder-v3/0.7.0/)

A native Linux port of QECTOR Decoder Workbench v0.5.2 for x86_64 desktop Linux. This repository builds a portable AppImage and distro-tuned Debian packages.

## Table of Contents

- [Overview](#overview)
- [Install the Prebuilt .deb (Recommended)](#install-the-prebuilt-deb-recommended)
- [Quick Start (Build from Source)](#quick-start-build-from-source)
- [Compatibility](#compatibility)
- [Native Installers](#native-installers--separate-ubuntu--antix-deb-packages)
- [compile.sh Flags](#compilesh-flags)
- [What the Build Does](#what-the-build-does)
- [Decoders, Code Families & Features](#decoders-code-families--new-features-v070-backend)
- [System Prerequisites](#system-prerequisites-native-build-only)
- [Linux-Native Changes vs. the Windows Tree](#linux-native-changes-vs-the-windows-tree)
- [Verify](#verify)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Citation](#citation)
- [Related](#related)

## Overview

The Workbench bundle ships the ABI-correct `qector-decoder-v3` manylinux wheel (v0.7.0) as a bundled data file. On first launch, `decoder_provisioner.py` purges any outdated managed decoder site (< 0.7.0), extracts the bundled wheel into the ABI-scoped managed user site, and activates it — fully offline, no PyPI access needed. This is the exact same provisioning model as the Windows production build.

**Target: Linux x86_64 only** — the compiled `qector-decoder-v3` backend ships manylinux x86_64 wheels but no aarch64 Linux wheel.

## Install the Prebuilt `.deb` (Recommended)

Two packages are provided — the same app with tuned dependencies. Pick your distro and run from the folder containing the `.deb` files:

```bash
# Ubuntu / Debian / Mint (resolves dependencies automatically)
sudo apt install ./qector-workbench_0.5.2_amd64_ubuntu.deb

# antiX / MX (dpkg, then pull any missing deps)
sudo dpkg -i ./qector-workbench_0.5.2_amd64_antix.deb && sudo apt-get -f install

qector-workbench          # launch the GUI (also in the Science / Education menu)
qector-workbench --mcp    # 56-tool stdio MCP server
sudo apt remove qector-workbench   # uninstall
```

The app is fully self-contained: embedded Python 3.11 + Tcl/Tk + scientific stack, with the decoder provisioned offline from the bundled wheel. No system Python, pip, or internet connection is required.

## Quick Start (Build from Source)

```bash
cd Linux

# UNIVERSAL build (recommended) — runs on almost any Linux. Needs Docker.
# Builds in Debian 11 / glibc 2.31, so the AppImage requires only glibc >= 2.30.
./compile.sh --docker --test

# …or a fast native build on this host. NOTE: the resulting AppImage requires
# the *host's* glibc or newer — build on an old distro for wide compatibility.
./compile.sh --with-deps --test
```

Output:

```
dist/QectorWorkbench-0.5.2-x86_64.AppImage
```

Run it:

```bash
chmod +x dist/QectorWorkbench-0.5.2-x86_64.AppImage
./dist/QectorWorkbench-0.5.2-x86_64.AppImage           # GUI
./dist/QectorWorkbench-0.5.2-x86_64.AppImage --mcp     # 56-tool stdio MCP server
```

## Compatibility

The `--docker` build produces a binary that requires glibc >= 2.30, so it runs on:

| Distro family | Minimum version (glibc) |
|---|---|
| antiX / MX Linux | antiX 21, MX 21 (Debian 11, 2.31) |
| Ubuntu | 20.04 LTS (2.31) and newer |
| Debian | 11 "bullseye" (2.31) and newer |
| Linux Mint | 20 (2.31) and newer |
| Fedora | 32 (2.30) and newer |
| openSUSE Leap | 15.3 (2.31) and newer |
| Arch / Manjaro / rolling | Supported |

A native build inherits the build host's glibc (e.g. Kali's 2.42), so it will not start on the older distros above — always use `--docker` for distribution.

## Native Installers — Separate Ubuntu & antiX `.deb` Packages

For a real installed app (menu entry + official icon, launches as `qector-workbench`) rather than a portable AppImage, build the two distro-tuned Debian packages:

```bash
cd Linux
./build_installers.sh            # both installers, reproducible glibc-2.31 Docker build
./build_installers.sh --test     # run the pytest suite inside the container first
./build_installers.sh --native   # build on this host instead of Docker
```

Output:

```
dist/qector-workbench_0.5.2_amd64_ubuntu.deb
dist/qector-workbench_0.5.2_amd64_antix.deb
```

Both wrap the same Workbench bundle (embedded Python 3.11 + Tcl/Tk + scientific stack, with the decoder provisioned offline from the bundled wheel) installed under `/usr/lib/qector-workbench`, with a `/usr/bin/qector-workbench` launcher, a desktop menu entry, and the official 256×256 icon in the hicolor theme. They differ only in their tuned `Depends:` (GL library naming): the antiX package accepts Debian 11's `libgl1-mesa-glx`, the Ubuntu package targets `libgl1`. Because both are built on the glibc 2.31 base, each still runs on Ubuntu 20.04+ / antiX 21+ and newer.

Install:

```bash
# Ubuntu / Debian / Mint (resolves dependencies automatically)
sudo apt install ./dist/qector-workbench_0.5.2_amd64_ubuntu.deb

# antiX / MX (dpkg, then pull any missing deps)
sudo dpkg -i ./dist/qector-workbench_0.5.2_amd64_antix.deb
sudo apt-get -f install

qector-workbench          # launch the GUI (also in the Science menu)
qector-workbench --mcp    # 56-tool stdio MCP server
sudo apt remove qector-workbench   # uninstall
```

## `compile.sh` Flags

| Flag | Effect |
|---|---|
| `--docker` | Build inside `python:3.11-slim-bullseye` (Debian 11, glibc 2.31, Python 3.11) for the widest compatibility. |
| `--with-deps` | `apt-get install` the system prerequisites (uses `sudo`). |
| `--test` | Run the pytest suite before packaging. |
| `--clean` | Remove `.venv/ build/ dist/` first. |
| `--no-appimage` | Stop after the PyInstaller onedir (leaves `dist/QectorWorkbench/`). |
| `-h`, `--help` | Usage. |

Flags combine, e.g. `./compile.sh --clean --with-deps --test`.

## What the Build Does

1. Creates a `.venv` and installs the runtime deps — all resolve to prebuilt manylinux wheels (`customtkinter`, `numpy`, `scipy`, `matplotlib`, `Pillow`, `psutil`), so no compiler is needed for the Python side.
2. Generates the professional icon set from the SVG master: a 256×256 `icon.png` (Linux hi-color theme) via Pillow.
3. Runs PyInstaller (`packaging/QectorWorkbench-linux.spec`) → a onedir bundle in `dist/QectorWorkbench/` that embeds Python 3.11 + Tcl/Tk + every dependency, plus the bundled `qector_decoder_v3-0.7.0-*.whl` data file.
4. Assembles an AppDir (`AppRun`, `.desktop`, icon, bundled DejaVu fonts) and packages it into the AppImage with `appimagetool`.

## Decoders, Code Families & New Features (v0.7.0 Backend)

This build wires all 16 decoders that the bundled `qector_decoder_v3` v0.7.0 exposes and that satisfy the workbench decode contract: `union_find`, `fast_union_find`, `blossom`, `sparse_blossom`, `bp_osd`, `auto`, `hybrid`, `lookup_table`, `predecoded`, `auto_router`, `hybrid_cascade`, `gnn_belief_matching`, `belief_matching`, plus the qLDPC-era additions (`bivariate_bicycle` family and `colour_code`).

It also wires all 10 code families, including the two qLDPC families — `bicycle` and `bivariate_bicycle` (the IBM BB code family, e.g. the [[72,12,6]] "gross" code) — `colour_code`, and the `hypergraph_product` CSS family (graphlike; built from a repetition-code seed). Coverage lives in `tests/test_decoders.py` and `tests/test_code_families.py` (construction, GF(2) syndrome validity, determinism, decoder-compatibility, benchmark and streaming).

A resilient self/auto-debug layer (`autodebug.py`, surfaced in the Diagnostics tab and via MCP tools — `self_diagnostics`, `probe_decoders`, `resilient_decode`) verifies `H·c == s` on every decode and automatically falls back through alternative decoders (and `cuda → opencl → cpu` for batch), recording a full attempt trace.

The 56-tool MCP server includes tools for versioning, native recommendations, streaming, cascade stats, neural predecoder training, and advanced decoding modes.

**Offline versioning** (`version_service.py`) resolves the effective app and backend versions locally — no PyPI queries. The window title and status bar show a stable banner (e.g. `QECTOR Decoder Workbench v0.5.2 | qector-decoder-v3 0.7.0`).

**New professional icon set**: the `.png` for the Linux hi-color theme and desktop entry is generated from the SVG master.

Run the suite:

```bash
MPLBACKEND=Agg .venv/bin/python -m pytest -q      # unit + GUI + decoder + autodebug
MPLBACKEND=Agg .venv/bin/python test_mcp_all.py   # 56-tool MCP verification
```

## System Prerequisites (Native Build Only)

`--with-deps` installs these on apt systems; on others install the equivalents:

```
python3 (>=3.11) python3-venv python3-tk build-essential
libgl1 libglib2.0-0 fonts-dejavu-core wget file desktop-file-utils libfuse2
```

`--docker` needs only Docker itself.

## Linux-Native Changes vs. the Windows Tree

This tree is a fully independent copy. Only four modules differ from Windows, each guarded so Windows/macOS behaviour is unchanged:

- **`app.py`** — window icon via `iconphoto` + PNG on Linux (Windows keeps `iconbitmap`/`.ico`).
- **`theme.py`** — DejaVu Sans / DejaVu Sans Mono on Linux (Consolas/Segoe UI on Windows).
- **`documentation_tab.py`** — "Open export folder" uses `xdg-open` (`open` on macOS, `startfile` on Windows).
- **`utils.py`** — per-user data dir follows the XDG spec (`$XDG_DATA_HOME` → `~/.local/share/QectorWorkbench`).

Runtime data (logs, exports) lives in `~/.local/share/QectorWorkbench/` (override with `QECTOR_DATA_DIR`).

## Verify

```bash
# Headless import smoke test
MPLBACKEND=Agg .venv/bin/python -c "import app, backend, mcp_server, theme; print('ok')"

# Full test suite
MPLBACKEND=Agg .venv/bin/python -m pytest -q

# MCP transport against the built AppImage (56 tools)
.venv/bin/python test_mcp_all.py
```

## Troubleshooting

- **AppImages require FUSE to run** — either install FUSE (`sudo apt install libfuse2`) or launch with `./QectorWorkbench-*.AppImage --appimage-extract-and-run`, or set `APPIMAGE_EXTRACT_AND_RUN=1`.
- **No window / `couldn't connect to display`** — the GUI needs an X11/Wayland session; MCP mode (`--mcp`) is headless and needs no display.
- **Older distro won't launch a native build** — rebuild with `--docker` for the glibc 2.31 baseline.

## License

**Workbench:** source-available — see EULA (free use including commercial, with QECTOR watermark retention per EULA §2).

**Backend `qector-decoder-v3`:** separately licensed by Guillaume Lessard / iD01t Productions — free for personal/academic/non-commercial research; commercial use requires a paid commercial license (www.qector.store, admin@qector.store). Honor the backend license for any commercial deployment.

## Citation

Citation metadata is maintained in [`CITATION.cff`](CITATION.cff) at the repository root. GitHub renders this automatically as a "Cite this repository" button on the repo's main page, offering APA and BibTeX export.

## Related

- **Windows Build:** [qectorlab/qector-decoder-workbench-windows](https://github.com/qectorlab/qector-decoder-workbench-windows)
- **PyPI Package:** [qector-decoder-v3 0.7.0](https://pypi.org/project/qector-decoder-v3/0.7.0/)
- **Core Library:** [GuillaumeLessard/qector-decoder](https://github.com/GuillaumeLessard/qector-decoder)
- **Commercial Licensing:** [qector.store](https://qector.store)

Author: Guillaume Lessard / iD01t Productions · ORCID [0009-0000-3465-3753](https://orcid.org/0009-0000-3465-3753) · [www.qector.store](https://www.qector.store)
