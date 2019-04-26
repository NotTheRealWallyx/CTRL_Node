# Server tools

Scan the ports of your server or get the DNS records with this small scripts.

## Prerequisites

You only need two things to run the scripts Python and dnspython to install dnspython you can use pip:

```
pip uninstall dnspython
```

## Options

Options:
  -h  --help       Show this screen.
  -v  --version    Show version.
  -a  --all        Scan all ports (Takes a while).
  -c  --common     Only scans the most commond ports.
  -d  --dns        DNS scan of the domain.

## Versioning

We use [SemVer](http://semver.org/) for versioning.

## Licence

[MIT Licence](LICENSE.md)

This program is intended for individuals to test their own equipment for weak security, and the author will take no responsibility if it is put to any other use.