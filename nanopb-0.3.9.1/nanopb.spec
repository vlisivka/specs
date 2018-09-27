Name:           nanopb
Version:        0.3.9.1
Release:        5
License:        Zlib
Summary:        Protocol Buffers with small code size
Url:            https://github.com/nanopb/nanopb
Group:          Development/Languages/Python
Source:         https://github.com/nanopb/nanopb/archive/0.3.9.1.tar.gz
BuildRequires:  python2
BuildRequires:  protobuf-devel
BuildRequires:  cmake
Requires:       python-protobuf
Requires:       protobuf-devel
BuildArch:      noarch

%description
Nanopb is a plain-C implementation of Google's Protocol Buffers data format.
It is targeted at 32 bit microcontrollers, but is also fit for other embedded
systems with tight (2-10 kB ROM, <1 kB RAM) memory constraints. Nanopb supports
static memory allocation, i.e. you don't need a malloc implementation and can
be sure of the memory requirements of your code.

%prep
%setup -q -n %{name}-%{version}

%build
mkdir build
pushd build 
%cmake  -DCMAKE_VERBOSE_MAKEFILE=ON \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DSYSCONFDIR=%{_sysconfdir} \
        -DLIBDIR=%{_libdir} \
        -DLOCALSTATEDIR=%{_localstatedir} \
    ..
make
popd

pushd generator/proto
make
popd

%install
install -D -m 0644 generator/proto/nanopb_pb2.py %{buildroot}%{python_sitelib}/proto/nanopb_pb2.py
install -D -m 0644 generator/proto/plugin_pb2.py %{buildroot}%{python_sitelib}/proto/plugin_pb2.py
install -D -m 0644 generator/proto/__init__.py %{buildroot}%{python_sitelib}/proto/__init__.py
mkdir -p %{buildroot}%{_bindir}
install -D -m 0755 generator/nanopb_generator.py %{buildroot}%{_bindir}/nanopb_generator.py
install -D -m 0755 generator/protoc-gen-nanopb %{buildroot}%{_bindir}/protoc-gen-nanopb

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGELOG.txt LICENSE.txt README.md generator/proto/nanopb.proto
%{_bindir}/nanopb_generator.py
%{_bindir}/protoc-gen-nanopb
%{python_sitelib}/proto/

%changelog
