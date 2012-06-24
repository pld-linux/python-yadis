
%define		module	yadis

Summary:	Python modules offering Yadis support
Summary(pl):	Modu�y Pythona oferuj�ce obs�ug� Yadis
Name:		python-%{module}
Version:	1.1.0
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://www.openidenabled.com/resources/downloads/python-openid/%{name}-%{version}.tar.gz
# Source0-md5:	dce07b08a54f28dfe17ed6601175409c
URL:		http://www.openidenabled.com/
BuildRequires:	python-devel
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements relying party support for the Yadis service
discovery protocol. The protocol was developed for use by
decentralized URL-based identity systems, but is useful for
advertising services provided by or on behalf of a certain URL.

To learn more about Yadis, see http://www.openidenabled.com/yadis

%description -l pl
Ten modu� implementuje obs�ug� cz�ci przekazuj�cej dla protoko�u
wykrywania us�ug Yadis. Protok� zosta� stworzony do u�ywania przez
zdecentralizowane systemy identyfikacji oparte na URL-ach, ale jest
przydatny do us�ug reklamowych udost�pnianych przez lub w imieniu
okre�lonego URL-a.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/*
%{py_sitescriptdir}/%{module}
