Summary: 	Java Regular Expression
Summary(pl):	Wyra¿enia regularne do Javy
Name:		jakarta-regexp
Version:	1.2
Release:	1
License:	Apache Software License
Group:		Development/Languages/Java
Source0:	http://jakarta.apache.org/builds/%{name}/release/%{version}/%{name}-%{version}.tar.gz
URL:		http://jakarta.apache.org/regexp/index.html
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

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javalibdir}
install %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javalibdir}/regexp.jar

gzip -9nf LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc xdocs docs
