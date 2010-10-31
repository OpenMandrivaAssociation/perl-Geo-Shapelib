%define		pdir	Geo
%define		pnam	Shapelib
Summary:	Geo::Shapelib - Perl extension for reading and writing shapefiles as defined by ESRI(r)
Summary(pl.UTF-8):	Geo::Shapelib - rozszerzenie Perla o obsługę r/w plików ESRI(r) SHP
Name:		perl-Geo-Shapelib
Version:	0.20
Release:	%mkrel 1
License:	GPL
Group:		Development/Perl
Source0:	http://www.cpan.org/modules/by-module/Geo/%{pdir}-%{pnam}-%{version}.tar.gz
URL:		http://search.cpan.org/dist/Geo-Shapelib/
BuildRequires:	perl-devel >= 1:5.8.0




%description
This is a library for reading, creating, and writing shapefiles as
defined by ESRI(r) using Perl. The Perl code uses Frank Warmerdam's
Shapefile C Library (http://shapelib.maptools.org/). The library is
included in this distribution.


%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# make some directories
install -d %{buildroot}%{perl_vendorarch}/Geo
install -d %{buildroot}%{perl_vendorarch}/auto/Geo/Shapelib
install -d %{buildroot}%{perl_vendorarch}/auto/Geo/Shapelib/shputils



mv %{buildroot}%{perl_sitearch}/Geo/Shapelib.pm %{buildroot}%{perl_vendorarch}/Geo/Shapelib.pm 
mv %{buildroot}%{perl_sitearch}/auto/Geo/Shapelib/Shapelib.so %{buildroot}%{perl_vendorarch}/auto/Geo/Shapelib/Shapelib.so
mv %{buildroot}%{perl_sitearch}/auto/Geo/Shapelib/autosplit.ix %{buildroot}%{perl_vendorarch}/auto/Geo/Shapelib/autosplit.ix
mv %{buildroot}%{perl_sitearch}/auto/Geo/Shapelib/shputils/extralibs.ld %{buildroot}%{perl_vendorarch}/auto/Geo/Shapelib/shputils/extralibs.ld
mv %{buildroot}%{perl_sitearch}/auto/Geo/Shapelib/shputils/shputils.a %{buildroot}%{perl_vendorarch}/auto/Geo/Shapelib/shputils/shputils.a


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc Changes README Copying
%{perl_vendorarch}/Geo/Shapelib.pm
%dir %{perl_vendorarch}/auto/Geo/Shapelib/*
%{perl_vendorarch}/auto/Geo/Shapelib/shputils/*
%{_usr}/local/share/man/man3/Geo::Shapelib.3pm



