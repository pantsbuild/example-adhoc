# Copyright 2022 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

#
# Third-party requirements
#

jvm_artifact(
    name="antlr4",
    group="org.antlr",
    artifact="antlr4",
    version="4.11.1",
)

python_requirement(
    name="antlr4-python3-runtime",
    modules=["antlr4",],
    requirements=["antlr4-python3-runtime==4.11.1",],   
)

#
# Target that can be run with `pants run`
#

python_source(
    name="antlr_demo",
    source="antlr_demo.py",
    dependencies=[":expr_parser_py", ":antlr4-python3-runtime",],
)

#
# Sources for the `adhoc_tool`
#

files(name="grammars", sources=["*.g4"])

#
# `adhoc_tool` for handling antlr grammar files, outputting Python sources
#

# Runs the jar declared in `:antlr` with the args specified in `args`, consuming the grammar
# from `:grammars`, providing the files in `expr_parser` as outputs. 
adhoc_tool(
    name="run_antlr",
    runnable=":antlr4",
    args=["Expr.g4", "-Dlanguage=Python3", "-o", "expr_parser", "-package", "expr_parser",],
    output_directories=["expr_parser",],
    # These are consumed by `antlr`, but are not relevant to this target's dependents.
    execution_dependencies=[":grammars"],
    log_output=True,
)

# Allows the loose files provided by `:run_antlr` to be consumed as Python sources
experimental_wrap_as_python_sources(name="expr_parser_py", inputs=[":run_antlr", ])
