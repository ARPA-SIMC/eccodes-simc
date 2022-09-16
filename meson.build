project('eccodes-simc', [], version: '0.5', license : 'apache-2')

profile_dir = get_option('sysconfdir') / 'profile.d'

# Generate the profile file
profile_script = configure_file(output: 'eccodes-simc.sh', input: 'eccodes-simc.sh.in', configuration: {
    'datadir': get_option('datadir'),
})

install_data(
    profile_script,
    install_dir: profile_dir
)


# mkdir -p %{buildroot}%{_datadir}/%{name}/samples/
# %{__install} %{SOURCE0} %{buildroot}%{_datadir}/%{name}/samples
# 
# mkdir -p %{buildroot}%{_datadir}/%{name}/definitions/grib2/tables/0/
# %{__install} %{SOURCE1} %{buildroot}%{_datadir}/%{name}/definitions/grib2/tables/0/
# 
# mkdir -p %{buildroot}%{_datadir}/%{name}/definitions/grib1/
# cp -as %{_datadir}/eccodes/definitions/grib1/local.98.* %{buildroot}%{_datadir}/%{name}/definitions/grib1/
# rename local.98 local.200 %{buildroot}%{_datadir}/%{name}/definitions/grib1/local.98.*
# %{__install} %{SOURCE4} %{buildroot}%{_datadir}/%{name}/definitions/grib1/
# 
# cp %{_datadir}/eccodes/definitions/grib1/5.table %{buildroot}%{_datadir}/%{name}/definitions/grib1/
# cp %{_datadir}/eccodes/definitions/grib1/grid_definition_90.def %{buildroot}%{_datadir}/%{name}/definitions/grib1/
# cp %{_datadir}/eccodes/definitions/grib1/stepType.def %{buildroot}%{_datadir}/%{name}/definitions/grib1/
# cp %{_datadir}/eccodes/definitions/grib2/section.3.def %{buildroot}%{_datadir}/%{name}/definitions/grib2/
# 
# # around eccodes v2.23 this line appeared
# if grep -q 'gridDefinitionTemplateNumber *>= *32768' %{_datadir}/eccodes/definitions/grib2/section.3.def; then
#   mkdir -p %{buildroot}%{_datadir}/%{name}/definitions/grib2/local/cnmc \
#    %{buildroot}%{_datadir}/%{name}/definitions/grib2/local/200
#   %{__install} %{SOURCE2} %{buildroot}%{_datadir}/%{name}/definitions/grib2/local/cnmc
#   %{__install} %{SOURCE2} %{buildroot}%{_datadir}/%{name}/definitions/grib2/local/200
# else
#   %{__install} %{SOURCE2} %{buildroot}%{_datadir}/%{name}/definitions/grib2
# fi
# 
# pushd %{buildroot}%{_datadir}/%{name}/definitions/
# %if 0%{?rhel} == 7
# /usr/bin/patch -p1 < %{SOURCE5}
# %else
# /usr/bin/patch -p1 < %{SOURCE3}
# %endif
# popd
# 
# %files
# %{_sysconfdir}/profile.d/%{name}.sh
# %{_datadir}/%{name}/*

# conf_data = configuration_data()
# conf_data.set_quoted('PACKAGE_VERSION', meson.project_version())
# conf_data.set_quoted('TABLE_DIR', get_option('prefix') / table_dir)
# 
# # Dependencies
# foreach name : ['lua', 'lua5.1', 'lua5.2', 'lua5.3']
#     lua_dep = dependency(name, version: '>=5.1.1', required: false)
#     if lua_dep.found()
#         break
#     endif
# endforeach
# if not lua_dep.found()
#     error('Lua could not be found!')
# endif
# conf_data.set('HAVE_LUA', lua_dep.found())
# 
# compiler = meson.get_compiler('cpp')
# if compiler.has_function('getopt_long')
#     conf_data.set('HAS_GETOPT_LONG', true)
# endif
# 
# # Generate config.h
# configure_file(output: 'config.h', configuration: conf_data)
# 
# pymod = import('python')
# python3 = pymod.find_installation('python3', required: false)
# 
# if python3.found()
#     # FIXME: python3.path() is only available from meson 0.50: this is a workaround
#     python3_path = python3.get_variable('BINDIR') / python3.get_variable('PYTHON') + python3.language_version()
# 
#     sphinx = find_program('sphinx-build', 'sphinx-build-3', 'sphinx-build-' + python3.language_version(), required: false)
# 
#     # TODO: check if breathe is installed
#     # TODO AX_PYTHON_MODULE(breathe)
#     # See https://gitlab.freedesktop.org/wayland/weston/-/blob/master/doc/sphinx/meson.build
# 
#     doxygen = find_program('doxygen', required : false)
# 
#     build_docs = sphinx.found() and doxygen.found()
#     docdir = get_option('datadir') / 'doc' / meson.project_name()
# else
#     warning('Documentation disabled, requires doxygen, sphinx, and the breathe python module')
#     build_docs = false
# endif
# 
# subdir('wreport')
# subdir('src')
# 
# if python3.found()
#     subdir('python')
# endif
# 
# if build_docs
#     subdir('doc')
# endif
# 
# subdir('tables')
# 
# # Generate pkg-config metadata
# pkg = import('pkgconfig')
# pkg.generate(libwreport,
#     description: 'Weather report library',
#     filebase: 'libwreport',
#     requires: [lua_dep],
# )
