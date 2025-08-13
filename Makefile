.PHONY: html live clean

html:
	. .venv/bin/activate 2>/dev/null || true; sphinx-build -b html docs docs/_build/html

live:
	. .venv/bin/activate 2>/dev/null || true; sphinx-autobuild docs docs/_build/html --open-browser --host 0.0.0.0 --port 8000

clean:
	rm -rf docs/_build
