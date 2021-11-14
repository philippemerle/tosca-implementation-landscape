#! /bin/sh

for format in png svg
do
  echo Generating TOSCA-Implementation-Landscape.${format}
  java -jar plantuml.jar -T${format} TOSCA-Implementation-Landscape.puml
done
