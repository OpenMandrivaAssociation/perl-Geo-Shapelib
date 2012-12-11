%define upstream_name		Geo-Shapelib
%define upstream_version	0.20

Summary:	Perl extension for reading and writing shapefiles as defined by ESRI(r)
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.200.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Thu Nov 04 2010 Jani Välimaa <wally@mandriva.org> 0.200.0-1mdv2011.0
+ Revision: 593451
- use perl_convert_version macro
- fix summary, license, source and url
- fix BRs
- install file to a correct location
- get rid of .a files
- clean spec

* Sun Oct 31 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.20-1mdv2011.0
+ Revision: 590741
- corrected Group
- import perl-Geo-Shapelib

