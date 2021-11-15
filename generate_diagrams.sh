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

# Generate the PlantUML file from the dataset
./yaml2puml.py TOSCA-Implementation-Landscape.yaml

# Generate PlantUML diagrams
for format in png svg
do
  echo Generate TOSCA-Implementation-Landscape.${format}
  java -jar plantuml.jar -T${format} TOSCA-Implementation-Landscape.puml
done
