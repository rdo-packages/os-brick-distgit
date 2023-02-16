%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global pypi_name os-brick

%global with_doc 1

%global common_desc \
OpenStack Cinder brick library for managing local volume attaches

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
Summary:        OpenStack Cinder brick library for managing local volume attaches

License:        ASL 2.0
URL:            http://www.openstack.org/
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

%description
%{common_desc}

%package -n python3-%{pypi_name}
Summary:        OpenStack Cinder brick library for managing local volume attaches
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       os-brick = %{version}-%{release}

Requires:       python3-pbr
Requires:       python3-oslo-concurrency >= 5.0.0
Requires:       python3-oslo-context >= 4.1.0
Requires:       python3-oslo-i18n >= 5.1.0
Requires:       python3-oslo-log >= 4.8.0
Requires:       python3-oslo-serialization >= 4.3.0
Requires:       python3-oslo-service >= 2.8.0
Requires:       python3-oslo-utils >= 6.0.0
Requires:       python3-requests >= 2.25.1
Requires:       python3-oslo-privsep >= 3.0.0
Requires:       python3-os-win >= 5.7.0
Requires:       cryptsetup
Requires:       device-mapper-multipath
Requires:       iscsi-initiator-utils
Requires:       lsscsi >= 0.29
Requires:       lvm2
Requires:       nfs-utils
Requires:       nvme-cli
Requires:       sg3_utils
Requires:       systemd-udev

Requires:       python3-tenacity
Requires:       python3-oslo-config >= 9.0.0

BuildRequires:  openstack-macros
BuildRequires:  python3-devel
BuildRequires:  python3-ddt
BuildRequires:  python3-fixtures
BuildRequires:  python3-pbr >= 5.5.0
BuildRequires:  git-core
BuildRequires:  python3-reno
BuildRequires:  python3-oslo-concurrency  >= 4.4.0
BuildRequires:  python3-oslo-i18n >= 5.0.1
BuildRequires:  python3-oslo-log >= 4.4.0
BuildRequires:  python3-oslo-service >= 2.5.0
BuildRequires:  python3-os-win
BuildRequires:  python3-requests >= 2.25.1
BuildRequires:  python3-setuptools
BuildRequires:  python3-oslo-privsep >= 2.4.0
BuildRequires:  python3-oslo-vmware
BuildRequires:  python3-oslo-config
BuildRequires:  python3-testtools

# Castellan is only for unit tests
BuildRequires:  python3-castellan

%if 0%{?with_doc}
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinx
%endif

BuildRequires:  python3-tenacity

%description -n python3-%{pypi_name}
%{common_desc}

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{pypi_name}-%{upstream_version} -S git
%py_req_cleanup


%build
%{py3_build}

%check
python3 setup.py test

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
