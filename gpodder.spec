%define name	gpodder
%define version	0.12.0
%define svn 610
%define release %mkrel 2


Name: 	 	%{name}
Summary: 	A graphical podcast catcher
Version: 	%{version}
Release: 	%{release}
Source:		http://perli.net/projekte/gpodder/releases/%{version}/%{name}-%{version}.tar.gz
#Source:		http://perli.net/projekte/gpodder/releases/%{version}/%{name}-r%{svn}.tar.bz2
Patch: gpodder-r778-fix-ipod-sync.patch
URL:		http://www.perli.net/projekte/gpodder/
License:	GPL
Group:		Networking/News
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:  python-devel
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires:  help2man
Requires:	pygtk2.0 >= 2.6
Requires:       pygtk2.0-libglade
Requires:       python-feedparser
%if %mdkversion <= 200700
Requires:       python-sqlite2
%endif
# gw for iPod support:
Requires:	python-gpod
Requires:	pymad
Requires:	python-eyed3
# gw required for content length detection
Requires:	mplayer
# gw for transcoding and tagging Ogg Vorbis
Suggests:	vorbis-tools
Suggests:	lame
# gw for Bluetooth support
Suggests: bluez-utils bluez-gnome
BuildArch:	noarch

%description
gPodder is a Podcast reciever/catcher written in Python, using GTK. It manages
podcast feeds for you and automatically downloads all podcasts from as many
feeds as you like.

%prep
%setup -q
%patch

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %name
desktop-file-install --vendor="" \
  --add-category="GTK;Network;News" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
		
%postun
%clean_icon_cache hicolor

%files -f %name.lang
%defattr(-,root,root)
%doc ChangeLog README 
%{_bindir}/%name
%{_datadir}/%name
%{py_puresitedir}/%name
%{py_puresitedir}/*.egg-info
%{_mandir}/man1/*
%{_datadir}/applications/*
%_datadir/icons/hicolor/*/apps/gpodder.*
%{_datadir}/pixmaps/gpodd*.png


