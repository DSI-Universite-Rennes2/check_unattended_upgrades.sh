[![Build Status](https://travis-ci.org/Josef-Friedrich/check_unattended_upgrades.svg?branch=master)](https://travis-ci.org/Josef-Friedrich/check_unattended_upgrades)

# check_unattended_upgrades

Forked from https://github.com/Josef-Friedrich/check_unattended_upgrades and reverted to maintain bash version with minimal dependencies

## Summary / Short description

> Monitoring plugin with minimal dependencies to check automatic updates (unattended-upgrades) on Debian GNU Linux or derivative distributions like Ubuntu, Linux Mint etc.

## Usage

First and before : verify the user who run the check have read rights on /var/log/unattended-upgrades/unattended-upgrades.log

## Project pages

* https://github.com/DSI-Universite-Rennes2/check_unattended_upgrades
* https://github.com/Josef-Friedrich/check_unattended_upgrades (Original project, in python now)

## Testing

```
make test
```

