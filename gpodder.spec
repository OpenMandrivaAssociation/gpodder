%define name	gpodder
%define version	3.2.0
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




%changelog
* Mon Aug 27 2012 Götz Waschk <waschk@mandriva.org> 3.2.0-1mdv2012.0
+ Revision: 815861
- remove build workaround
- update to new version 3.2.0

* Tue May 29 2012 Götz Waschk <waschk@mandriva.org> 3.1.2-1
+ Revision: 801047
- update to new version 3.1.2

* Mon Apr 30 2012 Götz Waschk <waschk@mandriva.org> 3.1.1-1
+ Revision: 794586
- update to new version 3.1.1

* Tue Mar 27 2012 Götz Waschk <waschk@mandriva.org> 3.1.0-1
+ Revision: 787498
- fix icon installation
- update file list
- new version

* Wed Jan 25 2012 Götz Waschk <waschk@mandriva.org> 3.0.4-1
+ Revision: 768182
- update to new version 3.0.4

* Tue Jan 10 2012 Götz Waschk <waschk@mandriva.org> 3.0.3-1
+ Revision: 759317
- new version

* Wed Dec 14 2011 Götz Waschk <waschk@mandriva.org> 3.0.2-1
+ Revision: 740899
- new version

* Mon Nov 14 2011 Götz Waschk <waschk@mandriva.org> 3.0.1-1
+ Revision: 730646
- update to new version 3.0.1

* Mon Nov 07 2011 Götz Waschk <waschk@mandriva.org> 3.0.0-1
+ Revision: 725777
- new version
- remove old deps
- update URL

* Wed Oct 19 2011 Götz Waschk <waschk@mandriva.org> 2.20-1
+ Revision: 705439
- update to new version 2.20

* Fri Sep 16 2011 Götz Waschk <waschk@mandriva.org> 2.19-1
+ Revision: 699992
- update to new version 2.19

* Mon Aug 08 2011 Götz Waschk <waschk@mandriva.org> 2.18-1
+ Revision: 693669
- new version

* Thu Aug 04 2011 Götz Waschk <waschk@mandriva.org> 2.17-1
+ Revision: 693210
- update to new version 2.17

* Mon Jul 11 2011 Götz Waschk <waschk@mandriva.org> 2.16-1
+ Revision: 689477
- update to new version 2.16

* Tue May 03 2011 Götz Waschk <waschk@mandriva.org> 2.15-1
+ Revision: 664983
- update to new version 2.15

* Tue Apr 05 2011 Götz Waschk <waschk@mandriva.org> 2.14-1
+ Revision: 650677
- update to new version 2.14

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 2.13-2
+ Revision: 640438
- rebuild to obsolete old packages

* Sun Feb 20 2011 Götz Waschk <waschk@mandriva.org> 2.13-1
+ Revision: 638975
- update to new version 2.13

* Wed Jan 12 2011 Götz Waschk <waschk@mandriva.org> 2.12-1
+ Revision: 630960
- update to new version 2.12

* Mon Dec 20 2010 Funda Wang <fwang@mandriva.org> 2.11-1mdv2011.0
+ Revision: 623241
- new version 2.11

* Sun Nov 28 2010 Götz Waschk <waschk@mandriva.org> 2.10-1mdv2011.0
+ Revision: 602428
- update to new version 2.10

* Tue Nov 02 2010 Funda Wang <fwang@mandriva.org> 2.9-2mdv2011.0
+ Revision: 591743
- BR python-mygpoclient

  + Michael Scherer <misc@mandriva.org>
    - rebuild for python 2.7

* Sun Oct 10 2010 Götz Waschk <waschk@mandriva.org> 2.9-1mdv2011.0
+ Revision: 584842
- update to new version 2.9

* Sun Aug 29 2010 Götz Waschk <waschk@mandriva.org> 2.8-1mdv2011.0
+ Revision: 574112
- update to new version 2.8

* Sat Jul 10 2010 Götz Waschk <waschk@mandriva.org> 2.7-1mdv2011.0
+ Revision: 550267
- new version
- bump mygpoclient dep
- depend on python binding for webkit instead of gtkhtml

* Wed Apr 21 2010 Götz Waschk <waschk@mandriva.org> 2.5-1mdv2010.1
+ Revision: 537419
- update to new version 2.5

* Mon Mar 29 2010 Götz Waschk <waschk@mandriva.org> 2.4-1mdv2010.1
+ Revision: 528735
- new version
- drop patch
- suggest PIL for rockbox cover support

* Mon Mar 08 2010 Götz Waschk <waschk@mandriva.org> 2.3-2mdv2010.1
+ Revision: 515898
- remove old dep on pybluez

* Sat Feb 27 2010 Götz Waschk <waschk@mandriva.org> 2.3-1mdv2010.1
+ Revision: 512505
- update to new version 2.3

* Fri Feb 05 2010 Götz Waschk <waschk@mandriva.org> 2.2-1mdv2010.1
+ Revision: 501260
- update build deps
- new version
- drop patch
- add dbus service to the file list
- add dep on mygpoclient

* Thu Feb 04 2010 Götz Waschk <waschk@mandriva.org> 2.1-2mdv2010.1
+ Revision: 500721
- patch for new gtk

* Sat Dec 12 2009 Götz Waschk <waschk@mandriva.org> 2.1-1mdv2010.1
+ Revision: 477822
- update to new version 2.1

* Tue Sep 15 2009 Götz Waschk <waschk@mandriva.org> 2.0-1mdv2010.0
+ Revision: 443160
- new version
- drop patch

* Tue Jul 28 2009 Götz Waschk <waschk@mandriva.org> 0.17.0-2mdv2010.0
+ Revision: 402858
- fix encoding of German translation

* Mon Jul 27 2009 Götz Waschk <waschk@mandriva.org> 0.17.0-1mdv2010.0
+ Revision: 400548
- update to new version 0.17.0

* Fri Jun 05 2009 Götz Waschk <waschk@mandriva.org> 0.16.1-1mdv2010.0
+ Revision: 383028
- update to new version 0.16.1

* Mon Jun 01 2009 Götz Waschk <waschk@mandriva.org> 0.16.0-1mdv2010.0
+ Revision: 381972
- fix build deps
- new version
- update file list

* Mon May 04 2009 Götz Waschk <waschk@mandriva.org> 0.15.2-1mdv2010.0
+ Revision: 371604
- new version

* Fri Mar 13 2009 Götz Waschk <waschk@mandriva.org> 0.15.1-1mdv2009.1
+ Revision: 354476
- new version
- drop patch

* Wed Mar 11 2009 Götz Waschk <waschk@mandriva.org> 0.15.0-2mdv2009.1
+ Revision: 353917
- fix it for python 2.6

* Mon Mar 09 2009 Götz Waschk <waschk@mandriva.org> 0.15.0-1mdv2009.1
+ Revision: 353182
- new version
- update file list

* Sun Feb 01 2009 Götz Waschk <waschk@mandriva.org> 0.14.1-1mdv2009.1
+ Revision: 336289
- new version

* Sun Dec 28 2008 Götz Waschk <waschk@mandriva.org> 0.14.0-2mdv2009.1
+ Revision: 320582
- rebuild for new python

* Thu Dec 18 2008 Götz Waschk <waschk@mandriva.org> 0.14.0-1mdv2009.1
+ Revision: 315727
- new version
- update deps

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Oct 30 2008 Götz Waschk <waschk@mandriva.org> 0.13.1-1mdv2009.1
+ Revision: 298743
- new version
- fix source URL

* Sat Oct 11 2008 Götz Waschk <waschk@mandriva.org> 0.13.0-1mdv2009.1
+ Revision: 291904
- new version
- update deps

* Tue Sep 09 2008 Götz Waschk <waschk@mandriva.org> 0.12.3-1mdv2009.0
+ Revision: 283094
- new version

* Fri Aug 08 2008 Götz Waschk <waschk@mandriva.org> 0.12.2-1mdv2009.0
+ Revision: 268064
- new version
- update file list
- update license
- update postinstall scripts

* Thu Jul 24 2008 Götz Waschk <waschk@mandriva.org> 0.12.1-1mdv2009.0
+ Revision: 245148
- new version
- drop patch

* Fri Jul 18 2008 Götz Waschk <waschk@mandriva.org> 0.12.0-2mdv2009.0
+ Revision: 238166
- fix syncing to ipod

* Tue Jul 15 2008 Götz Waschk <waschk@mandriva.org> 0.12.0-1mdv2009.0
+ Revision: 235814
- new version
- update deps

* Mon Jun 02 2008 Götz Waschk <waschk@mandriva.org> 0.11.3-1mdv2009.0
+ Revision: 214178
- new version
- new version
- update file list

* Wed Apr 09 2008 Götz Waschk <waschk@mandriva.org> 0.11.1-1mdv2009.0
+ Revision: 192434
- new version
- drop patch

* Tue Feb 26 2008 Götz Waschk <waschk@mandriva.org> 0.11.0-2mdv2008.1
+ Revision: 175397
- use bluez-gnome instead of gnome-bluetooth

* Mon Feb 25 2008 Götz Waschk <waschk@mandriva.org> 0.11.0-1mdv2008.1
+ Revision: 174794
- new version
- update deps

* Tue Jan 22 2008 Götz Waschk <waschk@mandriva.org> 0.10.4-1mdv2008.1
+ Revision: 156229
- new version
- fix desktop entry

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Dec 13 2007 Götz Waschk <waschk@mandriva.org> 0.10.3-1mdv2008.1
+ Revision: 119224
- new version
- update file list

* Mon Nov 26 2007 Götz Waschk <waschk@mandriva.org> 0.10.2-1mdv2008.1
+ Revision: 112151
- new version
- remove dep on python-id3

* Sat Nov 17 2007 Funda Wang <fwang@mandriva.org> 0.10.1-2mdv2008.1
+ Revision: 109227
- rebuild fore new lzma

* Sun Oct 28 2007 Götz Waschk <waschk@mandriva.org> 0.10.1-1mdv2008.1
+ Revision: 102832
- new version

* Tue Oct 09 2007 Götz Waschk <waschk@mandriva.org> 0.10.0-1mdv2008.1
+ Revision: 95941
- new version
- update deps

* Sun Aug 26 2007 Götz Waschk <waschk@mandriva.org> 0.9.5-1mdv2008.0
+ Revision: 71586
- new version
- drop patches

* Thu Aug 09 2007 Götz Waschk <waschk@mandriva.org> 0.9.4-4mdv2008.0
+ Revision: 60785
- fix sync with more than one new episode in a feed
- drop patch 1 again

* Tue Aug 07 2007 Götz Waschk <waschk@mandriva.org> 0.9.4-3mdv2008.0
+ Revision: 59708
- patch to improve mp3 length detection

* Mon Jul 23 2007 Götz Waschk <waschk@mandriva.org> 0.9.4-2mdv2008.0
+ Revision: 54541
- patch to use the right python-id3
- fix deps

* Sat Jul 21 2007 Götz Waschk <waschk@mandriva.org> 0.9.4-1mdv2008.0
+ Revision: 54284
- new version
- drop patch

* Sun Jul 08 2007 Götz Waschk <waschk@mandriva.org> 0.9.4-0.345.1mdv2008.0
+ Revision: 49931
- fix buildrequires
- svn snapshot with support for libgpod 0.5.x

* Tue Jun 26 2007 Götz Waschk <waschk@mandriva.org> 0.9.3-1mdv2008.0
+ Revision: 44214
- new version
- drop patch

* Fri May 25 2007 Götz Waschk <waschk@mandriva.org> 0.9.2-2mdv2008.0
+ Revision: 31071
- fix download on startup

* Wed May 23 2007 Götz Waschk <waschk@mandriva.org> 0.9.2-1mdv2008.0
+ Revision: 30123
- new version


* Sat Apr 07 2007 Götz Waschk <waschk@mandriva.org> 0.9.1-1mdv2007.1
+ Revision: 150957
- oops, fix buildrequires
- new version
- update deps
- drop patch
- fix installation
- add new icons

* Fri Mar 09 2007 Götz Waschk <waschk@mandriva.org> 0.9.0-2mdv2007.1
+ Revision: 138576
- fix desktop entry

* Wed Mar 07 2007 Jérôme Soyer <saispo@mandriva.org> 0.9.0-1mdv2007.1
+ Revision: 134489
- New release 0.9.0

* Mon Feb 05 2007 Jérôme Soyer <saispo@mandriva.org> 0.8.9-1mdv2007.1
+ Revision: 116233
- New release 0.8.9

* Tue Dec 19 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.8.0-3mdv2007.1
+ Revision: 99234
- Fix file list
- Rebuild against new python
- Swtich to new xdg menu
- Remove old menu style
- Import gpodder

* Tue Aug 01 2006 Jerome Soyer <saispo@mandriva.org> 0.8.0-1mdv2007.0
- New release 0.8.0

* Tue Apr 11 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.7-2mdk
- Add BuildRequires
- use mkrel

* Mon Apr 10 2006 Austin Acton <austin@mandriva.org> 0.7-1mdk
- New release 0.7

* Fri Mar 31 2006 Austin Acton <austin@mandriva.org> 0.6-1mdk
- New release 0.6

* Sat Feb 11 2006 Austin Acton <austin@mandriva.org> 0.5-1mdk
- New release 0.5

* Fri Sep 09 2005 Austin Acton <austin@mandriva.org> 0.4-1mdk
- New release 0.4

* Sun Sep 04 2005 Austin Acton <austin@mandriva.org> 0.3-1mdk
- initial package

