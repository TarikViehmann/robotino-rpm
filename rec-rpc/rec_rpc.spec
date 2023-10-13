Name: rec-rpc
Version: 1.6.1
Release: 1%{?dist}
Summary: REC's Qt based RPC library

License: Unknown
URL: http://openrobotino.org/
Source0: https://packages2.openrobotino.org/pool/xenial/main/r/rec-rpc/rec-rpc_1.6.1_amd64.deb
Source1: RecRpcConfig.cmake

# Define the architecture
BuildArch: x86_64
BuildRequires: dpkg
%description
Binary distribution of REC's Qt based RPC library
# Install section
%install
# Extract files from the deb package
dpkg-deb -x %{SOURCE0} %{buildroot}

# Create necessary directories
mkdir -p %{buildroot}/usr/lib64/cmake/RecRpc
mkdir -p %{buildroot}/usr/include/rec/rpc/serialization
mkdir -p %{buildroot}/usr/include/rec/rpc

cp %{SOURCE1} %{buildroot}/usr/lib64/cmake/RecRpc/

find %{buildroot} -type f \( -name '*.so' -o -name '*.so.*' \) -exec chmod 755 {} +

mv %{buildroot}/opt/rec_rpc/include/rec/rpc/serialization/* %{buildroot}/usr/include/rec/rpc/serialization/
cp -r %{buildroot}/opt/rec_rpc/lib/* %{buildroot}/usr/lib64
cp -r %{buildroot}/opt/rec_rpc/include/rec/rpc/* %{buildroot}/usr/include/rec/rpc/
# Remove empty directories
rm -r %{buildroot}/opt
rm -r %{buildroot}/etc

# Package section
%files
%{_libdir}/cmake/RecRpc/
%{_includedir}/rec/rpc/
%{_libdir}/librec_rpc.so

# Clean section (optional)
%clean
rm -rf %{buildroot}

%changelog
* Fri Oct 13 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de>
- Initial repackage
# End of the spec file

