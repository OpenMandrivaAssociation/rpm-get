%define	name	rpm-get 
%define	version	1.5
%define release	7

Summary:	Simple clone of apt-get for rpm
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Configuration/Packaging
URL:		https://zoy.org/~alien/rpm-get
Source0:	http://zoy.org/~alien/rpm-get/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch

%description
rpm-get is a simple clone of Debian's apt-get utility for 
automatically download and install files.
Use the /etc/rpm-get.conf file to set up your favorites ftp mirrors.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/var/rpm-get

install -D -m755 %_builddir/%{name}/rpm-get-configure $RPM_BUILD_ROOT/sbin/rpm-get-configure
install -D -m755 $RPM_BUILD_DIR/rpm-get/rpm-get $RPM_BUILD_ROOT/sbin/rpm-get
install -D -m755 $RPM_BUILD_DIR/rpm-get/dep-check.sh $RPM_BUILD_ROOT/sbin/dep-check.sh
install -D -m755 $RPM_BUILD_DIR/rpm-get/rpm-dep.sh $RPM_BUILD_ROOT/sbin/rpm-dep.sh
install -D -m755 $RPM_BUILD_DIR/rpm-get/rpm-fle2pkg.sh $RPM_BUILD_ROOT/sbin/rpm-fle2pkg.sh
install -D -m644 $RPM_BUILD_DIR/rpm-get/rpm-get.conf $RPM_BUILD_ROOT%{_sysconfdir}/rpm-get.conf
install -D -m644 $RPM_BUILD_DIR/rpm-get/rpm-get.1 $RPM_BUILD_ROOT%{_mandir}/man1/rpm-get.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes BUGS AUTHORS TODO
%config(noreplace) %{_sysconfdir}/*
/sbin/*
%{_mandir}/man1/*
/var/rpm-get/



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.5-6mdv2010.0
+ Revision: 433453
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.5-5mdv2009.0
+ Revision: 260321
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.5-4mdv2009.0
+ Revision: 251493
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.5-2mdv2008.1
+ Revision: 140747
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 23 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.5-2mdv2008.0
+ Revision: 69926
- use %%mkrel


* Thu Jun 12 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.5-1mdk
- 1.5
- BuildArch: noarch
- nicer formatting
- updated url to source
- drop LICENSE file from %%docs, it's GPL...
- added TODO to %%docs
- added URL tag

* Sun Jan 20 2002 Daouda LO <daouda@mandrakesoft.com> 1.4-2mdk 
- fix group (Credits to Alexander)

* Sun Sep 02 2001 Daouda LO <daouda@mandrakesoft.com> 1.4-1mdk 
- release 1.4.

* Sat Jul 21 2001 Daouda Lo <daouda@mandrakesoft.com> 1.0-1mdk 
- release 1.0.

* Sun Jul 01 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.7-2mdk
- Fix some Daouda suck: ;)
  - s/^apt-get/rpm-get/ in %%description.
  - s/Copyright/License/;

* Sun Jul 01 2001 Daouda Lo <daouda@mandrakesoft.com> 0.7-1mdk 
- first release for mdk 
- request for stress testing ;)

