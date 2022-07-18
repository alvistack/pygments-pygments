%global debug_package %{nil}

Name: python-pygments
Epoch: 100
Version: 2.11.2
Release: 1%{?dist}
BuildArch: noarch
Summary: Generic syntax highlighter written in Python
License: BSD-2-Clause
URL: https://github.com/pygments/pygments/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Pygments is a generic syntax highlighter written in Python that supports
over 500 languages and text formats, for use in code hosting, forums,
wikis or other applications that need to prettify source code.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}
%if 0%{?centos_version} == 700
mv %{buildroot}%{_bindir}/pygmentize %{buildroot}%{_bindir}/pygmentize3
%endif

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-Pygments
Summary: Generic syntax highlighter written in Python
Requires: python3
Provides: python3-pygments = %{epoch}:%{version}-%{release}
Provides: python3dist(pygments) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pygments = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pygments) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pygments = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pygments) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-Pygments
Pygments is a generic syntax highlighter written in Python that supports
over 500 languages and text formats, for use in code hosting, forums,
wikis or other applications that need to prettify source code.

%files -n python%{python3_version_nodots}-Pygments
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-Pygments
Summary: Generic syntax highlighter written in Python
Requires: python3
Provides: python3-pygments = %{epoch}:%{version}-%{release}
Provides: python3dist(pygments) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pygments = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pygments) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pygments = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pygments) = %{epoch}:%{version}-%{release}

%description -n python3-Pygments
Pygments is a generic syntax highlighter written in Python that supports
over 500 languages and text formats, for use in code hosting, forums,
wikis or other applications that need to prettify source code.

%files -n python3-Pygments
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-pygments
Summary: Generic syntax highlighter written in Python
Requires: python3
Provides: python3-pygments = %{epoch}:%{version}-%{release}
Provides: python3dist(pygments) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pygments = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pygments) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pygments = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pygments) = %{epoch}:%{version}-%{release}

%description -n python3-pygments
Pygments is a generic syntax highlighter written in Python that supports
over 500 languages and text formats, for use in code hosting, forums,
wikis or other applications that need to prettify source code.

%files -n python3-pygments
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
