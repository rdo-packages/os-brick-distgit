# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %{expand:%{python%{pyver}_sitelib}}
%global pyver_install %{expand:%{py%{pyver}_install}}
%global pyver_build %{expand:%{py%{pyver}_build}}
# End of macros for py2/py3 compatibility
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global pypi_name os-brick

%global with_doc 1

%global common_desc \
OpenStack Cinder brick library for managing local volume attaches

Name:           python-%{pypi_name}
Version:        2.10.4
Release:        3%{?dist}
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
Requires:       python%{pyver}-oslo-privsep >= 1.32.0
Requires:       python%{pyver}-os-win >= 3.0.0
Requires:       cryptsetup
Requires:       device-mapper-multipath
Requires:       iscsi-initiator-utils
Requires:       lsscsi >= 0.29
Requires:       lvm2
Requires:       nfs-utils
Requires:       sg3_utils
Requires:       sysfsutils

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
BuildRequires:  python%{pyver}-oslo-concurrency  >= 3.8.0
BuildRequires:  python%{pyver}-oslo-i18n >= 3.15.3
BuildRequires:  python%{pyver}-oslo-log >= 3.36.0
BuildRequires:  python%{pyver}-oslo-service >= 1.24.0
BuildRequires:  python%{pyver}-os-win
BuildRequires:  python%{pyver}-requests >= 2.14.2
BuildRequires:  python%{pyver}-six >= 1.10.0
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  python%{pyver}-oslo-privsep >= 1.32.0

%if 0%{?with_doc}
BuildRequires:  python%{pyver}-openstackdocstheme
BuildRequires:  python%{pyver}-sphinx
%endif

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

%if 0%{?with_doc}
# generate html docs
%{pyver_bin} setup.py build_sphinx -b html
# remove the sphinx-build-%{pyver} leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

# Move config files to proper location
install -d -m 755 %{buildroot}%{_datarootdir}/%{pypi_name}/rootwrap
mv %{buildroot}/usr/etc/os-brick/rootwrap.d/*.filters %{buildroot}%{_datarootdir}/%{pypi_name}/rootwrap

%files -n python%{pyver}-%{pypi_name}
%license LICENSE
%if 0%{?with_doc}
%doc doc/build/html
%endif
%doc README.rst
%{pyver_sitelib}/os_brick*
%{_datarootdir}/%{pypi_name}
%exclude %{pyver_sitelib}/os_brick/tests

%changelog
* Mon Sep 14 2020 Eric Harney <eharney@redhat.com> 2.10.4-3
- Add lsscsi requirement

* Mon Sep 14 2020 Eric Harney <eharney@redhat.com> 2.10.4-2
- Add iscsi-initiator-utils requirement

* Wed Jun 24 2020 RDO <dev@lists.rdoproject.org> 2.10.4-1
- Update to 2.10.4

* Fri Jun 05 2020 RDO <dev@lists.rdoproject.org> 2.10.3-1
- Update to 2.10.3

* Fri Mar 27 2020 RDO <dev@lists.rdoproject.org> 2.10.2-1
- Update to 2.10.2

* Wed Jan 08 2020 RDO <dev@lists.rdoproject.org> 2.10.1-1
- Update to 2.10.1

* Fri Sep 20 2019 RDO <dev@lists.rdoproject.org> 2.10.0-1
- Update to 2.10.0

