"""Validate standalone Python examples embedded in the learning tutorials."""

from __future__ import annotations

import ast
import contextlib
import io
import re
import tempfile
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
TUTORIALS = (
    "programming/python/01_basis_function.md",
    "programming/python/02_variable_and_data_type.md",
    "programming/python/03_operators.md",
    "programming/python/command.md",
)
FENCE = re.compile(r"^\x60\x60\x60python\s*\n(.*?)^\x60\x60\x60\s*$", re.MULTILINE | re.DOTALL)


def main() -> None:
    failures = []
    tested = 0
    for relative in TUTORIALS:
        path = ROOT / relative
        markdown = path.read_text(encoding="utf-8")
        blocks = FENCE.findall(markdown)
        if not blocks:
            failures.append(f"{relative}: no Python examples found")
        for index, source in enumerate(blocks, start=1):
            tested += 1
            label = f"{relative} (block {index})"
            try:
                compiled = compile(ast.parse(source, filename=label), label, "exec")
                # Run each block independently; mock input and isolate generated files.
                responses = iter(["Ada", "25", "101.5"])
                with tempfile.TemporaryDirectory() as tmp:
                    with patch("builtins.input", side_effect=lambda prompt="": next(responses)):
                        with contextlib.redirect_stdout(io.StringIO()):
                            exec(compiled, {"__name__": "__main__", "__file__": str(Path(tmp) / "example.py")})
            except Exception as exc:
                failures.append(f"{label}: {type(exc).__name__}: {exc}")
    print(f"Validated {tested} Python examples across {len(TUTORIALS)} tutorials.")
    if failures:
        raise SystemExit("\n".join(failures))
    print("All Python tutorial examples passed.")


if __name__ == "__main__":
    main()
