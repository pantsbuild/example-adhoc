# Copyright 2022 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

jvm_artifact(
    name="antlr4",
    group="org.antlr",
    artifact="antlr4",
    version="4.11.1",
)

files(name="grammars", sources=["*.g4"])

python_source(
    name="antlr_demo",
    source="antlr_demo.py",
    dependencies=[":expr_parser_py", ":antlr4-python3-runtime",],
)

python_source(
    name="magic",
    source="magic.py",
    dependencies=[":expr_parser_py",],
)

experimental_run_in_sandbox(
    name="run_antlr",
    runnable=":antlr4",
    args=["Expr.g4", "-Dlanguage=Python3", "-o", "expr_parser", "-package", "expr_parser",],
    output_directories=["expr_parser",],
    execution_dependencies=[":grammars"],
    log_output=True,
)

experimental_run_in_sandbox(
    name="run_magic",
    runnable=":magic",
    stdout="stdout",
    stderr="stderr",
)

experimental_wrap_as_python_sources(name="expr_parser_py", inputs=[":run_antlr", ])

python_requirement(
    name="antlr4-python3-runtime",
    modules=["antlr4",],
    requirements=["antlr4-python3-runtime==4.11.1",],   
)


experimental_shell_command(
    name="whoops",
    tools=["ls",],
    command="ls -laR {chroot} > floopington",
    output_files=["floopington",],
    execution_dependencies=[":run_antlr"],
    root_output_directory=".",
)

experimental_run_shell_command(
    name="florb",
    command="echo hello world && cat {chroot}/floopington",
    execution_dependencies=[":whoops2"],
)




system_binary(
    name="bash",
    binary_name="bash",
    fingerprint=r"Binary Name v6\.32\.1",
    fingerprint_args=("-c","Bina"),
)

adhoc_tool(
    name="adhoc",
    runnable=":bash",
    args=["-c","echo I am a duck!"],
    log_output=True,
    stdout="stdout",
)
