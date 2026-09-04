import os

os.environ["QECTOR_SILENT"] = "1"

# Product version of the Workbench application itself. This is the public
# release line (1.0.x) and is deliberately INDEPENDENT of BACKEND_VERSION
# below: the decoder ships on its own cadence, and copying its number here has
# already caused a release to be labelled with the backend's version.
WORKBENCH_VERSION = "1.0.6"
DOC_GENERATOR_VERSION = "1.0.6"
# Backend: qector-decoder-v3.  It IS bundled into the app as a platform-specific
# wheel.  decoder_provisioner activates it from the bundled wheel into an
# ABI-scoped managed site on first launch (offline).  BACKEND_VERSION is the
# bundled release version.
BACKEND_VERSION = "1.0.0"
MIN_BACKEND_VERSION = "1.0.0"
# This constant is a cache, not a source of truth: it must equal
# len(mcp_server.get_mcp_server().tools.tools) on the live registry. It has
# drifted twice already (47->56->85->86, and then back down to 85 when the
# flush_usage tool was unregistered for the 0b.1 air-gap fix in
# todo777.md) because nothing enforced the two staying in sync. Any future
# tool registration/removal MUST update this line in the same commit;
# `scripts/check_docs.py` and `dev/_verify_todo777_baseline.py` both assert
# against the live registry count independently of this constant, so a
# stale value here will be caught, not silently shipped.
MCP_TOOLS = 85
# Upstream backend attribution (see the QECTOR Decoder v3 user manual).
AUTHOR = "Guillaume Lessard / iD01t Productions"
AUTHOR_ORCID = "0009-0000-3465-3753"
PROJECT_URL = "https://www.qector.store"
FULL_VERSION = f"QECTOR Decoder Workbench v{WORKBENCH_VERSION}"

# ---------------------------------------------------------------------------
# Developer / business information, surfaced in-app (Documentation tab) and CLI.
# ---------------------------------------------------------------------------
COMPANY = "iD01t Productions"
MAINTAINER = "Guillaume Lessard"
CONTACT_EMAIL = "admin@qector.store"
PRICING_URL = "https://qector.store/pricing"
SUPPORT_URL = "https://www.qector.store"
LICENCE_SUMMARY = (
    "Source-available. Free for academic, personal and non-commercial research. "
    "Commercial use requires a paid licence."
)
LICENCE_EVALUATION = "60-day commercial evaluation available, creditable against a licence."


def business_info() -> dict:
    """Developer/business facts as a plain mapping (used by the GUI and CLI)."""
    return {
        "product": f"QECTOR Decoder Workbench v{WORKBENCH_VERSION}",
        "backend": f"qector-decoder-v3 v{BACKEND_VERSION} (Rust/PyO3 core, bundled)",
        "company": COMPANY,
        "maintainer": MAINTAINER,
        "orcid": AUTHOR_ORCID,
        "contact": CONTACT_EMAIL,
        "website": PROJECT_URL,
        "pricing": PRICING_URL,
        "licence": LICENCE_SUMMARY,
        "evaluation": LICENCE_EVALUATION,
    }
