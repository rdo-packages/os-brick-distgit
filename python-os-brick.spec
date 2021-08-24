%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global pypi_name os-brick

%global with_doc 1

%global common_desc \
OpenStack Cinder brick library for managing local volume attaches

Name:           python-%{pypi_name}
Version:        3.0.6
Release:        2%{?dist}
Summary:        OpenStack Cinder brick library for managing local volume attaches

License:        ASL 2.0
URL:            http://www.openstack.org/
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
%{common_desc}

%package -n python3-%{pypi_name}
Summary:        OpenStack Cinder brick library for managing local volume attaches
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       os-brick = %{version}-%{release}

Requires:       python3-pbr
Requires:       python3-babel >= 2.3.4
Requires:       python3-eventlet >= 0.18.2
Requires:       python3-oslo-concurrency >= 3.26.0
Requires:       python3-oslo-context >= 2.23.0
Requires:       python3-oslo-i18n >= 3.15.3
Requires:       python3-oslo-log >= 3.36.0
Requires:       python3-oslo-serialization >= 2.29.0
Requires:       python3-oslo-service >= 1.24.0
Requires:       python3-oslo-utils >= 3.33.0
Requires:       python3-requests >= 2.14.2
Requires:       python3-six >= 1.10.0
Requires:       python3-oslo-privsep >= 1.32.0
Requires:       python3-os-win >= 3.0.0
Requires:       cryptsetup
Requires:       device-mapper-multipath
Requires:       iscsi-initiator-utils
Requires:       lsscsi >= 0.29
Requires:       lvm2
Requires:       nfs-utils
Requires:       sg3_utils
Requires:       sysfsutils
Requires:       systemd-udev

Requires:       python3-retrying

BuildRequires:  python3-devel
BuildRequires:  python3-ddt
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  git
BuildRequires:  python3-reno
BuildRequires:  python3-oslo-concurrency  >= 3.8.0
BuildRequires:  python3-oslo-i18n >= 3.15.3
BuildRequires:  python3-oslo-log >= 3.36.0
BuildRequires:  python3-oslo-service >= 1.24.0
BuildRequires:  python3-os-win
BuildRequires:  python3-requests >= 2.14.2
BuildRequires:  python3-six >= 1.10.0
BuildRequires:  python3-setuptools
BuildRequires:  python3-oslo-privsep >= 1.32.0

%if 0%{?with_doc}
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinx
%endif

BuildRequires:  python3-retrying

%description -n python3-%{pypi_name}
%{common_desc}

%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git


%build
%{py3_build}

%install
%{py3_install}

%if 0%{?with_doc}
# generate html docs
sphinx-build-3 -b html doc/source doc/build/html
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

# Move config files to proper location
install -d -m 755 %{buildroot}%{_datarootdir}/%{pypi_name}/rootwrap
mv %{buildroot}/usr/etc/os-brick/rootwrap.d/*.filters %{buildroot}%{_datarootdir}/%{pypi_name}/rootwrap

%files -n python3-%{pypi_name}
%license LICENSE
%if 0%{?with_doc}
%doc doc/build/html
%endif
%doc README.rst
%{python3_sitelib}/os_brick*
%{_datarootdir}/%{pypi_name}
%exclude %{python3_sitelib}/os_brick/tests

%changelog
* Wed Aug 25 2021 Alan Bishop <abishop@redhat.com> 3.0.6-2
- Require systemd-udev

* Thu Apr 08 2021 RDO <dev@lists.rdoproject.org> 3.0.6-1
- Update to 3.0.6

* Mon Mar 15 2021 RDO <dev@lists.rdoproject.org> 3.0.5-1
- Update to 3.0.5

* Mon Jan 11 2021 RDO <dev@lists.rdoproject.org> 3.0.4-1
- Update to 3.0.4

* Mon Sep 14 2020 Eric Harney <eharney@redhat.com> 3.0.3-2
- Add lsscsi requirement

* Mon Sep 07 2020 RDO <dev@lists.rdoproject.org> 3.0.3-1
- Update to 3.0.3

* Thu Jun 04 2020 RDO <dev@lists.rdoproject.org> 3.0.2-1
- Update to 3.0.2

* Mon May 04 2020 Eric Harney <eharney@redhat.com> 3.0.1-2
- Add missing oslo and iSCSI dependencies

* Mon Apr 27 2020 RDO <dev@lists.rdoproject.org> 3.0.1-1
- Update to 3.0.1

