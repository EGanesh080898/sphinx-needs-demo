import os
import sys
from datetime import date

project = "IVC Module — Sphinx-Needs Demo"
author = "Your Team"
copyright = f"{date.today().year}, {author}"

extensions = [
    "myst_parser",
    "sphinx_needs",
]

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "alabaster"
html_static_path = ["_static"]

# --- Sphinx-Needs configuration ---
needs_types = [
    dict(directive="req",  title="Requirement",   prefix="REQ_"),
    dict(directive="spec", title="Specification", prefix="SPEC_"),
    dict(directive="impl", title="Implementation",prefix="IMPL_"),
    dict(directive="test", title="Test Case",     prefix="TEST_"),
    dict(directive="process", title="Process Step", prefix="PROC_"),
]

needs_statuses = ["open", "in_progress", "done", "blocked", "deprecated"]
needs_tags = ["networking", "safety", "performance", "reliability", "perception", "control"]

# Extra fields you can use like :priority:, :component:, :owner:
needs_extra_options = ["priority", "component", "owner"]

# Optional: style tweaks for tables/lists (can be themed later)
needs_table_style = "table"
