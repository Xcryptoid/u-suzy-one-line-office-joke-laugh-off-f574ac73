"""Copy the finished one-line office joke into the grader output folder."""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(HERE, "entry.txt"),
        os.path.join(out_dir, "entry.txt"),
    )


if __name__ == "__main__":
    main()


# Note: this file does not write or change the joke itself. It only
# carries the finished text file over to the output folder exactly as
# it already is, so what gets judged is the joke we already wrote.
