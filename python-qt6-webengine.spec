%define _disable_lto 1
%define _disable_ld_no_undefined 1
%define major %(echo %{version} |cut -d. -f1-2)
%define _debugsource_packages 0
%global _debugsource_template %{nil}

Summary:	Set of Python bindings for Qt WebEngine
Name:		python-qt6-webengine
Version:	6.9.0
Release:	2
License:	GPLv2+
Group:		Development/KDE and Qt
Url:		https://www.riverbankcomputing.co.uk/software/pyqt/intro
Source0:	https://files.pythonhosted.org/packages/source/P/PyQt6-WebEngine/PyQt6_WebEngine-%{version}.tar.gz

BuildRequires:	python-sip >= 5.1.0
BuildRequires:	python-sip-qt6
BuildRequires:	python-qt-builder
BuildRequires:	qmake-qt6
BuildRequires:	qt6-cmake
BuildRequires:	glibc-devel
BuildRequires:	sed
BuildRequires:	pkgconfig(dbus-python)
BuildRequires:	pkgconfig(python3)
BuildRequires:	cmake(Qt6Bluetooth)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Nfc)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Designer)
BuildRequires:	cmake(Qt6UiPlugin)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6MultimediaWidgets)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6OpenGL)
BuildRequires:	cmake(Qt6OpenGLWidgets)
BuildRequires:	cmake(Qt6Positioning)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6RemoteObjects)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6QmlModels)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Quick3D)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6Help)
BuildRequires:	cmake(Qt6SerialPort)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6SvgWidgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6WebChannel)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:	cmake(Qt6WebSockets)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Sensors)
BuildRequires:	cmake(Qt6ShaderTools)
BuildRequires:	cmake(Qt6WebEngineCore)
BuildRequires:	cmake(Qt6WebEngineQuick)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(dri)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(icu-uc)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	pkgconfig(libpcre2-16)
BuildRequires:	pkgconfig(libzstd)
BuildRequires:	cmake(double-conversion)
BuildRequires:	python-qt6
BuildRequires:	python-qt6-core
BuildRequires:	python-qt6-gui
BuildRequires:	python-qt6-network
BuildRequires:	python-qt6-webchannel
BuildRequires:	python-qt6-devel

%description
PyQt is a set of Python bindings for Trolltech's Qt application framework.

%files
%{python_sitearch}/PyQt6/QtWebEngineCore.abi3.so
%{python_sitearch}/PyQt6/QtWebEngineQuick.abi3.so
%{python_sitearch}/PyQt6/QtWebEngineWidgets.abi3.so
%{python_sitearch}/PyQt6/bindings/QtWebEngineCore
%{python_sitearch}/PyQt6/bindings/QtWebEngineQuick
%{python_sitearch}/PyQt6/bindings/QtWebEngineWidgets
%{python_sitearch}/pyqt6_webengine-%{version}.dist-info/

%prep
%autosetup -n pyqt6_webengine-%{version} -p1
export QTDIR=%{_qtdir}
export PATH=%{_qtdir}/bin:$PATH
sip-build \
	--no-make
find . -name Makefile |xargs sed -i -e 's,-L/usr/lib64,,g;s,-L/usr/lib,,g;s,-flto,-fno-lto,g'

%build
%make_build -C build


%install
%make_install -C build INSTALL_ROOT=%{buildroot}

# ensure .so modules are executable for proper -debuginfo extraction
find %{buildroot}%{python_sitearch} -name "*.so" |xargs chmod a+rx
