#
# Conditional build:
%bcond_without	javadoc		# don't build javadoc

%define		srcname		regexp
Summary:	Java Regular Expression
Summary(pl.UTF-8):	Wyrażenia regularne do Javy
Name:		java-regexp
Version:	1.5
Release:	2
License:	Apache v2.0
Group:		Libraries/Java
Source0:	http://www.apache.org/dist/jakarta/regexp/source/jakarta-regexp-%{version}.tar.gz
# Source0-md5:	b941b8f4de297827f3211c2cb34af199
Patch0:		jakarta-regexp-build.patch
URL:		http://jakarta.apache.org/regexp/index.html
BuildRequires:	ant
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jre
Obsoletes:	jakarta-regexp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Regexp is a 100% Pure Java Regular Expression package that was
graciously donated to the Apache Software Foundation by Jonathan
Locke. This package is intended to be an answer to a question we
commonly hear in the Java world: "Why isn't there a decent regular
expression package available for Java under a BSD-Style (ie: Apache)
license?"

%description -l pl.UTF-8
Regexp to pakiet obsługujący wyrażenia regularne napisany całkowicie w
czystej Javie. Został on łaskawie podarowany Apache Software
Foundation przez Jonathana Locke. Ten pakiet ma być odpowiedzią na
pytanie często słyszane w świecie Javy: "dlaczego nie ma przyzwoitego
pakietu obsługującego wyrażenia regularne w Javie na licencji typu
BSD?".

%package javadoc
Summary:	Java Regular Expression API documentation
Summary(pl.UTF-8):	Dokumentacja API javowych wyrażeń regularnych
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	jakarta-regexp-doc
Obsoletes:	jakarta-regexp-javadoc

%description javadoc
Java Regular Expression API documentation.

%description javadoc -l pl.UTF-8
Dokumentacja API javowych wyrażeń regularnych.

%prep
%setup -q -n jakarta-regexp-%{version}
%patch -P0 -p1
find -name "*.jar" -exec rm -f {} \;

%build
unset CLASSPATH || :
export JAVA_HOME="%{java_home}"
%ant jar %{?with_javadoc:javadocs}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javadir}

install build/jakarta-regexp-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -sf %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

# javadoc
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -R docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%doc LICENSE docs/*.html docs/*.txt
%{_javadir}/regexp-%{version}.jar
%{_javadir}/regexp.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
%endif
