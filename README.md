# Pants `adhoc_tool` examples

This is an example repository to demonstrate support for arbitrary languages and 3rd-party tools in [Pants](https://pantsbuild.org).

See [pantsbuild.org](https://www.pantsbuild.org/stable/docs/ad-hoc-tools/integrating-new-tools-without-plugins) for much more detailed documentation of `adhoc_tool` and `system_binary`.

This is only one possible way of laying out your project with Pants. See 
[pantsbuild.org/docs/source-roots#examples](https://www.pantsbuild.org/docs/source-roots#examples) for some other example layouts.

This repository demonstrates advanced uses of Pants. For more introductory use cases, consider looking at [`example-python`](https://github.com/pantsbuild/example-python) or [`example-jvm`](https://github.com/pantsbuild/example-jvm).

## Examples

### Using a JVM artifact from Maven to generate Python source code

Using `adhoc_tool`, you can run a Maven artifact that's declared by a `jvm_artifact` target. We can use that to run the JVM-based `antlr` parser generator to transparently produce Python bindings, which can then be imported from our first-party Python code.

To see the demo in practice, run `pants run antlr/antlr_demo.py`.

This demo uses:

* `jvm_artifact` to declare a dependency on the Antlr parser generator
* `adhoc_tool` which asks Pants to run the Antlr dependency as a build step, outputting files containing Python bindings (as loose `files`)
* `experimental_wrap_as_python_sources`, which allows subsequent steps to consume the loose files as Python sources that can be imported.

Note that sources declared by `experimental_wrap_as_*` targets can not currently be detected using Dependency Inference.


### Building a JavaScript asset for inclusion in a web application

Using `system_binary`, you can declare dependencies on tools that are managed externally to Pants, including basic compatibility checks by way of version constraints.

This allows you to use tools from languages that aren't directly supported by Pants. We can use that to manage a `node_modules` directory using `yarn` and `node` binaries that were installed onto the host system (e.g. by Homebrew or `apt`).

Our demo produces a simple CLI script that imports an `npm` dependency and functions from a first-party library and links them together using [Parcel](https://parceljs.org/). Package resolution and tool execution is handled by `yarn`.

To see the demo in practice, run `pants run javascript:run-js-app`, or `pants package javascript:packaged-js` to package the JavaScript code into a zip file.

This demo uses:

* `system_binary` to declare dependencies on `node` and `yarn` binaries. The `fingerprint*` fields are used to declare version constraints that can be used to ensure builds are reproducible across multiple execution environments.
* `adhoc_tool` to execute the `yarn install` and `yarn parcel` commands.
* `run_shell_command` to run the generated JavaScript artifact with `node`.
* `archive` to package the generated JavaScript archive into a zip file


### Automatically generating JavaScript bindings for a Flask web app with an OpenAPI schema

Using `adhoc_tool`, you can run individual first-party sources to fetch their output. This can produce inputs for other targets.

In this example, a small Flask web application can dump an OpenAPI schema, which can in turn be used to transparently generate bindings for other languages.

To see the demo in practive, run `pants export-codegen openapi:webapp-js-bindings`

This demo uses

* `python_source` to declare a runnable Python source, `webapp.py`.
* `jvm_artifact` to declare a dependency on the JVM-based OpenAPI client generator
* `adhoc_tool` to run the `webapp.py` source, and saving its `stdout` to a file using the `stdout=` field
* `adhoc_tool` to run the JVM client generator