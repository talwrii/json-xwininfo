# json-xwininfo
[@readwithai](https://x.com/readwithai) - [X](https://x.com/readwithai) - [blog](https://readwithai.substack.com/) - [machine-aid reading](https://www.reddit.com/r/machineAidedReading/)

Get information about an X11 window in machine-readable JSON. This is similar to the `xwininfo` information

# Installation
You can install this using [pipx](https://github.com/pypa/pipx):

```
pipx install json-xwinfo
```

# Usage
```
json-xwininfo
```

You can information about the currently focused window using:

```
json-xwininfo --focused
```

Most programming languages provides facilities to easily parse `JSON`. For using this information at the moment line you may wish to use the [jq](https://github.com/jqlang/jq).

# Alternatives and prior work
This tool is obviously inspired by [xwininfo](https://packages.debian.org/buster/x11-utils) and at the moment wraps this tool and parses the output. This tool usings [Xlib](https://github.com/python-xlib/python-xlib). You may prefer to use this library to obtain this information rather than using this tool for more "self-contained" pieces of software.

# Motivation
I was experimenting with displaying information at particular positions on the screen - such as the top left corner of the window. The shell code necessary to do this was a little too involved to count as a good idea so I decided to wrap this into tool.

# Caveats
Information is partial. At the moment this tool wraps `xwininfo` and parses the output.

# Support
If you find this tool useful you can support it by [giving me money on ko-fi](https://ko-fi.com/c/b10db5a742). I would suggest a $1 dollar donation if you find this tool useful. This will incentivise me to create [similar tools](https://readwithai.substack.com/p/my-productivity-tools).

You may also like to look at my [json-wmctrl](https://github.com/talwrii/json-wmctrl) which can be used to list and select windows and raise them.

You might like to read some of my [writing about the note taking app Obsidian](https://readwithai.substack.com/p/what-exactly-is-obsidian).

# About me
I am **@readwithai**. I make tools related to reading, research and productivity sometimes with [Obsidian](https://readwithai.substack.com/p/what-exactly-is-obsidian).

You can follow me on [X](https://x.com/readwithai) where I post about tools like this and a range of topics. Or if reading and research sounds interesting you could read [my blog](https://readwithai.substack.com/).

![@readwithai logo](./logo.png)
