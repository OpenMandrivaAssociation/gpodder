%define name	gpodder
%define version	2.8
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	A graphical podcast catcher
Version: 	%{version}
Release: 	%{release}
Source:		http://download.berlios.de/gpodder/%{name}-%{version}.tar.gz
URL:		http://www.perli.net/projekte/gpodder/
#gw SimpleGladeApp is LGPL
License:	GPLv3+ and LGPLv2+
Group:		Networking/News
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:  python-devel
BuildRequires:  python-feedparser
BuildRequires:	python-mygpoclient
BuildRequires:  imagemagick
BuildRequires:  desktop-file-utils
BuildRequires:  help2man
BuildRequires:  intltool
Requires:	pygtk2.0 >= 2.6
Requires:       pygtk2.0-libglade
Requires:       python-feedparser
%if %mdkversion <= 200700
Requires:       python-sqlite2
%endif
# gw for iPod support:
Requires:	python-gpod
#gw MTP player support:
Requires:	python-pymtp
Requires:	python-mygpoclient >= 1.4
Requires:	pymad
Requires:	python-eyed3
# gw required for content length detection
Requires:	mplayer
# gw required for HTML show notes
Requires: python-webkitgtk
# gw for transcoding and tagging Ogg Vorbis
Suggests:	vorbis-tools
Suggests:	lame
# gw for Bluetooth support
Suggests: bluez-utils bluez-gnome
#gw for rockbox cover support
Suggests: python-imaging
BuildArch:	noarch

%description
gPodder is a Podcast reciever/catcher written in Python, using GTK. It manages
podcast feeds for you and automatically downloads all podcasts from as many
feeds as you like.

%prep
%setup -q
%apply_patches

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %name
desktop-file-install --vendor="" \
  --add-category="GTK;Network;News" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdvver < 200900
%post
%update_icon_cache hicolor
%postun
%clean_icon_cache hicolor
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc README 
%{_bindir}/gpo
%{_bindir}/gpodder-backup
%{_bindir}/%name
%_datadir/dbus-1/services/org.gpodder.service
%{_datadir}/%name
%{py_puresitedir}/%name
%{py_puresitedir}/*.egg-info
%{_mandir}/man1/*
%{_datadir}/applications/*
%_datadir/icons/hicolor/*/apps/gpodder.*
%{_datadir}/pixmaps/gpodd*.png


