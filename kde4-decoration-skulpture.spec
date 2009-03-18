Summary:	KDE4 minimalistic window decoration
Summary(pl.UTF-8):	Minimalistyczna dekoracja okien dla KDE4
Name:		kde4-decoration-skulpture
Version:	0.2.2.4
Release:	0.1
License:	GPL
Group:		X11/Amusements
Source0:	http://skulpture.maxiom.de/releases/skulpture-%{version}.tar.bz2
# Source0-md5:	78b1a4796cb3945d86fccc770c034d49
URL:		http://skulpture.maxiom.de/
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	gettext-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

%prep
%setup -q -n skulpture-%{version}

%build
%cmake \
		-DCMAKE_INSTALL_PREFIX=%{_prefix} \
		-DLIB_INSTALL_DIR=%{_libdir} \
		-DCMAKE_BUILD_TYPE=%{!?debug:release}%{?debug:debug} \
%if "%{_lib}" == "lib64"
		-DLIB_SUFFIX=64 \
%endif
		.

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
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
