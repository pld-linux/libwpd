Summary:	Library for reading and converting WordPerfect(TM) documents
Summary(pl):	Biblioteka do odczytu i konwersji dokumentów WordPerfecta(TM)
Name:		libwpd
Version:	0.8.5
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libwpd/%{name}-%{version}.tar.gz
# Source0-md5:	6b679e205a2805c3d23f41c65b35e266
URL:		http://libwpd.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	libgsf-devel >= 1.14.1
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.12.0
Requires:	libgsf >= 1.14.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library that handles WordPerfect documents.

%description -l pl
Biblioteka obs³uguj±ca dokumenty WordPerfecta.

%package devel
Summary:	Header files for libwpd library
Summary(pl):	Pliki nag³ówkowe biblioteki libwpd
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.12.0
Requires:	libgsf-devel >= 1.14.1
Requires:	libstdc++-devel

%description devel
Header files for libwpd library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libwpd.

%package static
Summary:	Static libwpd library
Summary(pl):	Statyczna biblioteka libwpd
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libwpd library.

%description static -l pl
Statyczna biblioteka libwpd.

%package tools
Summary:	Tools to transform WordPerfect Documents into other formats
Summary(pl):	Narzêdzia do przekszta³cania dokumentów WordPerfecta na inne formaty
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description tools
Tools to transform WordPerfect Documents (WPD) into other formats.
Currently supported: html, raw, text.

%description tools -l pl
Narzêdzia do przekszta³cania dokumentów WordPerfecta (WPD) na inne
formaty. Aktualnie obs³ugiwane s±: html, raw, text.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
LDFLAGS="%{rpmldflags} -Wl,--as-needed"
%configure \
	--enable-static
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
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libwpd*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
