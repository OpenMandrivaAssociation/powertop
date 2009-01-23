%define Werror_cflags %nil

%define name powertop
%define version 1.11
%define release %mkrel 1

Summary: Power saving diagnostic tool
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.linuxpowertop.org/download/%{name}-%{version}.tar.gz
Patch0: powertop-1.5-ncursesw.patch
License: GPLv2+
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
%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%doc README Changelog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
