#! /usr/bin/env python3
######################################################################
#
# TOSCA Implementation Landscape
#
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

CATEGORIES = [
    "Open Standards",
    "EU Funded Projects",
    "TOSCA Modeling Tools",
    "TOSCA Marketplaces",
    "TOSCA Orchestrators",
    "TOSCA Developer Tools",
    "TOSCA Parsers",
    "Open Source Communities",
]

CRITERIA = {
    "Status" : [
        "ACTIVE",
        "SLEEPING",
        "INACTIVE",
        "UNKNOWN"
    ],
    "TOSCA" : [
        "Any",
        "XML",
        1.0,
        "NFV 1.0",
        1.1,
        1.2,
        1.3,
        2.0,
        "Alien DSL",
        "Cloudify DSL",
        "OpenStack Heat",
        "Unfurl DSL",
        "Unknown",
    ],
    "Target": [
        "Model-Driven Automation",
        "NFV",
        "Any cloud",
        "Azure",
        "Docker",
        "Docker Swarm",
        "Kubernetes",
        "OpenStack",
        "Open Telekom Cloud",
        "Unknown"
     ],
    "Usage": [
        "Library",
        "CLI",
        "Eclipse",
        "Webapp",
        "SaaS",
        "Unknown",
    ],
    "Nature": [
        "Commercial product",
        "Academia product",
        "Academia prototype",
        "Open source",
    ],
    "Language": [
        "Go",
        "Java",
        "JavaScript",
        "Php",
        "Python",
        "Unknown",
    ],
    "Links": [
        "Forge",
        "GitHub",
        "SaaS",
        "Spec",
        "Website",
        "Unknown",
    ]
}

RELATIONSHIPS = {
    "contributes": {
        "key": None,
    },
    "hosts": {
        "key": None
    },
    "uses": {
        "key": "Used by"
    },
    "same ecosystem": {
        "key": None
    },
    "plugins": {
        "key": None
    },
    "applied to": {
        "key": None
    },
}

class Statistics(object):
    def compute(self, dataset):
        self.implementations = {}
        self.by_categories = { key: [] for key in CATEGORIES }
        self.by_criteria = { key: [] for key in CRITERIA }
        for key, value in CRITERIA.items():
            self.by_criteria[key] = { k: [] for k in value }
        self.by_relationships = { k: {} for k in RELATIONSHIPS }
        self.visit_categories(dataset)

    def visit_categories(self, categories):
        for category_name, category_value in categories.items():
            self.by_categories[category_name] = []
            for implementation_name, implementation_value in category_value.items():
                if implementation_name == "categories":
                    self.visit_categories(implementation_value)
                    continue # skip to next implementation
                self.implementations[implementation_name] = implementation_value
                self.by_categories[category_name].append(implementation_name)
                for entry_name, entry_value in implementation_value.items():
                    if entry_name in CRITERIA:
                        if entry_name not in self.by_criteria:
                            self.by_criteria[entry_name] = {}
                        criteria = self.by_criteria[entry_name]
                        self.visit_value(criteria, entry_value, implementation_name)
                    elif entry_name in RELATIONSHIPS:
                        if entry_name not in self.by_relationships:
                            self.by_relationships[entry_name] = []
                        self.visit_value(self.by_relationships[entry_name],
                                         entry_value,
                                         implementation_name,
                                         RELATIONSHIPS[entry_name]["key"])

    def visit_value(self, criteria, criteria_value,
                    implementation_name, list_mode=True):
        if isinstance(criteria_value, (float, str)):
            if criteria_value not in criteria:
                criteria[criteria_value] = []
            criteria[criteria_value].append(implementation_name)
        elif isinstance(criteria_value, list):
            for value in criteria_value:
                if value is not None:
                    if list_mode:
                        self.visit_value(criteria, value, implementation_name)
                    else:
                        self.visit_value(criteria, implementation_name, value)
        elif isinstance(criteria_value, dict):
            for k, v in criteria_value.items():
                if k not in criteria:
                    criteria[k] = []
                self.visit_value(criteria, k, implementation_name)

    def report(self, ostream):
        print("# Overall statistics", file=ostream)
        print(file=ostream)
        print("|                 |  #  |", file=ostream)
        print("|---              |---  |", file=ostream)
        print("| Implementations |", len(self.implementations), "|", file=ostream)
        print("| Categories      |", len(self.by_categories), "|", file=ostream)
        print("| Criteria        |", len(self.by_criteria), "|", file=ostream)
        print("| Relationships   |", len(self.by_relationships), "|", file=ostream)
        print(file=ostream)
        print("# Statistics by categories", file=ostream)
        print(file=ostream)
        print("| Category                  |  #  | Implementations |", file=ostream)
        print("|---                        |---  |---              |", file=ostream)
        for key, value in self.by_categories.items():
            print("|", key, "|", len(value), "|", self.stringify_list(value), "|", file=ostream)
        print(file=ostream)
        print("# Statistics by criteria", file=ostream)
        print(file=ostream)
        for key, value in self.by_criteria.items():
            print("##", key, file=ostream)
            print(file=ostream)
            print("|   Value   |  #  | Implementations |", file=ostream)
            print("|---        |---  |---              |", file=ostream)
            for k, v in value.items():
                print("|", k, "|", len(v), "|", self.stringify_list(v), "|", file=ostream)
            print(file=ostream)
        print("# Statistics by relationships", file=ostream)
        print(file=ostream)
        for key, value in self.by_relationships.items():
            print("## \<\<`", key, "`\>\>", file=ostream)
            print(file=ostream)
            colunm_title = RELATIONSHIPS[key].get("key") or "Implementations"
            print("|   Implementation   |  #  |", colunm_title, "|", file=ostream)
            print("|---        |---  |---              |", file=ostream)
            for k, v in value.items():
                print("|", k, "|", len(v), "|", self.stringify_list(v), "|", file=ostream)
            print(file=ostream)

    def stringify_list(self, a_list):
        result = ""
        sep = ""
        for item in a_list:
            result += sep + item
            implementation = self.implementations[item]
            for k, v in implementation.get("Links", {}).items():
                result += " [![%s](icons/%s.png)](%s)" % (k, k, v)
            sep = "<br>"
        return result

# Main program

filename = sys.argv[1]

print("Load", filename)
with open(filename) as input_stream:
    dataset = yaml.load(input_stream)

statistics = Statistics()
statistics.compute(dataset)

filename = filename[:filename.rindex('.')] + "-statistics.md"
print("Generate", filename)
with open(filename, 'w') as output_stream:
    statistics.report(output_stream)
