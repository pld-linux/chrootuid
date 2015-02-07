Summary:	Runs Daemons with restricted File System Access
Name:		chrootuid
Version:	1.3
Release:	1
License:	BSD License
Group:		Applications
Source0:	http://ftp.porcupine.org/pub/security/%{name}%{version}.tar.gz
# Source0-md5:	15510abadf5de189e1c22a1544dc926a
Patch1:		http://ftp.debian.org/debian/pool/main/c/chrootuid/%{name}_1.3-6.diff.gz
# Patch1-md5:	5d2b52c59c6f915b973055375e9b0ec0
URL:		http://ftp.porcupine.org/pub/security/index.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Chrootuid makes it easy to run a network service at low privilege
level and with restricted file system access. At Eindhoven University
we use this program to run the gopher and www (world-wide web) network
daemons in a minimal environment: the daemons have access only to
their own directory tree, and run under a low-privileged userid. The
arrangement greatly reduces the impact of possible loopholes in daemon
software.

%prep
%setup -q -n %{name}%{version}
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -p chrootuid $RPM_BUILD_ROOT%{_bindir}
cp -p chrootuid.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean

%files
%defattr(644,root,root,755)
%doc README chrootuid_license
%attr(755,root,root) %{_bindir}/chrootuid
%{_mandir}/man1/chrootuid.1*
