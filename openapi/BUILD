# Copyright 2023 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

python_source(
    name="webapp",
    source="webapp.py",
)

# Explicitly declare `apispec_webframeworks`' dependency on `setuptools` (sigh)
python_requirement(
    name="setuptools",
    requirements=["setuptools"],
)

python_requirement(
    name="apispec-webframeworks",
    requirements=["apispec-webframeworks==0.5.2"],
    dependencies=[":setuptools"],
)


# Specify JAR dependencies
jvm_artifact(
    name="openapi-generator",
    group="org.openapitools",
    artifact="openapi-generator-cli",
    version="6.2.1",
)


adhoc_tool(
    name="generate-schema",
    runnable=":webapp",
    args=["dump-schema"],
    stdout="webapp-schema.json",    
    root_output_directory=".",
)

# Generate the openapi bindings from a schema produced by a different step
adhoc_tool(
    name="webapp-js-bindings",
    runnable=":openapi-generator",
    args=["generate", "-i", "webapp-schema.json", "--skip-validate-spec", "-g", "javascript", "-o", "./webapp-js-bindings"],
    execution_dependencies=[":generate-schema",],
    output_directories=["webapp-js-bindings/",],
    workdir="/",
    root_output_directory=".",
)
