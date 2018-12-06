Name:           golang-github-oschwald-maxminddb-golang
Summary:        MaxMind DB Reader for Go
Version:        1.3.0
Release:        4%{?dist}
# Code: ISC; Test data: CC-BY-SA 3.0
License:        ISC and CC-BY-SA

# https://github.com/oschwald/maxminddb-golang
%global repo    maxminddb-golang
%global goipath github.com/oschwald/%{repo}
%global tag     v1.3.0

%gometa

URL:            %{gourl}
Source0:        %{gourl}/archive/%{tag}/%{repo}-%{version}.tar.gz

# test data for the non-exported git submodule
%global dataurl https://github.com/maxmind/MaxMind-DB
%global dataref 2159aef4f87fab9fb418da00307e3afd8722a56e
Source1:        %{dataurl}/archive/%{dataref}/MaxMind-DB-%{dataref}.tar.gz


%description
%{summary}


%package        devel
Summary:        %{summary}
BuildArch:      noarch

BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(golang.org/x/sys/unix)

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup -p1

# extract test data to the right location
pushd test-data
tar -xzf %{SOURCE1}
mv MaxMind-DB-%{dataref}/* ./
rm -r MaxMind-DB-%{dataref}
popd


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 1.3.0-4
- Use standard GitHub SourceURL again for consistency between releases.
- Use forgeautosetup instead of gosetup.

* Sun Sep 02 2018 Fabio Valentini <decathorpe@gmail.com> - 1.3.0-3
- Update to use spec 3.0 and enable tests.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 26 2018 Fabio Valentini <decathorpe@gmail.com> - 1.3.0-1
- Update to version 1.3.0.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Fabio Valentini <decathorpe@gmail.com> - 1.2.1-1
- Update to version 1.2.1.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 07 2017 Fabio Valentini <decathorpe@gmail.com> - 1.2.0-1
- Update to version 1.2.0.

* Mon Mar 13 2017 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-1.git697da80
- First package for Fedora

