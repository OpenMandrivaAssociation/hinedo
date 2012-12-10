Name: hinedo
Summary: Tray applet to listen Hinet radio
Version: 0.4
Release: 2
License: GPLv2+
Group: Sound
Source0: http://of.openfoundry.org/download_path/hinedo/2007.11.18/%name-%version.tar.bz2
Patch0: hinedo-0.4-makefile.patch
Patch1: hinedo-0.4-str-fmt.patch
patch2:	hinedo-0.4.nostrip.patch
URL: http://of.openfoundry.org/projects/814
BuildRequires: pkgconfig(gtk+-2.0) desktop-file-utils
Requires: mplayer
Requires: python
Obsoletes: hinetradio

%description
Tray applet to listen Hinet radio.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0
%patch1 -p0
%patch2 -p1 -b .nostrip

%build
%make CFLAGS="%optflags" LDFLAGS="%{?ldflags} -lX11"

%install
%makeinstall_std CFLAGS="%optflags" LDFLAGS="%{?ldflags} -lX11"

desktop-file-install --vendor="" \
	--remove-category="Application" \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_prefix}/lib/hinedo/update



%changelog
* Sun May 24 2009 Funda Wang <fwang@mandriva.org> 0.4-2mdv2010.0
+ Revision: 379122
- drop desktop environment

* Sat May 23 2009 Funda Wang <fwang@mandriva.org> 0.4-1mdv2010.0
+ Revision: 378883
- import hinedo


