%define name	gpodder
%define version	3.1.1
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	A graphical podcast catcher
Version: 	%{version}
Release: 	%{release}
Source:		http://gpodder.org/src/%{name}-%{version}.tar.gz
URL:		http://gpodder.org/
#gw SimpleGladeApp is LGPL
License:	GPLv3+ and LGPLv2+
Group:		Networking/News
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:  python-devel
BuildRequires:  python-feedparser >= 5.0.1
BuildRequires:	python-mygpoclient
BuildRequires:  imagemagick
BuildRequires:  desktop-file-utils
BuildRequires:  help2man
BuildRequires:  intltool
BuildRequires:	python-mygpoclient >= 1.4
Requires:	pygtk2.0 >= 2.6
Requires:       pygtk2.0-libglade
Requires:       python-feedparser >= 5.0.1
%if %mdkversion <= 200700
Requires:       python-sqlite2
%endif
Requires:	python-mygpoclient >= 1.4
# gw required for HTML show notes
Requires: python-webkitgtk
# gw for Bluetooth support
Suggests: bluez-utils bluez-gnome
BuildArch:	noarch

%description
gPodder is a Podcast reciever/catcher written in Python, using GTK. It manages
podcast feeds for you and automatically downloads all podcasts from as many
feeds as you like.

%prep
%setup -q
%apply_patches
#gw fix directory structure:
cd share/icons/hicolor
for dir in *x*;do
(cd $dir;mkdir apps;mv *.png apps)
done

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %name
desktop-file-install --vendor="" \
  --add-category="GTK;Network;News" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc README 
%{_bindir}/gpo
%{_bindir}/gpodder-migrate2tres
%{_bindir}/%name
%_datadir/dbus-1/services/org.gpodder.service
%{_datadir}/%name
%{py_puresitedir}/%name
%{py_puresitedir}/*.egg-info
%{_mandir}/man1/*
%{_datadir}/applications/*
%_datadir/icons/hicolor/*/apps/gpodder.*


