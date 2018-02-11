#
# Conditional build:
%bcond_without	static_libs	# don't build static library

Summary:	Library for reading and converting WordPerfect(TM) documents
Summary(pl.UTF-8):	Biblioteka do odczytu i konwersji dokumentów WordPerfecta(TM)
Name:		libwpd
Version:	0.10.2
Release:	1
License:	MPL v2.0 or LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libwpd/%{name}-%{version}.tar.xz
# Source0-md5:	50d575509d68c940e566c4a0581cd61a
URL:		http://libwpd.sourceforge.net/
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake >= 1:1.11
BuildRequires:	doxygen
BuildRequires:	librevenge-devel >= 0.0.1
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	librevenge >= 0.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library that handles WordPerfect documents.

%description -l pl.UTF-8
Biblioteka obsługująca dokumenty WordPerfecta.

%package devel
Summary:	Header files for libwpd library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libwpd
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	librevenge-devel >= 0.0.1
Requires:	libstdc++-devel

%description devel
Header files for libwpd library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libwpd.

%package static
Summary:	Static libwpd library
Summary(pl.UTF-8):	Statyczna biblioteka libwpd
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libwpd library.

%description static -l pl.UTF-8
Statyczna biblioteka libwpd.

%package apidocs
Summary:	API documentation for libwpd library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libwpd
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for libwpd library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libwpd.

%package tools
Summary:	Tools to transform WordPerfect Documents into other formats
Summary(pl.UTF-8):	Narzędzia do przekształcania dokumentów WordPerfecta na inne formaty
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description tools
Tools to transform WordPerfect Documents (WPD) into other formats.
Currently supported: html, raw, text.

%description tools -l pl.UTF-8
Narzędzia do przekształcania dokumentów WordPerfecta (WPD) na inne
formaty. Aktualnie obsługiwane są: html, raw, text.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_static_libs:--enable-static} \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libwpd-*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libwpd-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwpd-0.10.so.10

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwpd-0.10.so
%{_includedir}/libwpd-0.10
%{_pkgconfigdir}/libwpd-0.10.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libwpd-0.10.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc docs/doxygen/html/*

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wpd2html
%attr(755,root,root) %{_bindir}/wpd2raw
%attr(755,root,root) %{_bindir}/wpd2text
