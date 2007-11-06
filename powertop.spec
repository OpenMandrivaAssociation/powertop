%define name powertop
%define version 1.9
%define release %mkrel 2

Summary: Power saving diagnostic tool
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.linuxpowertop.org/download/%{name}-%{version}.tar.gz
Patch0: powertop-1.5-ncursesw.patch
License: GPL
Group: System/Kernel and hardware
Url: http://www.linuxpowertop.org/
BuildRequires: libncursesw-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
PowerTOP tool is a program that collects the various pieces of
information from a system and presents an overview of how well a
laptop is doing in terms of power savings. In addition, PowerTOP will
provide an indication of which tunables and software components are
the biggest offenders in slurping up battery time. PowerTOP will
update it's display frequently so that the impact of any changes can
be seen directly.

%prep
%setup -q
%patch0 -p1 -b .ncursesw

%build
%make

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -m755 %{name} %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -m644 %{name}.1 %{buildroot}%{_mandir}/man1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changelog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
