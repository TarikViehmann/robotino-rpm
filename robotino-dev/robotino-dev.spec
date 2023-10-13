Name: robotino-dev
Version: 1.0.2
Release: 1%{?dist}
Summary: Robotino Development Files

License: Unknown
URL: http://openrobotino.org/
Source0: https://packages2.openrobotino.org/pool/xenial/main/r/robotino-dev/robotino-dev_1.0.2_amd64.deb

# Define the architecture
BuildArch: x86_64
BuildRequires: dpkg
Requires: rec-rpc
%description
Development libraries for Robotino

# Install section
%install
# Extract files from the deb package
dpkg-deb -x %{SOURCE0} %{buildroot}
# Create necessary directories
mkdir -p %{buildroot}/usr/lib64/cmake/robotino
mkdir -p %{buildroot}/usr/share/robotino

find %{buildroot} -type f \( -name '*.so' -o -name '*.so.*' \) -exec chmod 755 {} +

mv %{buildroot}/opt/robotino/cmake/* %{buildroot}/usr/lib64/cmake/robotino/
cp -r %{buildroot}/opt/robotino/lib/* %{buildroot}/usr/lib64
cp -r %{buildroot}/opt/robotino/include %{buildroot}/usr/
# Remove empty directories
rm -r %{buildroot}/opt
rm -r %{buildroot}/etc

# Package section
%files
%{_libdir}/cmake/robotino/
%{_includedir}/rec/robotino/
%{_libdir}/librec_robotino_rpc.so

# Changelog
%changelog
* Fri Oct 13 2023 Your Name <your.email@example.com> - 1.0.2-1
- Initial repackage

