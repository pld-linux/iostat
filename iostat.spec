Summary:	Command line I/O performance monitoring utility
Name:		iostat
Version:	2.0
Release:	1
License:	unknown
Group:		Applications/System
Source0:	http://linux.inet.hr/%{name}-%{version}.tar.gz
# Source0-md5:	11f0c7e04ce17967fa9ea0259f53ea94
URL:		http://linux.inet.hr/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
iostat is a command line I/O performance monitoring utility. It is present
in almost every major Unix flavor in use today, and here you can get your
version for Linux. It works on both 2.4 & 2.6. What makes it different from
other Linux utilities, which mostly show only I/O transfer rates, is that
you finally can get important information about disk utilization, number of
requests, average queue size and disk & queue wait times. No serious
sysadmin should be without it. Check the screenshots to learn more.


%prep
%setup -q

%build
%{__make} CFLAGS="%{rpmcflags}"

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
