# TOSCA Implementation Landscape

The **TOSCA Implementation Landscape** is a visual representation of the list of [Known TOSCA Implementations](https://github.com/oasis-open/tosca-community-contributions/wiki/Known-TOSCA-Implementations) maintained by the OASIS TOSCA TC, see these [slides](https://www.oasis-open.org/committees/download.php/67709/TOSCA%20Webinar-2020-09-09.pdf) also.

## TOSCA Implementation Landscape

The **TOSCA Implementation Landscape** is depicted in the following big picture:

![TOSCA Implementation Landscape](TOSCA-Implementation-Landscape.png)

See also the [interactive version of the **TOSCA Implementation Landscape**](TOSCA-Implementation-Landscape.svg), i.e., SVG + hyperlinks.

## Applied Methodology

The most crucial methodological points in any study are objectivity and exhaustivity. I did my best. 

### Collecting the data set

I started from the list of [Known TOSCA Implementations](https://github.com/oasis-open/tosca-community-contributions/wiki/Known-TOSCA-Implementations) maintained by the OASIS TOSCA TC and reported in these [slides](https://www.oasis-open.org/committees/download.php/67709/TOSCA%20Webinar-2020-09-09.pdf). The entries in this list are sorted in the alphabetical order and are intrinsically heterogeneous.

In order to structure the TOSCA landscape, I gradually built a classification containing the following six categories:
1. **EU Funded Projects**: This groups European Union funded projects which are have contributed to some TOSCA software tools. Examplary projects are **CELAR**, **Indigo**, **RADON**, **SeaClouds**, and **SODALITE**. I discovered the missing **DICE** later during the study.   
2. **TOSCA Modeling Tools**: This groups all TOSCA implementations providing a graphical interface (GUI) to design both TOSCA topology templates and types. Examplary implementations are **Alien4Cloud**, **Cloud Topology Designer**, **DICER**, **Eclipse Winery**, and **EnterpriseWeb**. I discovered the missing **DICE** and **RADON IDE** later during the study.
3. **TOSCA Marketplaces**: This groups TOSCA specific places where CSARs can be imported, stored, and then proposed to TOSCA end-users. I discovered this category during the study and found only one market place currently, i.e., **xOpera Template Library**. No doubt, other marketplaces could emerge in the future.
4. **TOSCA Orchestrators**: As the category name clearly indicates, this groups all TOSCA orchestrators which automate the deployment of TOSCA topology templates.  This category contains a lot of the entries of the initial list, and there are so many examplary orchestrators that I prefer to name none. But you should find your favorite orchestrator, shouldn't you?
5. **TOSCA Developer Tools**: This groups all other software to help the job of TOSCA developers, i.e. TOSCA parsers and TOSCA processors which are independent of any TOSCA orchestrator or modeling tool. Examplary tools are the well-known OpenStack **tosca-parser** and my amazing [**TOSCA toolbox**](https://github.com/Orange-OpenSource/Cloudnet-TOSCA-toolbox) (I am not really objective on the latter).
6. **Open Source Communities**: This groups large open source projects which host (or should host) TOSCA software tools and orchestrators. The examplary community is **OpenStack**.

TOSCA users should be mainly interested by the **TOSCA Modeling Tools**, **TOSCA Marketplaces**, **TOSCA Orchestrators**, and **TOSCA Developer Tools**. Following figure is depicted how these pieces of software interact:

![A journey with TOSCA](A%20journey%20with%20TOSCA.png)

### Generating the visual diagrams

[PlantUML](https://plantuml.com) is used to generate the visual **TOSCA Implementation Landscape** diagrams from the collected data set.

To (re)generate these diagrams, let's type:
```sh
$ ./generate_diagrams.sh
```

Let's note that following required software need to be pre-installed:
* [Java](https://www.java.com)
* [Graphviz](https://graphviz.org/)

## Contributions

Any contribution (e.g., adding a new TOSCA implementation, correcting any misinformation or adding new criteria) is welcome. Please, [create a new issue](https://github.com/philippemerle/tosca-implementation-landscape/issues/new) or pull request.
