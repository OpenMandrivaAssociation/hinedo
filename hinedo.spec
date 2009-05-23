Name: hinedo
Summary: Tray applet to listen Hinet radio
Version: 0.4
Release: %mkrel 1
License: GPLv2+
Group: Sound
Source: http://of.openfoundry.org/download_path/hinedo/2007.11.18/%name-%version.tar.bz2
Patch0: hinedo-0.4-makefile.patch
Patch1: hinedo-0.4-str-fmt.patch
URL: http://of.openfoundry.org/projects/814
BuildRequires: gtk+2-devel desktop-file-utils
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Requires: mplayer
Requires: python
Obsoletes: hinetradio

%description
Tray applet to listen Hinet radio.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0
%patch1 -p0

%build
%make CFLAGS="%optflags" LDFLAGS="%{?ldflags}"

%install
rm -fr %{buildroot}
%makeinstall_std CFLAGS="%optflags" LDFLAGS="%{?ldflags}"

desktop-file-install --vendor="" \
	--remove-category="Application" \
	--add-category="TrayIcon" \
	--add-only-show-in="KDE" \
	--add-only-show-in="GNOME" \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_prefix}/lib/hinedo/update

%clean
rm -rf %{buildroot}

