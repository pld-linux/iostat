Summary:	Command line I/O performance monitoring utility
Summary(pl):	Dzia³aj±ce z linii poleceñ narzêdzie do monitorowania wydajno¶ci I/O
Name:		iostat
Version:	2.2
Release:	1
License:	unknown
Group:		Applications/System
Source0:	http://linux.inet.hr/%{name}-%{version}.tar.gz
# Source0-md5:	74725e956dabbae4e9742990fa19a944
URL:		http://linux.inet.hr/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
iostat is a command line I/O performance monitoring utility. It is
present in almost every major Unix flavor in use today, and here you
can get your version for Linux. It works on both 2.4 & 2.6. What makes
it different from other Linux utilities, which mostly show only I/O
transfer rates, is that you finally can get important information
about disk utilization, number of requests, average queue size and
disk & queue wait times. No serious sysadmin should be without it.

%description -l pl
iostat to dzia³aj±ce z linii poleceñ narzêdzie do monitorowania
wydajno¶ci wej¶cia/wyj¶cia. Jest dostêpne dla prawie ka¿dej u¿ywanej
obecnie wersji uniksa, a to jest wersja dla Linuksa. Dzia³a z 2.4 i
2.6. To, co ró¿ni je od innych narzêdzi linuksowych, przewa¿nie
pokazuj±cych tylko szybko¶æ transferu I/O, to podawanie wa¿nych
informacji o wykorzystaniu dysku, liczbie ¿±dañ, ¶rednim rozmiarze
kolejki oraz czasach oczekiwania dla dysku i kolejki. ¯aden powa¿ny
administrator systemów nie powinien pozostaæ bez tego narzêdzia.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

install iostat   $RPM_BUILD_ROOT%{_bindir}
install iostat.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*
