%global pkg     mongokit

Name:           python-mongokit
Version:        0.9.1.1
Release:        1%{?dist}
Summary:        Structured schema and validation layer on top of PyMongo

Group:          Development/Languages
License:        New BSD License
URL:            http://namlook.github.com/%{pkg}/
Source0:        https://pypi.python.org/packages/source/m/%{pkg}/%{pkg}-%{version}.tar.gz

BuildArch:      noarch

Provides:       mongokit

Requires:       python-pymongo >= 2.5, python-pymongo-gridfs
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
%doc AUTHORS LICENSE README.md
%{python_sitelib}/*


%changelog
* Fri Aug 22 2014 Eugene G. Zamriy <eugene@zamriy.info> - 0.9.1.1-1
- update to 0.9.1.1 version

* Wed Sep 25 2013 Eugene G. Zamriy <eugene@zamriy.info> - 0.9.0-1
- update to 0.9.0 version. Now requires python-pymongo >= 2.5

* Wed Jul 10 2013 Eugene G. Zamriy <eugene@zamriy.info> - 0.8.3-2
- Added missing dependency python-pymongo-gridfs

* Mon Jul  8 2013 Eugene G. Zamriy <eugene@zamriy.info> - 0.8.3-1
- initial release. 0.8.3 version
