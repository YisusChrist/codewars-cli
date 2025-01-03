An unofficial CLI for CodeWars.

Table of Contents

- [Configuration](#configuration)
- [Installation](#installation)
- [Usage](#usage)

## Configuration

You need to set the `CW_SESSION_ID` and `CW_REMEMBER_USER_TOKEN` environment variables which you can grab from your cookies.

Rich will look at `MANPAGER` then the `PAGER` environment variables (`MANPAGER` takes priority) to get the pager command. On Linux and macOS you can set one of these to `less -r` to display the description with ANSI styles.

## Installation

You can install `codewars-cli` using `pip`:

```sh
pip install codewars-cli
```

## Usage

```sh
$ codewars --help
Usage: codewars [OPTIONS] COMMAND [ARGS]...

  An unofficial CLI for CodeWars.

Options:
  --help  Show this message and exit.

Commands:
  attempt   Attempt to pass the full test suite.
  practice  Search for a kata.
  submit    Submit your solution.
  test      Test against the sample tests.
  train     Choose a kata to solve.
```

You can also check the help for each subcommand.
