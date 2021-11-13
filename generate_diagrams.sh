#! /bin/sh

for format in [ png, svg]
do
  java -jar plantuml.jar -T${format} TOSCA-Implementation-Landscape.puml
done
