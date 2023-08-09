#!/usr/bin/env bash

yq "(.items[] | select(.kind == \"Job\") | .metadata.name) += \"-$(git rev-parse --short HEAD)\"" < /dev/stdin
