from IPython.core.magic import register_cell_magic
from IPython.display import display, Markdown
import subprocess
import tempfile
from pathlib import Path

@register_cell_magic
def mypy(line, cell):
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        source = tmp / "demo.py"
        cache = tmp / "mypy-cache"

        source.write_text(cell)

        result = subprocess.run(
            [
                "python", "-m", "mypy",
                "--no-incremental",
                "--no-color-output",
                "--cache-dir", str(cache),
                *line.split(),
                str(source),
            ],
            capture_output=True,
            text=True,
        )

    output = result.stdout + result.stderr
    output = output.replace(str(source), "mypy output: ")

    display(Markdown(f"```text\n{output or 'Success: no issues found'}\n```"))