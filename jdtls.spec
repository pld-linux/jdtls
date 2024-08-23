Summary:	Java language server
Name:		jdtls
Version:	1.38.0
Release:	1
License:	EPL v2.0
Group:		Development/Languages/Java
Source0:	https://www.eclipse.org/downloads/download.php?file=/jdtls/milestones/%{version}/jdt-language-server-%{version}-202408011337.tar.gz
# Source0-md5:	a4a5739cad5c9720e8e4d8c885238bfd
URL:		https://projects.eclipse.org/projects/eclipse.jdt.ls
Requires:	jdk >= 17
Requires:	python3 >= 1:3.9
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Eclipse JDT Language Server is a Java language specific
implementation of the Language Server Protocol and can be used with
any editor that supports the protocol, to offer good support for the
Java Language.

%prep
%setup -q -c

%{__sed} -i -e '1 s,#!.*env python.*,#!%{__python3},' bin/jdtls

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/bin}
ln -sf %{_datadir}/%{name}/bin/jdtls $RPM_BUILD_ROOT%{_bindir}/jdtls

cp -p bin/jdtls{,.py} $RPM_BUILD_ROOT%{_datadir}/%{name}/bin
cp -rp config*linux* features plugins $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jdtls
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/bin
%attr(755,root,root) %{_datadir}/%{name}/bin/jdtls
%{_datadir}/%{name}/bin/jdtls.py
%{_datadir}/%{name}/config*linux*
%{_datadir}/%{name}/features
%{_datadir}/%{name}/plugins
