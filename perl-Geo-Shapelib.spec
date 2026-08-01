%define upstream_name Geo-Shapelib
%define upstream_version 0.22
Summary:	Perl extension for reading and writing shapefiles as defined by ESRI(r)
Name:		perl-%{upstream_name}
Version:	0.22
Release:	51
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/ajolma/Geo-Shapelib
Source0:	https://cpan.metacpan.org/authors/id/A/AJ/AJOLMA/Geo-Shapelib-0.22.tar.gz
BuildRequires:	make
BuildRequires:	pkgconfig(shapelib)
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
# Makefile.PL needs a real libshp.so path (not only -lshp); headers live under include/libshp
libdir=$(pkg-config --variable=libdir shapelib 2>/dev/null || echo %{_libdir})
libshp=
for c in "$libdir/libshp.so" "%{_libdir}/libshp.so" "$libdir/libshp.so.1" "$libdir/libshp.so.4"; do
	if [ -e "$c" ]; then libshp=$c; break; fi
done
if [ -z "$libshp" ]; then
	libshp=$(ls "$libdir"/libshp.so* "%{_libdir}"/libshp.so* 2>/dev/null | head -1 || true)
fi
if [ -z "$libshp" ] || [ ! -e "$libshp" ]; then
	echo "ERROR: libshp.so not found (pkgconfig shapelib libdir=$libdir)" >&2
	pkg-config --libs --cflags shapelib || true
	ls -la "$libdir"/libshp* "%{_libdir}"/libshp* 2>/dev/null || true
	exit 1
fi
export PERL_SHAPELIB="$libshp"
echo "Using PERL_SHAPELIB=$PERL_SHAPELIB"
perl Makefile.PL INSTALLDIRS=vendor
# headers are under %{_includedir}/libshp (Makefile.PL used libdir as -I)
sed -i "s|-I${libdir}|-I%{_includedir}/libshp|g; s|-I%{_libdir}|-I%{_includedir}/libshp|g" Makefile || :
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


