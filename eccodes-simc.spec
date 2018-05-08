%global releaseno 1

Name:           eccodes-simc
Version:        0.2
Release:        %{releaseno}%{?dist}
Summary:        Custom grib definitions and samples used at ARPAE-SIMC
License:        Apache License, Version 2.0
URL:            https://arpae.it/sim
BuildArch:      noarch
Source0:        https://raw.githubusercontent.com/ARPA-SIMC/%{name}/v%{version}-%{releaseno}/utm_grib2.tmpl
Source1:        https://raw.githubusercontent.com/ARPA-SIMC/%{name}/v%{version}-%{releaseno}/3.datum.table
Source2:        https://raw.githubusercontent.com/ARPA-SIMC/%{name}/v%{version}-%{releaseno}/template.3.32768.def
Source3:        https://raw.githubusercontent.com/ARPA-SIMC/%{name}/v%{version}-%{releaseno}/eccodes-simc.patch
Source4:        https://raw.githubusercontent.com/ARPA-SIMC/%{name}/v%{version}-%{releaseno}/local.200.254.def

BuildRequires:  eccodes, util-linux
Requires:       eccodes

%description
Custom grib definitions and samples used at ARPAE-SIMC:

- definitions for centre 200 (old COSMO implementation)
- timerange 13 (for nudging analysis)
- UTM grib2

%build


%install
[ "%{buildroot}" != / ] && rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sysconfdir}/profile.d/
echo "export ECCODES_DEFINITION_PATH=\"%{_datarootdir}/eccodes-simc/definitions/:%{_datarootdir}/eccodes/definitions/\"" > %{buildroot}/%{_sysconfdir}/profile.d/%{name}.sh
echo "export  ECCODES_SAMPLES_PATH=\"%{_datarootdir}/eccodes-simc/samples/:%{_datarootdir}/eccodes/samples/\"" >> %{buildroot}/%{_sysconfdir}/profile.d/%{name}.sh

mkdir -p %{buildroot}%{_datadir}/%{name}/sample/
%{__install} %{SOURCE0} %{buildroot}%{_datadir}/%{name}/sample

mkdir -p %{buildroot}%{_datadir}/%{name}/definitions/grib2/tables/0/
%{__install} %{SOURCE1} %{buildroot}%{_datadir}/%{name}/definitions/grib2/tables/0/
%{__install} %{SOURCE2} %{buildroot}%{_datadir}/%{name}/definitions/grib2/

mkdir -p %{buildroot}%{_datadir}/%{name}/definitions/grib1/localConcepts/ecmf/
cp -a %{_datadir}/eccodes/definitions/grib1/local.98.* %{buildroot}%{_datadir}/%{name}/definitions/grib1/
rename local.98 local.200 %{buildroot}%{_datadir}/%{name}/definitions/grib1/local.98.*
%{__install} %{SOURCE4} %{buildroot}%{_datadir}/%{name}/definitions/grib1/

cp %{_datadir}/eccodes/definitions/grib1/5.table %{buildroot}%{_datadir}/%{name}/definitions/grib1/
cp %{_datadir}/eccodes/definitions/grib1/grid_definition_90.def %{buildroot}%{_datadir}/%{name}/definitions/grib1/
cp %{_datadir}/eccodes/definitions/grib1/localConcepts/ecmf/stepType.def %{buildroot}%{_datadir}/%{name}/definitions/grib1/localConcepts/ecmf/
cp %{_datadir}/eccodes/definitions/grib2/section.3.def %{buildroot}%{_datadir}/%{name}/definitions/grib2/

pushd %{buildroot}%{_datadir}/%{name}/definitions/
/usr/bin/patch -p1 --suffix --fuzz=0 < %{SOURCE3}
popd

%files
%{_sysconfdir}/profile.d/%{name}.sh
%{_datadir}/%{name}/*

%changelog
* Tue May 8 2018 Daniele Branchini <dbranchini@arpae.it> - 0.2-1%{dist}
- added missing definition

* Fri May 4 2018 Daniele Branchini <dbranchini@arpae.it> - 0.1-1%{dist}
- first build

