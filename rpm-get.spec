%define	name	rpm-get 
%define	version	1.5
%define	release	%mkrel 6

Summary:	Simple clone of apt-get for rpm
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Configuration/Packaging
URL:		http://zoy.org/~alien/rpm-get
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
install -D -m755 %{_builddir}/rpm-get/rpm-get $RPM_BUILD_ROOT/sbin/rpm-get
install -D -m755 %{_builddir}/rpm-get/dep-check.sh $RPM_BUILD_ROOT/sbin/dep-check.sh
install -D -m755 %{_builddir}/rpm-get/rpm-dep.sh $RPM_BUILD_ROOT/sbin/rpm-dep.sh
install -D -m755 %{_builddir}/rpm-get/rpm-fle2pkg.sh $RPM_BUILD_ROOT/sbin/rpm-fle2pkg.sh
install -D -m644 %{_builddir}/rpm-get/rpm-get.conf $RPM_BUILD_ROOT%{_sysconfdir}/rpm-get.conf
install -D -m644 %{_builddir}/rpm-get/rpm-get.1 $RPM_BUILD_ROOT%{_mandir}/man1/rpm-get.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes BUGS AUTHORS TODO
%config(noreplace) %{_sysconfdir}/*
/sbin/*
%{_mandir}/man1/*
/var/rpm-get/

