Summary: 	Java Regular Expression
Name:		jakarta-regexp
Version:	1.2
Release:	1
License:	Apache Software License
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Source0:	http://www.apache.org/dist/jakarta/%{name}/release/%{version}/%{name}-%{version}.tar.gz
URL:		http://jakarta.apache.org/regexp/index.html
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
Java Regular Expression

%package doc
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Summary:	Java Regular Expression documentation

%description doc
Java Regular Expression documentation

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_javalibdir}
cp %{name}-%{version}.jar $RPM_BUILD_ROOT/%{_javalibdir}/regexp.jar

gzip -9nf LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%dir %{_javalibdir}
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc xdocs docs
