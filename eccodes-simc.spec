%global releaseno 1

Name:           eccodes-simc
Version:        0.1
Release:        %{releaseno}%{?dist}
Summary:        Custom grib definitions and samples used at ARPAE-SIMC
License:        Apache License, Version 2.0
URL:            https://arpae.it/sim
BuildArch:      noarch
Source0:        https://raw.githubusercontent.com/ARPA-SIMC/%{name}/v%{version}-%{releaseno}/utm_grib2.tmpl
#ource0:        https://raw.githubusercontent.com/ARPA-SIMC/%{name}/v%{version}-%{releaseno}/eccodes-simc.patch
#ource1:        https://raw.githubusercontent.com/ARPA-SIMC/%{name}/v%{version}-%{releaseno}/eccodes-simc-profile.sh

BuildRequires:  eccodes
Requires:       eccodes

%description
Custom grib definitions and samples used at ARPAE-SIMC:

- definitions for centre 200 (old COSMO implementation)
- timerange 13 (for nudging analysis)
- UTM grib2

%install
[ "%{buildroot}" != / ] && rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sysconfdir}/profile.d/
echo "export ECCODES_DEFINITION_PATH=\"%{_datarootdir}/eccodes-simc/definitions/:%{_datarootdir}/eccodes/definitions/\"" > %{buildroot}/%{_sysconfdir}/profile.d/%{name}.sh
echo "export  ECCODES_SAMPLES_PATH=\"%{_datarootdir}/eccodes-simc/samples/:%{_datarootdir}/eccodes/samples/\"" >> %{buildroot}/%{_sysconfdir}/profile.d/%{name}.sh
mkdir -p %{buildroot}%{_datadir}/%{name}/sample/
%{__install} %{SOURCE0} %{buildroot}%{_datadir}/%{name}/sample

%files
%{_sysconfdir}/profile.d/%{name}.sh
%{_datadir}/%{name}/*

%changelog
* Fri May 4 2018 Daniele Branchini <dbranchini@arpae.it> - 0.1-1%{dist}
- first build
