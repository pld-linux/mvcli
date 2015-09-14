Summary:	MSU (Marvell Storage Utility).
Name:		mvcli
Version:	4.1.0.2019
Release:	1
License:	?
Group:		Base
Source0:	http://datoptic.com/Download/LINUXMSU%{version}.rar
# NoSource0-md5:	64c48649acd838d1a8f013fad8ad8287
NoSource:	0
URL:		http://www.marvell.com/support/
BuildRequires:	rpm-utils
BuildRequires:	unrar
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MSU (Marvell Storage Utility) is a storage management tool applied to
Marvell HBA products.

%prep
%setup -qcT
unrar x %{SOURCE0}
%ifarch %{ix86}
arch=i386
%endif
%ifarch %{x8664}
arch=x86_64
%endif

SOURCE=%{version}/MSU-%{version}-1.$arch.rpm
rpm2cpio $SOURCE | cpio -i -d

mv %{version}/*.txt .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_libdir}}

install -p %{_lib}/libmvraid.so $RPM_BUILD_ROOT%{_libdir}
install -p opt/marvell/storage/cli/mvcli $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_sbindir}/mvcli
%attr(755,root,root) %{_libdir}/libmvraid.so
