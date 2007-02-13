Summary:	Command line I/O performance monitoring utility
Summary(pl.UTF-8):	Działające z linii poleceń narzędzie do monitorowania wydajności I/O
Name:		iostat
Version:	2.2
Release:	1
License:	GPL v2
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

%description -l pl.UTF-8
iostat to działające z linii poleceń narzędzie do monitorowania
wydajności wejścia/wyjścia. Jest dostępne dla prawie każdej używanej
obecnie wersji uniksa, a to jest wersja dla Linuksa. Działa z 2.4 i
2.6. To, co różni je od innych narzędzi linuksowych, przeważnie
pokazujących tylko szybkość transferu I/O, to podawanie ważnych
informacji o wykorzystaniu dysku, liczbie żądań, średnim rozmiarze
kolejki oraz czasach oczekiwania dla dysku i kolejki. Żaden poważny
administrator systemów nie powinien pozostać bez tego narzędzia.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
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
