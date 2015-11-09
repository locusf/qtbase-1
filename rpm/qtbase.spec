%define _qtmodule_snapshot_version 5.2.0
Name:       qt5-qtplatformplugin-rpi
Summary:    Qt Plaform Plugin for Raspberry Pi
Version:    5.2.0
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
#Source0:    %{name}-%{version}.tar.xz
Patch1:     add-rpi-platform-plugin.patch
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtopengl-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtdbus-devel
BuildRequires:  qt5-qtplatformsupport-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  libffi-devel
BuildRequires:  fdupes
BuildRequires:  pkgconfig(udev)
BuildRequires:  gfx-rpi-devel
BuildRequires:  gfx-rpi-libEGL-devel
BuildRequires:  gfx-rpi-libGLESv2-devel
BuildRequires:  pkgconfig(mtdev)

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains a Qt platform plugin for Raspberry Pi 


#### Build section

%prep

%build
export QTDIR=/usr/share/qt5
export INSTALLBASE=/usr

cd src/plugins/platforms/qtplatformplugin-rpi
cp ../eglfs/cursor-atlas.png .

qmake -qt=5

make %{?_smp_flags} 

%install
rm -rf %{buildroot}

cd src/plugins/platforms/qtplatformplugin-rpi
%make_install

# We don't need qt5/Qt/
rm -rf %{buildroot}/%{_includedir}/qt5/Qt
rm -rf %{buildroot}/%{_libdir}/cmake
#### Pre/Post section

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


#### File section

%files
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/platforms/libqtplatformplugin-rpi.so

