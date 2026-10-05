"""Internal helper: run a single example with evaluation-mode limits made non-fatal.

run_all_examples.py invokes this wrapper for each example as a separate subprocess.
A fresh process per example resets the evaluation build's documents-per-process
budget; this wrapper self-applies the license (when GROUPDOCS_LIC_PATH points at a
real file) and turns evaluation-limit and missing-font errors into a logged note +
exit 0, so the example still demonstrates the API and the suite stays green.

Usage (from run_all_examples.py):  python Examples/_run_example.py <example.py>
"""
import os
import runpy
import sys

from groupdocs.signature import License


def _apply_license():
    license_path = os.environ.get("GROUPDOCS_LIC_PATH")
    if license_path and os.path.exists(license_path):
        try:
            License().set_license(license_path)
        except Exception:
            pass


def _is_evaluation_limit(exc):
    lowered = str(exc).lower()
    return (
        "evaluation mode" in lowered
        or "evaluation only" in lowered
        or "trial mode" in lowered
        or "trial version" in lowered
        or "evaluation version allows" in lowered
        or ("evaluation" in lowered and "limit" in lowered)
    )


def _is_font_unavailable(exc):
    lowered = str(exc).lower()
    return "fontnotfoundexception" in lowered or ("font" in lowered and "was not found" in lowered)


def main(argv):
    if len(argv) != 2:
        print("Usage: _run_example.py <example.py>", file=sys.stderr)
        return 2
    _apply_license()
    try:
        runpy.run_path(argv[1], run_name="__main__")
    except Exception as exc:
        if _is_evaluation_limit(exc):
            print("Note: example stopped at an evaluation-mode limit (apply a license to run it fully).")
            return 0
        if _is_font_unavailable(exc):
            print("Note: example needs a named font not available on this host (run on Windows/macOS or install it).")
            return 0
        raise
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
