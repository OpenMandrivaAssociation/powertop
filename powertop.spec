%define Werror_cflags %nil

Summary:	Power saving diagnostic tool
Name:		powertop
Version:	1.97
Release:	%mkrel 1
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://www.linuxpowertop.org/
Source0:	http://www.kernel.org/pub/linux/status/powertop/%{name}-%{version}.tar.bz2
Patch0:		powertop-1.97-ncursesw.patch
BuildRequires:	libncursesw-devel
BuildRequires:	libnl-devel pciutils-devel zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%setup_compile_flags
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%doc README
%{_bindir}/%{name}
