Summary:	Power saving diagnostic tool
Name:		powertop
Version:	2.3
Release:	1
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://www.lesswatts.org/
Source0:	https://01.org/powertop/sites/default/files/downloads/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(libpci)
BuildRequires:	pkgconfig(libnl-3.0)
BuildRequires:	pkgconfig(zlib)

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

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc README TODO
%{_sbindir}/%{name}
%{_mandir}/*/*.*
