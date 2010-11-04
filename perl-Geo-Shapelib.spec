%define upstream_name		Geo-Shapelib
%define upstream_version	0.20

Summary:	Perl extension for reading and writing shapefiles as defined by ESRI(r)
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Geo/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl(Tree::R)
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This is a library for reading, creating, and writing shapefiles as
defined by ESRI(r) using Perl. The Perl code uses Frank Warmerdam's
Shapefile C Library (http://shapelib.maptools.org/). The library is
included in this distribution.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# we don't want this
find %{buildroot} -name "*.a" -exec rm -rf {} \;

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc Changes README
%{perl_vendorarch}/Geo/Shapelib.pm
%{perl_vendorarch}/auto/Geo/Shapelib
%{_mandir}/man3/Geo::Shapelib.3pm.*
