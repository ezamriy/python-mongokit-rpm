%global pkg     mongokit

Name:           python-mongokit
Version:        0.8.3
Release:        1%{?dist}
Summary:        Structured schema and validation layer on top of PyMongo

Packager:       Eugene Zamriy <eugene@zamriy.info>

Group:          Development/Languages
License:        New BSD License
URL:            http://namlook.github.com/%{pkg}/
Source0:        https://github.com/namlook/%{pkg}/archive/v%{version}.tar.gz

BuildArch:      noarch

Provides:       mongokit

Requires:       python-pymongo >= 2.0.1
BuildRequires:  python-devel, python-setuptools


%description
MongoKit is a python module that brings structured schema and validation layer
on top of the great pymongo driver. It has be written to be as simple and light
as possible with the KISS and DRY principles in mind.


%prep
%setup -q -n %{pkg}-%{version}


%build
%{__python} setup.py build


%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%clean
%{__rm} -rf %{buildroot}
 

%files
%defattr(-,root,root,-)
%doc AUTHORS CHANGELOG LICENSE README
%{python_sitelib}/*


%changelog
* Mon Jul  8 2013 Eugene G. Zamriy <eugene@zamriy.info> - 0.8.3-1
- initial release. 0.8.3 version
