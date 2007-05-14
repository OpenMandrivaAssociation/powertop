%define name powertop
%define version 1.1
%define release %mkrel 1

Summary: Power saving diagnostic tool
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.linuxpowertop.org/download/%{name}-%{version}.tar.bz2
License: GPL
Group: System/Kernel and hardware
Url: http://www.linuxpowertop.org/
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
%setup -q -n %{name}

%build
%make

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -m755 %{name} %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changelog
%{_bindir}/%{name}
