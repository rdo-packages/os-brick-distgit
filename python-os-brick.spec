# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global pypi_name os-brick

%global common_desc \
OpenStack Cinder brick library for managing local volume attaches

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
Summary:        OpenStack Cinder brick library for managing local volume attaches

License:        ASL 2.0
URL:            http://www.openstack.org/
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
%{common_desc}

%package -n python%{pyver}-%{pypi_name}
Summary:        OpenStack Cinder brick library for managing local volume attaches
%{?python_provide:%python_provide python%{pyver}-%{pypi_name}}
Provides:       os-brick = %{version}-%{release}

Requires:       python%{pyver}-pbr
Requires:       python%{pyver}-babel >= 2.3.4
Requires:       python%{pyver}-eventlet >= 0.18.2
Requires:       python%{pyver}-oslo-concurrency >= 3.26.0
Requires:       python%{pyver}-oslo-i18n >= 3.15.3
Requires:       python%{pyver}-oslo-log >= 3.36.0
Requires:       python%{pyver}-oslo-service >= 1.24.0
Requires:       python%{pyver}-oslo-utils >= 3.33.0
Requires:       python%{pyver}-requests >= 2.14.2
Requires:       python%{pyver}-six >= 1.10.0
Requires:       python%{pyver}-oslo-privsep >= 1.23.0
Requires:       python%{pyver}-os-win >= 3.0.0
Requires:       device-mapper-multipath
Requires:       sg3_utils

# Handle python2 exception
%if %{pyver} == 2
Requires:       python-retrying
%else
Requires:       python%{pyver}-retrying
%endif

BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-ddt
BuildRequires:  python%{pyver}-pbr >= 2.0.0
BuildRequires:  git
BuildRequires:  python%{pyver}-reno
BuildRequires:  python%{pyver}-sphinx
BuildRequires:  python%{pyver}-oslo-concurrency  >= 3.8.0
BuildRequires:  python%{pyver}-oslo-i18n >= 3.15.3
BuildRequires:  python%{pyver}-oslo-log >= 3.36.0
BuildRequires:  python%{pyver}-oslo-service >= 1.24.0
BuildRequires:  python%{pyver}-openstackdocstheme
BuildRequires:  python%{pyver}-os-win
BuildRequires:  python%{pyver}-requests >= 2.14.2
BuildRequires:  python%{pyver}-six >= 1.10.0
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  python%{pyver}-oslo-privsep >= 1.23.0

# Handle python2 exception
%if %{pyver} == 2
BuildRequires:  python-retrying
%else
BuildRequires:  python%{pyver}-retrying
%endif

%description -n python%{pyver}-%{pypi_name}
%{common_desc}

%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git


%build
%{pyver_build}

%install
%{pyver_install}
# generate html docs
%{pyver_bin} setup.py build_sphinx -b html
# remove the sphinx-build-%{pyver} leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

# Move config files to proper location
install -d -m 755 %{buildroot}%{_datarootdir}/%{pypi_name}/rootwrap
mv %{buildroot}/usr/etc/os-brick/rootwrap.d/*.filters %{buildroot}%{_datarootdir}/%{pypi_name}/rootwrap

%files -n python%{pyver}-%{pypi_name}
%license LICENSE
%doc doc/build/html README.rst
%{pyver_sitelib}/os_brick*
%{_datarootdir}/%{pypi_name}
%exclude %{pyver_sitelib}/os_brick/tests

%changelog
# REMOVEME: error caused by commit http://git.openstack.org/cgit/openstack/os-brick/commit/?id=881c9582723e3fcc22d51f6aa38764716f2517cd
