%define libname libshivavg
%define devname libshivavg-devel
%define debug_package %nil

Name: shivavg
Version: 0.2.1
Release: 4
Source0: http://garr.dl.sourceforge.net/project/shivavg/ShivaVG/%{version}/ShivaVG-%{version}.zip
Patch0: ShivaVG-0.2.1-compile.patch
Patch1: ShivaVG-0.2.1-GL-linkage.patch
Summary: An implementation of the OpenVG vector graphics API
URL: http://shivavg.sf.net/
License: LGPLv2.1
Group: System/Libraries
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glu)
#BuildRequires: pkgconfig(glut)
BuildRequires: libjpeg-devel

%description
An implementation of the OpenVG vector graphics API on top of OpenGL

%package -n %{libname}
Summary: An implementation of the OpenVG vector graphics API
Group: System/Libraries

%description -n %{libname}
An implementation of the OpenVG vector graphics API on top of OpenGL

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{version}
# ShivaVG 0.2.1 implements the OpenVG standard 1.0, so...
Provides: openvg-devel = 1.0

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -qn ShivaVG-%{version}
%patch0 -p1
%patch1 -p1
chmod +x autogen.sh ; ./autogen.sh

%configure

%build
make

%install
make install DESTDIR="%{buildroot}"

# Since there seems to be some disagreement about
# %{_includedir}/vg vs. %{_includedir}/VG in the standard,
# let's support both...
ln -s vg %{buildroot}%{_includedir}/VG

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{devname}
%{_includedir}/vg
%{_includedir}/VG
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la

%changelog

* Sun Jul 19 2015 Bernhard Rosenkraenzer <bero@bero.eu> 0.2.1-4
- (b02b2ee) MassBuild#774: Increase release tag


