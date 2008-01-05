#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Library for reading and converting WordPerfect(TM) documents
Summary(pl.UTF-8):	Biblioteka do odczytu i konwersji dokumentów WordPerfecta(TM)
Name:		libwpd
Version:	0.8.13
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://dl.sourceforge.net/libwpd/%{name}-%{version}.tar.gz
# Source0-md5:	6a4efa95bcb1abcebd22927383983bd3
URL:		http://libwpd.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	libgsf-devel >= 1.14.1
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.12.0
Requires:	libgsf >= 1.14.1
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
Requires:	glib2-devel >= 1:2.12.0
Requires:	libgsf-devel >= 1.14.1
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
	--enable-static \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES TODO
%attr(755,root,root) %{_libdir}/libwpd-0.8.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwpd-0.8.so.8
%attr(755,root,root) %{_libdir}/libwpd-stream-0.8.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwpd-stream-0.8.so.8

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwpd-0.8.so
%attr(755,root,root) %{_libdir}/libwpd-stream-0.8.so
%{_libdir}/libwpd-0.8.la
%{_libdir}/libwpd-stream-0.8.la
%{_includedir}/libwpd-0.8
%{_pkgconfigdir}/libwpd-0.8.pc
%{_pkgconfigdir}/libwpd-stream-0.8.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libwpd-0.8.a
%{_libdir}/libwpd-stream-0.8.a
%endif

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
