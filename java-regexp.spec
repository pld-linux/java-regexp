Summary:	Java Regular Expression
Summary(pl.UTF-8):   Wyrażenia regularne do Javy
Name:		jakarta-regexp
Version:	1.4
Release:	2
License:	Apache v2.0
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/jakarta/regexp/source/%{name}-%{version}.tar.gz
# Source0-md5:	d903d84c949df848009f3bf205b32c97
Patch0:		%{name}-build.patch
URL:		http://jakarta.apache.org/regexp/index.html
BuildRequires:	ant
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jre
BuildArch:	noarch
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664} noarch
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
Summary(pl.UTF-8):   Dokumentacja API javowych wyrażeń regularnych
Group:		Development/Languages/Java
Requires:	jpackage-utils
Obsoletes:	jakarta-regexp-doc

%description javadoc
Java Regular Expression API documentation.

%description javadoc -l pl.UTF-8
Dokumentacja API javowych wyrażeń regularnych.

%prep
%setup -q
%patch0 -p1
find . -name "*.jar" -exec rm -f {} \;

%build
unset CLASSPATH || :
export JAVA_HOME="%{java_home}"
%ant jar javadocs

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_javadir},%{_javadocdir}/%{name}-%{version}}

install build/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/regexp.jar

cp -R docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE docs/*.html docs/*.txt
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%doc %{_javadocdir}/%{name}-%{version}
