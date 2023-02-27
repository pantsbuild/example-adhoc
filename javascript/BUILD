# Dependencies and source files
files(
    name="package-config",
    sources=["package.json", "yarn.lock",],
    dependencies=[],
)

# The source files themselves
files(
    name="js-sources",
    sources=["*.js",],
    dependencies=[],
)

system_binary(
    name="node",
    binary_name="node",
    fingerprint=r"v(19|[2-9][0-9])\..*\..*",
    fingerprint_args=["--version"],
)

system_binary(
    name="yarn",
    binary_name="yarn",
    fingerprint=r"1\.([2-9][0-9]|[1-9][0-9][0-9])\..*",
    fingerprint_args=["--version"],
    fingerprint_dependencies=[":node"],
)

# Fetch the dependencies and produce a `node_modules` directory
adhoc_tool(
    name="node-modules",
    runnable=":yarn",
    runnable_dependencies=[":node"],
    args=["install", "--immutable"],
    output_dependencies=[":package-config"],
    execution_dependencies=[":package-config"],
    output_directories=["node_modules"],
    timeout=300,
)

# Minify the JS sources and dependencies into a single js file.
adhoc_tool(
    name="build-js-app",
    runnable=":yarn",
    runnable_dependencies=[":node"],
    args=["parcel", "build"],
    execution_dependencies=[":node-modules", ":js-sources",],
    output_files=["index.js", "index.js.map",],
    root_output_directory=".",
)

# Run the resulting JS file
run_shell_command(
    name="run-js-app",
    command="node {chroot}/index.js",
    execution_dependencies=[":build-js-app",],
)

# Demonstrate using the JS file as an input to an artifact
archive(
    name="packaged-js",
    format="tar",
    description="Package containing `index.js` file",
    files=[":build-js-app",],
)