Name: robotino-api2
Version: 1.1.14
Release: 1%{?dist}
Summary: Robotino API 2

License: Unknown
URL: openrobotino.org
Source0: https://packages2.openrobotino.org/pool/xenial/main/r/robotino-api2/robotino-api2_1.1.14_amd64.deb
Source1: RobotinoAPI2Config.cmake
# Define the architecture
BuildArch: x86_64
BuildRequires: dpkg
Requires: rec-rpc
Requires: robotino-dev
%description
Robotion API version 2
%prep
rm -dr %{_builddir}/robotino_api2
mkdir %{_builddir}/robotino_api2
dpkg-deb -x %{SOURCE0} %{_builddir}/robotino_api2
cd %{_builddir}/robotino_api2/
# Install section
%install
cp -r  %{_builddir}/robotino_api2/* %{buildroot}
cp %{SOURCE1} %{buildroot}/
# Extract files from the deb package
# Create necessary directories
mkdir -p %{buildroot}/usr/lib64/cmake/RobotinoAPI2
mkdir -p %{buildroot}/usr/share/robotino

find %{buildroot} -type f \( -name '*.so' -o -name '*.so.*' \) -exec chmod 755 {} +
# mv %{buildroot}/opt/robotino/cmake/FindRobotinoAPI2.cmake %{buildroot}/usr/lib64/cmake/robotino/FindRobotinoAPI2.cmake
mv %{buildroot}/opt/robotino/doc %{buildroot}/usr/share/robotino/
mv %{buildroot}/opt/robotino/bin %{buildroot}/usr/
mv %{buildroot}/RobotinoAPI2Config.cmake %{buildroot}/usr/lib64/cmake/RobotinoAPI2/
cp -r %{buildroot}/opt/robotino/lib/* %{buildroot}/usr/lib64
cp -r %{buildroot}/opt/robotino/include %{buildroot}/usr/
# Remove empty directories
rm -r %{buildroot}/opt
rm -r %{buildroot}/etc
# Package section
%files
%{_libdir}/cmake/RobotinoAPI2/
%{_includedir}/rec/robotino/
%{_libdir}/librec_robotino_api2.so
%{_datadir}/robotino
%{_bindir}/{example_camera,example_c_camera,example_c_circle,example_circle,example_laserrangefinder,example_wallfollow}


# Changelog
%changelog
* Fri Oct 13 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de>
- Initial repackage

