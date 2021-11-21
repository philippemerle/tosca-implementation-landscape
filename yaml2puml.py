#! /usr/bin/env python3
######################################################################
#
# TOSCA Implementation Landscape
# Copyright (c) 2021 Inria
#
# This software is distributed under the Apache License 2.0
# the text of which is available at http://www.apache.org/licenses/LICENSE-2.0
# or see the "LICENSE-2.0.txt" file for more details.
#
# Author: Philippe Merle <philippe.merle@inria.fr>
#
######################################################################

import sys
import yaml

# Mapping of activity levels to PlantUML colors
COLORS = {
    "ACTIVE": "PaleGreen",
    "SLEEPING": "Orange",
    "INACTIVE": "DarkRed",
    "UNKNOWN": "White",
}

# Iconifiable labels
ICONS = [
    "Eclipse",
    "GitHub",
    "SaaS",
    "Website",
]

# Criteria
CRITERIA = {
    "Status": None,
    "TOSCA":    { "sep": " + " },
    "Target":   { "sep": " + " },
    "Usage":    { "sep": " + " },
    "Nature":   { "sep": "\\n" },
    "Language": { "sep": " + " },
    "Links":    { "sep": " " },
}

# Mapping of relationships to PlantUML arrows
RELATIONSHIPS = {
    "contributes": "o--",
    "hosts": "*-up-",
    "uses": "..>",
    "plugins": "<..",
    "same ecosystem": "..",
    "applied to": "..up..>",
}

# Arrows to force the PlantUML layout
ARROWS_TO_FORCE_THE_LAYOUT = [
    "TOSCA_toolbox .up[hidden]. Cloudnet_TOSCA_Toolbox",
    "Heat_Translator .up[hidden]. tosca_parser",
    "Heat_Translator .up[hidden]. tosca_parser",
]

# Vertical layout of categories
LAYOUT_OF_CATEGORIES = [
    "Open Standards",
    "EU Funded Projects",
    "TOSCA Modeling Tools",
    "TOSCA Marketplaces",
    "TOSCA Orchestrators",
    "TOSCA Developer Tools",
    "Open Source Communities",
]

def to_id(label):
    for s in [' ', '.', '-']:
        label = label.replace(s, '_')
    return label

def serialize(data, iconable=False, sep=None):
    if isinstance(data, float):
        return str(data)
    elif isinstance(data, str):
        if iconable and data in ICONS:
            return "<img:icons/%s.png{scale=0.5}>" % data
        if data.endswith("\n"):
            data = data[:-1]
        return data.replace("\n", "\\n")
    elif isinstance(data, list):
        result = ''
        s = ''
        for d in data:
            if d != None:
                result += s + serialize(d, iconable=True)
                s = sep
            else:
                result += " +\\n"
                s = ''
        return result
    elif isinstance(data, dict):
        result = ''
        s = ''
        for k, v in data.items():
            result += s + "[[" + serialize(v, False) + " " + serialize(k, True) + "]]"
            s = sep
        return result

def generate_category(category_name, category_values, arrows, indent=''):
    print(indent, 'package "**%s**" as %s {' % (category_name, to_id(category_name)), sep='', file=output_stream)
    lindent = indent + "  "
    for impl_name, impl_values in category_values.items():
        if impl_name == "categories":
            for k, v in impl_values.items():
                generate_category(k, v, arrows, lindent)
            continue # skip to the next implementation
        status = impl_values["Status"]
        print(lindent, 'map "**%s**" as %s #%s {' % (impl_name, to_id(impl_name), COLORS[status]), sep='', file=output_stream)
        for criteria_name, criteria_value in impl_values.items():
            line = "  " + criteria_name + " => "
            if criteria_name == "Status":
                continue # skip it as already handled
            elif criteria_name in CRITERIA:
                line += serialize(criteria_value, sep=CRITERIA[criteria_name]["sep"])
            elif criteria_name in RELATIONSHIPS:
                source_id = to_id(impl_name)
                arrow = RELATIONSHIPS[criteria_name]
                for target in criteria_value:
                    arrows.append("%s %s %s : <<%s>>" % (source_id, arrow, to_id(target), criteria_name))
                continue # skip next print
            print(lindent, line, sep='', file=output_stream)
        print(lindent, "}", sep='', file=output_stream)
    print(indent, "}", sep='', file=output_stream)

# Main program
filename = sys.argv[1]
print("Load", filename)
with open(filename) as input_stream:
    dataset = yaml.load(input_stream)
filename = filename[:filename.rindex('.')] + ".puml"
print("Generate", filename)
with open(filename, 'w') as output_stream:
    print("@startuml", file=output_stream)
    print("Title **TOSCA Implementation Landscape**", file=output_stream)
    arrows = []
    for category_name, category_values in dataset.items():
        generate_category(category_name, category_values, arrows)
    arrows.extend(ARROWS_TO_FORCE_THE_LAYOUT)
    previous_category = LAYOUT_OF_CATEGORIES[0]
    for category in LAYOUT_OF_CATEGORIES[1:]:
        arrows.append("%s --[hidden]-- %s" % (to_id(previous_category), to_id(category)))
        previous_category = category
    for arrow in arrows:
        print(arrow, file=output_stream)
    print("@enduml", file=output_stream)
