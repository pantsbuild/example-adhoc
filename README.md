# example-adhoc
An example repository to demonstrate support for unsupported languages and arbitrary 3rd-party tools in Pants.

See [pantsbuild.org](https://www.pantsbuild.org/docs) for much more detailed documentation.

This is only one possible way of laying out your project with Pants. See 
[pantsbuild.org/docs/source-roots#examples](https://www.pantsbuild.org/docs/source-roots#examples) for some other
example layouts.

This repository demonstrates advanced uses of Pants. For more introductory use cases, consider looking at `example-python` or `example-jvm`.

## Examples

### Using a JVM artifact from Maven to generate Python source code

Using `adhoc_tool`, you can run a Maven artifact that's declared by a `jvm_artifact` target. We can use that to run the JVM-based `antlr` parser generator to transparently produce Python bindings, which can then be imported from our first-party Python code.

To see the demo in practice, run `./pants run antlr/antlr_demo.py`.

This demo uses:

* `jvm_artifact` to declare a dependency on the Antlr parser generator
* `adhoc_tool` which asks Pants to run the Antlr dependency as a build step, outputting files containing Python bindings (as loose `files`)
* `experimental_wrap_as_python_sources`, which allows subsequent steps to consume the loose files as Python sources that can be imported.

Note that sources declared by `experimental_wrap_as_*` targets can not currently be detected using Dependency Inference.

