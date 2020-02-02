# Server tools

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ca70f4341eb04084b8beb5515fdd38c8)](https://app.codacy.com/manual/mikelsmartinez/server-tools?utm_source=github.com&utm_medium=referral&utm_content=sWallyx/server-tools&utm_campaign=Badge_Grade_Dashboard)

Scan the ports of your server or get the DNS records with this small scripts.

## Prerequisites

You only need two things to run the scripts Python3 and dnspython to install dnspython for python3 you can use pip3 or pip:

``` shell
pip3 install dnspython
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

[MIT - Licence](LICENSE)

This program is intended for individuals to test their own equipment for weak security, and the author will take no responsibility if it is put to any other use.
