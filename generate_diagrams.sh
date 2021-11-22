#! /bin/sh
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

# Generate the Markdown-based statistics document
./statistics.py TOSCA-Implementation-Landscape.yaml

# Generate the PlantUML file from the dataset
./yaml2puml.py TOSCA-Implementation-Landscape.yaml

# Generate PlantUML diagrams
for filename in metamodel TOSCA-Implementation-Landscape
do
  for format in png svg
  do
    echo Generate ${filename}.${format}
    java -jar plantuml.jar -T${format} ${filename}.puml
  done
done
