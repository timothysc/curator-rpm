%global namedreltag -incubating
%global namedversion %{version}%{?namedreltag}
Name:          curator
Version:       2.2.0
Release:       1%{?dist}
Summary:       A set of Java libraries that make using Apache ZooKeeper much easier
License:       ASL 2.0
URL:           http://curator.incubator.apache.org/
Source0:       http://www.apache.org/dist/incubator/%{name}/%{namedversion}/apache-%{name}-%{namedversion}-source-release.zip
# Fix test deps
Patch0:        %{name}-2.2.0-jetty9.patch
Patch1:        %{name}-2.2.0-commons-math3.patch

BuildRequires: java-devel
# guava 14.0.1
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.google.inject:guice)
BuildRequires: mvn(javax.ws.rs:jsr311-api)
BuildRequires: mvn(org.apache.commons:commons-math3)
BuildRequires: mvn(org.apache.zookeeper:zookeeper)
BuildRequires: mvn(org.codehaus.jackson:jackson-mapper-asl)
BuildRequires: mvn(org.javassist:javassist)
BuildRequires: mvn(org.slf4j:slf4j-api)

# Test deps
BuildRequires: mvn(com.sun.jersey:jersey-client)
BuildRequires: mvn(com.sun.jersey:jersey-core)
BuildRequires: mvn(com.sun.jersey:jersey-server)
BuildRequires: mvn(com.sun.jersey:jersey-servlet)
BuildRequires: mvn(log4j:log4j)
BuildRequires: mvn(org.eclipse.jetty:jetty-server)
BuildRequires: mvn(org.eclipse.jetty:jetty-servlet)
# resteasy 2.3.0.GA
BuildRequires: mvn(org.jboss.resteasy:resteasy-jaxrs)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.scannotation:scannotation)
BuildRequires: mvn(org.testng:testng)

BuildRequires: maven-local
BuildRequires: maven-doxia-module-confluence
BuildRequires: maven-plugin-bundle
BuildRequires: maven-remote-resources-plugin
BuildRequires: maven-site-plugin

BuildArch:     noarch

%description
Curator is a set of Java libraries that
make using Apache ZooKeeper much easier.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n apache-%{name}-%{namedversion}
find . -name "*.class" -print -delete
find . -name "*.jar" -print -delete

%patch0 -p1
%patch1 -p1

# disable cause build failure
%pom_remove_plugin :maven-license-plugin

%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId = 'scannotation' ]/pom:groupId" org.scannotation %{name}-x-discovery-server

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc DISCLAIMER LICENSE NOTICE README

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu Oct 10 2013 gil cattaneo <puntogil@libero.it> 2.2.0-1
- initial rpm