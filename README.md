# TOSCA Implementation Landscape

The **TOSCA Implementation Landscape** is a visual representation of the list of [Known TOSCA Implementations](https://github.com/oasis-open/tosca-community-contributions/wiki/Known-TOSCA-Implementations) maintained by the OASIS TOSCA TC, see these [slides](https://www.oasis-open.org/committees/download.php/67709/TOSCA%20Webinar-2020-09-09.pdf) also.

The **TOSCA Implementation Landscape** was announced on [Twitter](https://twitter.com/merle_philippe/status/1459981831126798352) and [LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:6865756530646548480/).

## TOSCA Implementation Landscape

The **TOSCA Implementation Landscape** is depicted in the following big picture (click on it to enlarge it):

![TOSCA Implementation Landscape](https://raw.githubusercontent.com/philippemerle/tosca-implementation-landscape/main/TOSCA-Implementation-Landscape.png)

See also the [interactive version of the **TOSCA Implementation Landscape**](https://raw.githubusercontent.com/philippemerle/tosca-implementation-landscape/main/TOSCA-Implementation-Landscape.svg), i.e., SVG + hyperlinks.

Let's note that the **TOSCA Implementation Landscape** evolves day after day (see [history](https://github.com/philippemerle/tosca-implementation-landscape/commits/main/TOSCA-Implementation-Landscape.png)) because this landscape is **automatically generated** from this [dataset](TOSCA-Implementation-Landscape.yaml). So, [each commit on this dataset](https://github.com/philippemerle/tosca-implementation-landscape/commits/main/TOSCA-Implementation-Landscape.yaml) implies the regeneration of the **TOSCA Implementation Landscape**.

## Applied Methodology

The most crucial methodological points in any study are objectivity and exhaustivity. I did my best.

### Collecting the data set

I started from the list of [Known TOSCA Implementations](https://github.com/oasis-open/tosca-community-contributions/wiki/Known-TOSCA-Implementations) maintained by the OASIS TOSCA TC and reported in these [slides](https://www.oasis-open.org/committees/download.php/67709/TOSCA%20Webinar-2020-09-09.pdf). The entries in this list are sorted in the alphabetical order and are intrinsically heterogeneous.

In order to structure the TOSCA landscape, I gradually built a classification containing the following eight categories:
1. **Open Standards**: This groups open standards based on TOSCA. Exemplary standards are **ETSI GS NFV-SOL 001** and **TM Forum IG1176**.
2. **EU Funded Projects**: This groups European Union funded projects which have contributed to some TOSCA software tools. Exemplary projects are **CELAR**, **Indigo**, **RADON**, **SeaClouds**, and **SODALITE**. I discovered the missing **DICE** later during the study.
3. **TOSCA Modeling Tools**: This groups all TOSCA implementations providing a graphical interface (GUI) to design both TOSCA topology templates and types. Exemplary implementations are **Alien4Cloud**, **Cloud Topology Designer**, **DICER**, **Eclipse Winery**, and **EnterpriseWeb**. I discovered the missing **c-Eclipse** and **RADON IDE** later during the study.
4. **TOSCA Marketplaces**: This groups TOSCA specific places where CSARs can be imported, stored, and then proposed to TOSCA end-users. A CSAR could contain one TOSCA application (one topology template + application-specific types) or one TOSCA profile (a set of general-purpose TOSCA types). I discovered this category during the study and found only one market place currently, i.e., **xOpera Template Library**. No doubt, other marketplaces could emerge in the future.
5. **TOSCA Orchestrators**: As the category name clearly indicates, this groups all TOSCA orchestrators which automate the deployment of TOSCA topology templates on target environments.  This category contains a lot of the entries of the initial list, and there are so many exemplary orchestrators that I prefer to name none. But you should find your favorite orchestrator, shouldn't you?
6. **TOSCA Developer Tools**: This groups all other pieces of software to help the job of TOSCA developers, i.e. TOSCA parsers and TOSCA processors which are independent of any TOSCA orchestrator or modeling tool. Exemplary developer tools are the well-known OpenStack **tosca-parser** and my amazing [**TOSCA toolbox**](https://github.com/Orange-OpenSource/Cloudnet-TOSCA-toolbox) (I am not really objective on the latter:wink:).
7. **Open Source Communities**: This groups large open source projects which host (or should host) TOSCA software tools and orchestrators. The exemplary community is **OpenStack**.
8. **TOSCA Applications**: This groups TOSCA-based applications. An exemplary application is **kubetos**, a TOSCA framework to deploy Kubernetes.

TOSCA users should be mainly interested by the **TOSCA Modeling Tools**, **TOSCA Marketplaces**, **TOSCA Orchestrators**, and **TOSCA Developer Tools**. Following figure is depicted how these pieces of software interact:

![A journey with TOSCA](A%20journey%20with%20TOSCA.png)

The next step was to select a set of criteria to characterize each TOSCA implementation. This set should be smallest to ease the reading of this study but enough large to provide pertinent information to TOSCA users (you). The currently selected seven criteria are the following:

* **Activity**: This is the level of activities of a TOSCA implementation.  The four levels are:
  * **Active**: An implementation is tagged as active and is represented by a green map when observable activities (e.g. commits) were done during the last year. More than two-thirds of implementations are active.
  * **Sleeping**: An implementation is tagged as sleeping and is represented by an orange map when no activities (e.g. commits) were observed during the last year. They are just sleeping before coming back active or becoming inactive. Sleeping implementations are **JTOSCA**, **MSO4SC HPC**, **Sommelier**, **TORCH**, **TosKer**, and **TosKeriser**.
  * **Inactive**: An implementation is tagged as inactive and is represented by a red map when it was retired, completed, or had no commits since several years. **CELAR**, **DICE** and **SeaClouds** EU projects are completed since several years ago. **AriaTosca** orchestrator was retired on 2018. There are no commits on **c-Eclipse** and **DICER** since 2015 and 2018, respectively.
  * **Unknown**: For some TOSCA implementation, there is not enough publicly available information to determinate their level of activities. They are represented by white maps. Exemplary implementations are **EnterpriseWeb**, **Cisco NSO**, **CPLANE.ai**, and **Itential**.

* **TOSCA**: These are the TOSCA profile(s), i.e., `tosca_definitions_version` keyname, supported by the TOSCA implementation. For some implementations, this information was not found, so it is unknown. This is the case for **c-Eclipse**, **Cisco NSO**, **CPLANE.ai**, **EntrepriseWeb**, and **Itential** products. Some products added their proprietary profiles such as **Alien4Cloud** and **Unfurl**. Let's note that **Cloudify** only supports its own profiles.

* **Target**: This is the target environment(s) where deployments can be done with the TOSCA implementation. A TOSCA orchestrator could potentially target any cloud such as **Cloudify**, **MiCADOscale**, **OpenTOSCA**, **Opera**, **Ubicity Orchestrator** and **Yorc**. Some TOSCA orchestrator targets a specific runtime environment: **Tacker** targets OpenStack only, **Turandot** targets Kubernetes only and **TosKer** targets Docker only.

* **Usage**: This determinates how the end-user interacts with the TOSCA implementation, via a
  * **CLI**: Command-Line Interface (CLI).
  * **Webapp**: A web application deployed on the end-user environment.
  * **SaaS**: A Software-as-Service (SaaS) already deployed by a provider.

* **Nature**: A TOSCA implementation could be
  * **Commercial product**: The implementation or services around the implementation are sold by a commercial company (or several). Exemplary implementations are **Cloud Topology Designer**, **Cloudify** and **Ubicity Orchestrator**.
  * **Academia product**: The implementation is developed since several years by an academia research group. Exemplary implementations are **Cloudnet TOSCA Toolbox**, **Eclipse Winery** and **OpenTOSCA**.
  * **Academia prototype**: The implementation was prototyped as proof of concept of one (or a series of) academia scientific papers. Exemplary implementations are **MiCADOscale**, **Sommelier**, **TORCH**, **TosKer**, and **TosKeriser**.
  * **Open source**: The source code of the implementation is available in a public accessible code repository, such as GitHub for instance. A lot of implementations are open source, so I prefer to name none.

* **Language**: Only for open source implementations, this indicates the programming language(s) used to develop the open source product.
* **Links**: This takes the following values:
  * **![Website](icons/Website.png)**: This link points to the address of the official Web site of the TOSCA implementation.
  * **![Spec](icons/Spec.png)**: This link points to the specification document associated to the TOSCA implementation.
  * **![GitHub](icons/GitHub.png)**: This link points to the GitHub repository hosting the open source code for the TOSCA implementation.
  * **![Forge](icons/Forge.png)**: This link points to the forge repository hosting the open source code for the TOSCA implementation.
  * **![SaaS](icons/SaaS.png)**: This link points to the address where the Software-as-Service is deployed.

All these TOSCA implementations are part of a global TOSCA ecosystem. To understand this ecosystem, this is important to capture the relationships between these TOSCA implementations. Following lists six types of pertinent relationships (represented by tagged arrows in the big picture):
* **`<<contributes>>`**: An EU funded project contributed to the development of a TOSCA software tool. For instance, **RADON** EU project contributed to **OpenTOSCA** orchestrator.
* **`<<hosts>>`**: An open source community (or EU project) hosts a TOSCA implementation. For instance, **OpenStack** hosts **tosca-parser**, **Heat-Translator** and **Tacker** open source projects.
* **`<<uses>>`**: A source implementation uses another target implementation. For instance, **Alien4Cloud** modeling tool uses both **Cloudify** and **Yorc** as TOSCA orchestrators.
* **`<<plugins>>`**: A source implementation is a plugin of another target implementation. For instance, **MSO4SC HPC** is a plugin for **Cloudify** orchestrator.
* **`<<same ecosystem>>`**: Two independent TOSCA implementations are developed jointly. For instance, both **Eclipse Winery** and **OpenTOSCA** are developed by the same academia research group and **Sommelier**, **TosKer** and **TosKeriser** were developed by another academia research group.
* **`<<applied to>>`**: A source implementation is applied to another target implementation. For instance, my [**TOSCA toolbox**](https://github.com/Orange-OpenSource/Cloudnet-TOSCA-toolbox) was applied to all the examples provided by **kubetos** application, **AriaTosca**, **Khutulun**, **TORCH**, **TosKer**, **Turandot** and **xOpera Opera** orchestrators, and the **ETSI GS NFV-SOL 001** standard.

Following figure depicts a metamodel encompassing all these categories, criteria and relationships.

![Metamodel](metamodel.png)

Then, this metamodel is instantiated and filled: See the [TOSCA Implementation Landscape dataset](TOSCA-Implementation-Landscape.yaml).

Then, some statistics about the [dataset](TOSCA-Implementation-Landscape.yaml) were automatically computed. Have a look to [TOSCA Implementation Landscape statistics](TOSCA-Implementation-Landscape-statistics.md).

I hope this small classification, sets of both criteria and relationships could help you to select the TOSCA implementations that match both your business and technical requirements. Don't hesitate to propose/ask for other new helpful category/criteria/relationship.

### Generating the visual diagrams

Following figure depicts the overall generation process:
![Generation Process](Generation%20Process.png)

[PlantUML](https://plantuml.com) is used to generate the visual **TOSCA Implementation Landscape** diagrams from the collected data set.

To (re)generate these diagrams, let's type:
```sh
$ ./generate_diagrams.sh
```

Let's note that following required software need to be pre-installed:
* [Graphviz](https://graphviz.org/)
* [Java](https://www.java.com)
* [Python 3.x](https://www.python.org/) with [PyYAML](https://pypi.org/project/PyYAML/) installed

## Contributions

Any contribution such as adding a new TOSCA implementation, correcting any misinformation or adding new criteria is welcome. Please [create a new issue](https://github.com/philippemerle/tosca-implementation-landscape/issues/new) or pull request.
