Summary:	Power saving diagnostic tool
Name:		powertop
Version:	1.98
Release:	1
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://www.lesswatts.org/
Source0:	http://www.kernel.org/pub/linux/status/powertop/%{name}-%{version}.tar.bz2
Patch0:		powertop-1.97-ncursesw.patch
Patch1:		powertop-1.98-to-git-9f1a713fe3f8befb951ab9163c720cc664895c43.patch
BuildRequires:	libncurses-devel
BuildRequires:	libncursesw-devel
BuildRequires:	libnl-devel pciutils-devel zlib-devel

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
%patch0 -p1 -b .ncursesw~
%patch1 -p1 -b .git~

%build
%setup_compile_flags
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc README TODO
%{_bindir}/%{name}
