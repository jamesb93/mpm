oclif-hello-world
=================

oclif example Hello World CLI

[![oclif](https://img.shields.io/badge/cli-oclif-brightgreen.svg)](https://oclif.io)
[![Version](https://img.shields.io/npm/v/oclif-hello-world.svg)](https://npmjs.org/package/oclif-hello-world)
[![CircleCI](https://circleci.com/gh/oclif/hello-world/tree/main.svg?style=shield)](https://circleci.com/gh/oclif/hello-world/tree/main)
[![Downloads/week](https://img.shields.io/npm/dw/oclif-hello-world.svg)](https://npmjs.org/package/oclif-hello-world)
[![License](https://img.shields.io/npm/l/oclif-hello-world.svg)](https://github.com/oclif/hello-world/blob/main/package.json)

<!-- toc -->
* [Usage](#usage)
* [Commands](#commands)
<!-- tocstop -->
# Usage
<!-- usage -->
```sh-session
$ npm install -g mpm
$ mpm COMMAND
running command...
$ mpm (--version)
mpm/0.0.0 darwin-arm64 node-v19.1.0
$ mpm --help [COMMAND]
USAGE
  $ mpm COMMAND
...
```
<!-- usagestop -->
# Commands
<!-- commands -->
* [`mpm hello PERSON`](#mpm-hello-person)
* [`mpm hello world`](#mpm-hello-world)
* [`mpm help [COMMAND]`](#mpm-help-command)
* [`mpm plugins`](#mpm-plugins)
* [`mpm plugins:install PLUGIN...`](#mpm-pluginsinstall-plugin)
* [`mpm plugins:inspect PLUGIN...`](#mpm-pluginsinspect-plugin)
* [`mpm plugins:install PLUGIN...`](#mpm-pluginsinstall-plugin-1)
* [`mpm plugins:link PLUGIN`](#mpm-pluginslink-plugin)
* [`mpm plugins:uninstall PLUGIN...`](#mpm-pluginsuninstall-plugin)
* [`mpm plugins:uninstall PLUGIN...`](#mpm-pluginsuninstall-plugin-1)
* [`mpm plugins:uninstall PLUGIN...`](#mpm-pluginsuninstall-plugin-2)
* [`mpm plugins update`](#mpm-plugins-update)

## `mpm hello PERSON`

Say hello

```
USAGE
  $ mpm hello [PERSON] -f <value>

ARGUMENTS
  PERSON  Person to say hello to

FLAGS
  -f, --from=<value>  (required) Who is saying hello

DESCRIPTION
  Say hello

EXAMPLES
  $ oex hello friend --from oclif
  hello friend from oclif! (./src/commands/hello/index.ts)
```

_See code: [dist/commands/hello/index.ts](https://github.com/jamesb93/mpm/blob/v0.0.0/dist/commands/hello/index.ts)_

## `mpm hello world`

Say hello world

```
USAGE
  $ mpm hello world

DESCRIPTION
  Say hello world

EXAMPLES
  $ mpm hello world
  hello world! (./src/commands/hello/world.ts)
```

## `mpm help [COMMAND]`

Display help for mpm.

```
USAGE
  $ mpm help [COMMAND] [-n]

ARGUMENTS
  COMMAND  Command to show help for.

FLAGS
  -n, --nested-commands  Include all nested commands in the output.

DESCRIPTION
  Display help for mpm.
```

_See code: [@oclif/plugin-help](https://github.com/oclif/plugin-help/blob/v5.1.18/src/commands/help.ts)_

## `mpm plugins`

List installed plugins.

```
USAGE
  $ mpm plugins [--core]

FLAGS
  --core  Show core plugins.

DESCRIPTION
  List installed plugins.

EXAMPLES
  $ mpm plugins
```

_See code: [@oclif/plugin-plugins](https://github.com/oclif/plugin-plugins/blob/v2.1.6/src/commands/plugins/index.ts)_

## `mpm plugins:install PLUGIN...`

Installs a plugin into the CLI.

```
USAGE
  $ mpm plugins:install PLUGIN...

ARGUMENTS
  PLUGIN  Plugin to install.

FLAGS
  -f, --force    Run yarn install with force flag.
  -h, --help     Show CLI help.
  -v, --verbose

DESCRIPTION
  Installs a plugin into the CLI.
  Can be installed from npm or a git url.

  Installation of a user-installed plugin will override a core plugin.

  e.g. If you have a core plugin that has a 'hello' command, installing a user-installed plugin with a 'hello' command
  will override the core plugin implementation. This is useful if a user needs to update core plugin functionality in
  the CLI without the need to patch and update the whole CLI.


ALIASES
  $ mpm plugins add

EXAMPLES
  $ mpm plugins:install myplugin 

  $ mpm plugins:install https://github.com/someuser/someplugin

  $ mpm plugins:install someuser/someplugin
```

## `mpm plugins:inspect PLUGIN...`

Displays installation properties of a plugin.

```
USAGE
  $ mpm plugins:inspect PLUGIN...

ARGUMENTS
  PLUGIN  [default: .] Plugin to inspect.

FLAGS
  -h, --help     Show CLI help.
  -v, --verbose

DESCRIPTION
  Displays installation properties of a plugin.

EXAMPLES
  $ mpm plugins:inspect myplugin
```

## `mpm plugins:install PLUGIN...`

Installs a plugin into the CLI.

```
USAGE
  $ mpm plugins:install PLUGIN...

ARGUMENTS
  PLUGIN  Plugin to install.

FLAGS
  -f, --force    Run yarn install with force flag.
  -h, --help     Show CLI help.
  -v, --verbose

DESCRIPTION
  Installs a plugin into the CLI.
  Can be installed from npm or a git url.

  Installation of a user-installed plugin will override a core plugin.

  e.g. If you have a core plugin that has a 'hello' command, installing a user-installed plugin with a 'hello' command
  will override the core plugin implementation. This is useful if a user needs to update core plugin functionality in
  the CLI without the need to patch and update the whole CLI.


ALIASES
  $ mpm plugins add

EXAMPLES
  $ mpm plugins:install myplugin 

  $ mpm plugins:install https://github.com/someuser/someplugin

  $ mpm plugins:install someuser/someplugin
```

## `mpm plugins:link PLUGIN`

Links a plugin into the CLI for development.

```
USAGE
  $ mpm plugins:link PLUGIN

ARGUMENTS
  PATH  [default: .] path to plugin

FLAGS
  -h, --help     Show CLI help.
  -v, --verbose

DESCRIPTION
  Links a plugin into the CLI for development.
  Installation of a linked plugin will override a user-installed or core plugin.

  e.g. If you have a user-installed or core plugin that has a 'hello' command, installing a linked plugin with a 'hello'
  command will override the user-installed or core plugin implementation. This is useful for development work.


EXAMPLES
  $ mpm plugins:link myplugin
```

## `mpm plugins:uninstall PLUGIN...`

Removes a plugin from the CLI.

```
USAGE
  $ mpm plugins:uninstall PLUGIN...

ARGUMENTS
  PLUGIN  plugin to uninstall

FLAGS
  -h, --help     Show CLI help.
  -v, --verbose

DESCRIPTION
  Removes a plugin from the CLI.

ALIASES
  $ mpm plugins unlink
  $ mpm plugins remove
```

## `mpm plugins:uninstall PLUGIN...`

Removes a plugin from the CLI.

```
USAGE
  $ mpm plugins:uninstall PLUGIN...

ARGUMENTS
  PLUGIN  plugin to uninstall

FLAGS
  -h, --help     Show CLI help.
  -v, --verbose

DESCRIPTION
  Removes a plugin from the CLI.

ALIASES
  $ mpm plugins unlink
  $ mpm plugins remove
```

## `mpm plugins:uninstall PLUGIN...`

Removes a plugin from the CLI.

```
USAGE
  $ mpm plugins:uninstall PLUGIN...

ARGUMENTS
  PLUGIN  plugin to uninstall

FLAGS
  -h, --help     Show CLI help.
  -v, --verbose

DESCRIPTION
  Removes a plugin from the CLI.

ALIASES
  $ mpm plugins unlink
  $ mpm plugins remove
```

## `mpm plugins update`

Update installed plugins.

```
USAGE
  $ mpm plugins update [-h] [-v]

FLAGS
  -h, --help     Show CLI help.
  -v, --verbose

DESCRIPTION
  Update installed plugins.
```
<!-- commandsstop -->
