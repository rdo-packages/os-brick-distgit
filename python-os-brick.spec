%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%if 0%{?fedora}
# There are some missing deps
%global with_python3 1
%endif

%global pypi_name os-brick

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
Summary:        OpenStack Cinder brick library for managing local volume attaches

License:        ASL 2.0
URL:            http://www.openstack.org/
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
OpenStack Cinder brick library for managing local volume attaches

%package -n python2-%{pypi_name}
Summary:        OpenStack Cinder brick library for managing local volume attaches
%{?python_provide:%python_provide python2-%{pypi_name}}
Provides:       os-brick = %{version}-%{release}

Requires:       python-babel >= 2.3.4
Requires:       python-eventlet >= 0.18.2
Requires:       python-oslo-serialization >= 1.10.0
Requires:       python-oslo-concurrency >= 3.8.0
Requires:       python-oslo-i18n >= 2.1.0
Requires:       python-oslo-log >= 3.22.0
Requires:       python-oslo-service >= 1.10.0
Requires:       python-oslo-utils >= 3.20.0
Requires:       python-requests >= 2.10.0
Requires:       python-retrying
Requires:       python-six >= 1.9.0
Requires:       python-oslo-privsep >= 1.9.0
Requires:       python-os-win >= 2.0.0

BuildRequires:  python2-devel
BuildRequires:  python-ddt
BuildRequires:  python-pbr >= 2.0.0
BuildRequires:  python-reno
BuildRequires:  python-sphinx
BuildRequires:  python-oslo-concurrency  >= 3.8.0
BuildRequires:  python-oslo-i18n >= 2.1.0
BuildRequires:  python-oslo-log >= 1.14.0
BuildRequires:  python-oslo-service >= 1.10.0
BuildRequires:  python-oslo-sphinx >= 2.5.0
BuildRequires:  python-requests >= 2.10.0
BuildRequires:  python-six >= 1.9.0
BuildRequires:  python-setuptools
BuildRequires:  python-oslo-privsep >= 1.9.0

%description -n python2-%{pypi_name}
OpenStack Cinder brick library for managing local volume attaches

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        OpenStack Cinder brick library for managing local volume attaches
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-babel >= 2.3.4
Requires:       python3-eventlet >= 0.18.2
Requires:       python3-oslo-serialization >= 1.10.0
Requires:       python3-oslo-concurrency >= 3.8.0
Requires:       python3-oslo-i18n >= 2.1.0
Requires:       python3-oslo-log >= 3.22.0
Requires:       python3-oslo-service >= 1.10.0
Requires:       python3-oslo-utils >= 3.20.0
Requires:       python3-requests >= 2.10.0
Requires:       python3-retrying
Requires:       python3-six >= 1.9.0
Requires:       python3-oslo-privsep >= 1.9.0
Requires:       python3-os-win

BuildRequires:  python3-devel
BuildRequires:  python3-ddt
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-reno
BuildRequires:  python3-sphinx
BuildRequires:  python3-oslo-concurrency  >= 3.8.0
BuildRequires:  python3-oslo-i18n >= 2.1.0
BuildRequires:  python3-oslo-log >= 1.14.0
BuildRequires:  python3-oslo-service >= 1.10.0
BuildRequires:  python3-oslo-sphinx >= 2.5.0
BuildRequires:  python3-requests >= 2.10.0
BuildRequires:  python3-six >= 1.9.0
BuildRequires:  python3-setuptools
BuildRequires:  python3-oslo-privsep >= 1.9.0

%description -n python3-%{pypi_name}
OpenStack Cinder brick library for managing local volume attaches

%endif

%prep
%setup -q -n %{pypi_name}-%{upstream_version}


%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install
# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%if 0%{?with_python3}
%py3_install
%endif

# Move config files to proper location
install -d -m 755 %{buildroot}%{_datarootdir}/%{pypi_name}/rootwrap
mv %{buildroot}/usr/etc/os-brick/rootwrap.d/*.filters %{buildroot}%{_datarootdir}/%{pypi_name}/rootwrap

%files -n python2-%{pypi_name}
%license LICENSE
%doc html README.rst
%{python2_sitelib}/os_brick*
%{_datarootdir}/%{pypi_name}
%exclude %{python2_sitelib}/os_brick/tests

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%license LICENSE
%doc html README.rst
%{python3_sitelib}/os_brick*
%{_datarootdir}/%{pypi_name}
%exclude %{python3_sitelib}/os_brick/tests
%endif

%changelog
