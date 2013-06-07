#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Library for reading and converting WordPerfect(TM) documents
Summary(pl.UTF-8):	Biblioteka do odczytu i konwersji dokumentów WordPerfecta(TM)
Name:		libwpd
Version:	0.9.8
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libwpd/%{name}-%{version}.tar.xz
# Source0-md5:	eb5a32136ebcb28d1450dc6c6eed1fe5
URL:		http://libwpd.sourceforge.net/
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake >= 1:1.11
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
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
	%{?with_static_libs:--enable-static} \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/doc
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libwpd-*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog NEWS TODO
%attr(755,root,root) %{_libdir}/libwpd-0.9.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwpd-0.9.so.9
%attr(755,root,root) %{_libdir}/libwpd-stream-0.9.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwpd-stream-0.9.so.9

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwpd-0.9.so
%attr(755,root,root) %{_libdir}/libwpd-stream-0.9.so
%{_includedir}/libwpd-0.9
%{_pkgconfigdir}/libwpd-0.9.pc
%{_pkgconfigdir}/libwpd-stream-0.9.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libwpd-0.9.a
%{_libdir}/libwpd-stream-0.9.a
%endif

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wpd2*
