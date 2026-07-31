%define upstream_name		Geo-Shapelib
%define upstream_version 0.22
Summary:	Perl extension for reading and writing shapefiles as defined by ESRI(r)
Name:		perl-%{upstream_name}
Version:	0.22
Release:	45
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/ajolma/Geo-Shapelib
Source0:	https://cpan.metacpan.org/authors/id/A/AJ/AJOLMA/Geo-Shapelib-0.22.tar.gz
BuildRequires:	make
BuildRequires:	perl(Tree::R)
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This is a library for reading, creating, and writing shapefiles as
defined by ESRI(r) using Perl. The Perl code uses Frank Warmerdam's
Shapefile C Library (http://shapelib.maptools.org/). The library is
included in this distribution.

%prep
%setup -q -n Geo-Shapelib-0.22

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build
%check
make test || :

%install
rm -rf %{buildroot}
%makeinstall_std

# we don't want this
find %{buildroot} -name "*.a" -exec rm -rf {} \;


%files
%defattr(-, root, root)
%doc Changes
%{perl_vendorarch}/Geo/Shapelib.pm
%{perl_vendorarch}/auto/Geo/Shapelib
%{_mandir}/man3/Geo::Shapelib.3pm.*


