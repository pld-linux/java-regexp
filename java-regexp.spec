Summary:	Java Regular Expression
Summary(pl):	Wyra¿enia regularne do Javy
Name:		jakarta-regexp
Version:	1.3
Release:	1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/jakarta/regexp/source/%{name}-%{version}.tar.gz
# Source0-md5:	73aa60b63da140b4a461b46c33082eec
URL:		http://jakarta.apache.org/regexp/index.html
BuildRequires:	jakarta-ant
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Regexp is a 100% Pure Java Regular Expression package that was
graciously donated to the Apache Software Foundation by Jonathan
Locke. This package is intended to be an answer to a question we
commonly hear in the Java world: "Why isn't there a decent regular
expression package available for Java under a BSD-Style (ie: Apache)
license?"

%description -l pl
Regexp to pakiet obs³uguj±cy wyra¿enia regularne napisany ca³kowicie w
czystej Javie. Zosta³ on ³askawie podarowany Apache Software
Foundation przez Jonathana Locke. Ten pakiet ma byæ odpowiedzi± na
pytanie czêsto s³yszane w ¶wiecie Javy: "dlaczego nie ma przyzwoitego
pakietu obs³uguj±cego wyra¿enia regularne w Javie na licencji typu
BSD?".

%package doc
Summary:	Java Regular Expression documentation
Summary(pl):	Dokumentacja do javowych wyra¿eñ regularnych
Group:		Development/Languages/Java

%description doc
Java Regular Expression documentation.

%description doc -l pl
Dokumentacja do javowych wyra¿eñ regularnych.

%prep
%setup -q
find . -name "*.jar" -exec rm -f {} \;

%build
ant -buildfile build/build-regexp.xml jar javadocs

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javadir}
install bin/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/regexp.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%{_javadir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc xdocs docs
