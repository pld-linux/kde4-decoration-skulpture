
%define		qtver	4.6.2
%define		kdever	4.4.2
%define		orgname	skulpture

Summary:	KDE4 minimalistic window decoration
Summary(pl.UTF-8):	Minimalistyczna dekoracja okien dla KDE4
Name:		kde4-decoration-%{orgname}
Version:	0.2.3
Release:	1
License:	GPL
Group:		X11/Amusements
Source0:	http://skulpture.maxiom.de/releases/%{orgname}-%{version}.tar.bz2
# Source0-md5:	f810e03967e60d398849386418de1e91
URL:		http://skulpture.maxiom.de/
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdebase-workspace-devel >= %{kdever}
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	libstdc++-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Skulpture, high configurable GUI style addon for KDE4, features
classical, three-dimensional artwork, along with other features not
found in other styles.

%description -l pl.UTF-8
Skulpture (ang. scultpure, rzeźba), dodatkowy styl dla KDE4, cechuje
się zarówno wyglądem klasycznym jak i trójwymiarowym. Ponadto zawiera
inne właściwości niespotykane w innych dekoracjach, jak na przykład
wysoka konfigurowalność.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIB_INSTALL_DIR=%{_libdir} \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir} \
        kde_libs_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kstyle_skulpture_config.so
%attr(755,root,root) %{_libdir}/kde4/kwin3_skulpture.so
%attr(755,root,root) %{_libdir}/kde4/kwin_skulpture_config.so
%attr(755,root,root) %{_libdir}/qt4/plugins/styles/libskulpture.so
%{_datadir}/apps/color-schemes/SkulptureChocolate.colors
%{_datadir}/apps/color-schemes/SkulptureIce.colors
%{_datadir}/apps/color-schemes/SkulptureMint.colors
%{_datadir}/apps/color-schemes/SkulptureStone.colors
%{_datadir}/apps/color-schemes/SkulptureStrawberry.colors
%{_datadir}/apps/color-schemes/SkulptureVanilla.colors
%{_datadir}/apps/kstyle/themes/skulpture.themerc
%{_datadir}/apps/kwin/skulpture.desktop
%{_datadir}/apps/skulpture/pics/skulpture.png
%{_datadir}/apps/skulpture/skulptureui.rc
