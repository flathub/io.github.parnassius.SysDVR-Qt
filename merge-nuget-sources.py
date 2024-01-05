#!/usr/bin/env python3

import json

with open("nuget-sources-arm64.json", encoding="utf-8") as fp:
    sources = json.load(fp)

with open("nuget-sources-x64.json", encoding="utf-8") as fp:
    for el in json.load(fp):
        if el not in sources:
            sources.append(el)

with open("nuget-sources.json", "w", encoding="utf-8") as fp:
    json.dump(
        sorted(sources, key=lambda n: n.get("dest-filename")),
        fp,
        indent=4
    )
