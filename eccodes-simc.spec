%global releaseno 1

Name:           eccodes-simc
Version:        0.5
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
Source5:        https://raw.githubusercontent.com/ARPA-SIMC/%{name}/v%{version}-%{releaseno}/eccodes-simc_el7.patch

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

%if 0%{?rhel} == 7
./make-defs --prefix=%{buildroot} --sysconfdir=%{_sysconfdir} --datadir=%{_datadir} --patch=eccodes-simc_el7.patch
%else
./make-defs --prefix=%{buildroot} --sysconfdir=%{_sysconfdir} --datadir=%{_datadir} --patch=eccodes-simc.patch
%endif

%files
%{_sysconfdir}/profile.d/%{name}.sh
%{_datadir}/%{name}/*

%changelog
* Tue Aug 2 2022 Davide Cesari <dcesari@arpae.it> - 0.5-1%{?dist}
- Move UTM template in local sections if required

* Wed Jun 29 2022 Daniele Branchini <dbranchini@arpae.it> - 0.4-3%{?dist}
- Fixed patch

* Fri Jun 3 2022 Daniele Branchini <dbranchini@arpae.it> - 0.4-2%{dist}
- Added fuzz option to patch

* Tue Oct 1 2019 Daniele Branchini <dbranchini@arpae.it> - 0.4-1%{dist}
- updated patch offset

* Thu Jun 7 2018 Daniele Branchini <dbranchini@arpae.it> - 0.3-1%{dist}
- fixed COSMO analysis files stepfile (#5)

* Tue May 8 2018 Daniele Branchini <dbranchini@arpae.it> - 0.2-1%{dist}
- added missing definition

* Fri May 4 2018 Daniele Branchini <dbranchini@arpae.it> - 0.1-1%{dist}
- first build

