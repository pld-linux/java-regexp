Summary:	Java Regular Expression
Summary(pl):	Wyra¿enia regularne do Javy
Name:		jakarta-regexp
Version:	1.2
Release:	3
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/jakarta/regexp/source/%{name}-%{version}.tar.gz
# Source0-md5:	73aa60b63da140b4a461b46c33082eec
URL:		http://jakarta.apache.org/regexp/index.html
BuildRequires:	jakarta-ant
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
Java Regular Expression.

%description -l pl
Wyra¿enia regularne do Javy.

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

install -d $RPM_BUILD_ROOT%{_javalibdir}
install bin/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javalibdir}
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javalibdir}/regexp.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc xdocs docs
